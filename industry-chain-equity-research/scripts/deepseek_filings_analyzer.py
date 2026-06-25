#!/usr/bin/env python3
"""Analyze filings with DeepSeek and emit an HTML research note.

The script intentionally reads the API key from an environment variable and
never persists it to disk.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request


DEFAULT_ENDPOINT = "https://api.deepseek.com/chat/completions"
DEFAULT_MODEL = "deepseek-chat"


def read_text_file(path: pathlib.Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "big5", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def strip_html(text: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return html.unescape(text)


def extract_pdf_text(path: pathlib.Path) -> str:
    try:
        import pdfplumber  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "PDF input requires pdfplumber. Convert the filing to text first, "
            "or run in a Codex workspace runtime that includes pdfplumber."
        ) from exc

    pages: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")
    return "\n".join(pages)


def extract_text(path: pathlib.Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf_text(path)
    text = read_text_file(path)
    if suffix in {".html", ".htm"}:
        text = strip_html(text)
    return text


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t\r\f\v]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_source_blocks(paths: list[pathlib.Path], per_file_chars: int, total_chars: int) -> list[dict[str, str]]:
    blocks: list[dict[str, str]] = []
    used = 0
    for path in paths:
        text = clean_text(extract_text(path))
        if not text:
            continue
        room = max(0, total_chars - used)
        if room <= 0:
            break
        clipped = text[: min(per_file_chars, room)]
        used += len(clipped)
        blocks.append(
            {
                "name": path.name,
                "path": str(path),
                "chars_used": str(len(clipped)),
                "text": clipped,
            }
        )
    return blocks


def build_prompt(topic: str, blocks: list[dict[str, str]]) -> str:
    sources = []
    for idx, block in enumerate(blocks, 1):
        sources.append(
            f"【来源 {idx}: {block['name']}】\n"
            f"路径：{block['path']}\n"
            f"截取字符数：{block['chars_used']}\n"
            f"{block['text']}"
        )

    return f"""你是严谨的中文科技产业链卖方研究员。请基于下列公告、招股书、年报、SEC 文件或财报文本，分析主题：
{topic}

要求：
1. 严格区分“已披露事实”“合理推断”“证据不足/未披露”，不要把推断写成事实。
2. 如果材料没有披露客户、供应商、设备数量、产能规模或订单金额，必须写“未披露”。
3. 面向产业链投研，重点拆解产品链、设备链、材料链、产能瓶颈、客户认证、价格/利润弹性和反证信号。
4. 不要给买入/卖出建议，不要给目标价，不要承诺收益。
5. 每只上市标的必须带股票代码和交易所后缀，例如 `688012.SH 中微公司`、`300750.SZ 宁德时代`、`NVDA.O Nvidia`。未上市或私有公司必须写 `未上市/私有`，不要省略代码列。
6. 输出中文 Markdown，使用以下结构：
   - 核心结论
   - 材料清单与证据强度
   - 已披露事实
   - 产业链/设备链拆解
   - 公司或标的对比表（必须包含“股票代码/交易所”列）
   - 量化假设与敏感性
   - 待验证问题
   - 风险与反证信号
   - 可继续跟踪的公告/财报关键词

文本材料如下：

{chr(10).join(sources)}
"""


def call_deepseek(
    prompt: str,
    api_key: str,
    endpoint: str,
    model: str,
    temperature: float,
    max_tokens: int,
) -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "你是严谨的中文投研文本分析助手，重视证据强弱和反证信号。",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"DeepSeek HTTP {exc.code}: {body[:1000]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"DeepSeek network error: {exc}. If this happens inside a sandbox, rerun with network approval."
        ) from exc
    return data["choices"][0]["message"]["content"]


def render_html(title: str, topic: str, analysis_md: str, blocks: list[dict[str, str]]) -> str:
    source_items = "\n".join(
        f"<li><code>{html.escape(block['name'])}</code> "
        f"<span>{html.escape(block['chars_used'])} chars</span></li>"
        for block in blocks
    )
    today = dt.date.today().isoformat()
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft YaHei", Arial, sans-serif; color: #17202a; line-height: 1.65; background: #fff; }}
    main {{ max-width: 1080px; margin: 0 auto; padding: 36px 24px 56px; }}
    header {{ border-bottom: 2px solid #d8dee6; margin-bottom: 22px; padding-bottom: 16px; }}
    h1 {{ font-size: 28px; margin: 0 0 10px; line-height: 1.25; }}
    .meta {{ color: #5d6d7e; font-size: 13px; display: flex; flex-wrap: wrap; gap: 12px; }}
    .sources {{ background: #f5f7fa; border: 1px solid #d8dee6; border-radius: 8px; padding: 12px 16px; margin: 18px 0; }}
    .sources ul {{ margin: 8px 0 0; padding-left: 22px; }}
    pre {{ white-space: pre-wrap; word-break: break-word; font-family: "Microsoft YaHei", Arial, sans-serif; font-size: 15px; background: #fff; }}
    footer {{ margin-top: 28px; padding-top: 14px; border-top: 1px solid #d8dee6; color: #5d6d7e; font-size: 13px; }}
  </style>
</head>
<body>
<main>
  <header>
    <h1>{html.escape(title)}</h1>
    <div class="meta">
      <span>生成日期：{today}</span>
      <span>主题：{html.escape(topic)}</span>
      <span>模型：DeepSeek</span>
    </div>
  </header>
  <section class="sources">
    <strong>输入材料</strong>
    <ul>
      {source_items}
    </ul>
  </section>
  <article>
    <pre>{html.escape(analysis_md)}</pre>
  </article>
  <footer>本报告由公开公告/财报文本和 DeepSeek 辅助生成，不构成投资建议。API key 未写入本文件。</footer>
</main>
</body>
</html>
"""


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Use DeepSeek to analyze filing/announcement text and write an HTML report."
    )
    parser.add_argument("--topic", required=True, help="Research topic or question.")
    parser.add_argument("--input", nargs="+", required=True, help="Input files: PDF, txt, md, html, json, csv.")
    parser.add_argument("--output-dir", required=True, help="Folder where index.html and analysis.md will be written.")
    parser.add_argument("--title", default="DeepSeek Filings Analysis", help="HTML report title.")
    parser.add_argument("--api-key-env", default="DEEPSEEK_API_KEY", help="Environment variable containing API key.")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT, help="DeepSeek API endpoint.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="DeepSeek model name.")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=4000)
    parser.add_argument("--per-file-chars", type=int, default=24000)
    parser.add_argument("--total-chars", type=int, default=100000)
    parser.add_argument("--save-prompt", action="store_true", help="Also save prompt.txt for auditability.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        print(f"Missing API key. Set {args.api_key_env}=<DeepSeek API key>.", file=sys.stderr)
        return 2

    input_paths = [pathlib.Path(p) for p in args.input]
    missing = [str(p) for p in input_paths if not p.exists()]
    if missing:
        print("Input file(s) not found: " + ", ".join(missing), file=sys.stderr)
        return 2

    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    blocks = build_source_blocks(input_paths, args.per_file_chars, args.total_chars)
    if not blocks:
        print("No text extracted from inputs.", file=sys.stderr)
        return 1

    prompt = build_prompt(args.topic, blocks)
    analysis = call_deepseek(
        prompt=prompt,
        api_key=api_key,
        endpoint=args.endpoint,
        model=args.model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )

    (output_dir / "analysis.md").write_text(analysis, encoding="utf-8")
    (output_dir / "index.html").write_text(
        render_html(args.title, args.topic, analysis, blocks),
        encoding="utf-8",
    )
    metadata = {
        "topic": args.topic,
        "title": args.title,
        "model": args.model,
        "endpoint": args.endpoint,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "inputs": [{k: v for k, v in block.items() if k != "text"} for block in blocks],
    }
    (output_dir / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    if args.save_prompt:
        (output_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

    print(str(output_dir / "index.html"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
