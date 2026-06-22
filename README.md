# AI Industry Chain Investment Research

这个仓库用于存放面向 AI 与科技产业链投研的 Codex skills。当前核心 skill 是 `industry-chain-equity-research`，用于把产业新闻、海外龙头变化、上游瓶颈或材料涨价，拆解成可验证的产业链、供应链、利润池和估值框架。

## 当前 Skill

### `industry-chain-equity-research`

这是一个面向科技与 AI 产业链投研的 skill。它不直接给股票池，也不根据题材联想熟悉公司，而是要求先重建真实产业链，再从产品、客户、产能、认证、价格、财报和公告证据中寻找候选标的。

适合研究的问题包括：

- AI 服务器、GPU、HBM、CoWoS、光模块、PCB、MLCC、液冷、电力设备等硬件链条怎么拆。
- HVLP 铜箔、电子布、覆铜板、先进封装材料等上游瓶颈如何映射到 A 股公司。
- 一条产业新闻应该选择系统厂、零部件、材料、设备，还是应用层。
- AI 产业链中哪些层级最赚钱，哪些层级最容易被卷。

入口文件：

```text
industry-chain-equity-research/SKILL.md
```

详细说明：

```text
industry-chain-equity-research/README.md
```

研究模板：

```text
industry-chain-equity-research/references/research-output-template.md
```

## 核心框架

skill 使用“美国/全球为主，中国为辅”的研究视角：

1. 先识别全球主导玩家、真实利润池和核心瓶颈。
2. 再判断中国公司属于国产替代、产能跟随、供应链配套、应用本地化，还是弱相关 proxy。
3. 不强行寻找中国映射；如果利润池主要在海外，需要如实标注。
4. 所有候选公司都必须有可验证证据，不能靠题材联想。

## AI 八层产业链

| 层级 | 核心问题 |
|---|---|
| 半导体设备 / EDA / 材料 | 谁提供先进芯片制造工具 |
| 晶圆代工 / 先进封装 | 谁解决制程和 CoWoS 等封装瓶颈 |
| AI GPU / 加速器 | 谁掌握训练与推理算力 |
| HBM / 内存 / 存储 | 谁解决内存带宽和数据供给 |
| 服务器 / 网络 / 液冷 / 电力 | 谁把芯片部署成可运行集群 |
| 云平台 / IaaS | 谁把算力卖给模型公司和企业 |
| 基础模型 / API | 谁把算力转化为通用智能能力 |
| 应用 / Agent / SaaS | 谁把 AI 嵌入具体工作流并收费 |

## 输出内容

一次完整研究通常应输出：

- 产业链挖掘地图
- 产业链节点搜索记录
- 候选标的对比表
- 利润池与被卷风险排序
- 关键变量仪表盘
- 供需测算
- 价格、成本与利润弹性
- 三年情景预测
- 估值比较
- 关键假设与反证清单

## 使用方式

在 Codex 中显式调用：

```text
Use $industry-chain-equity-research to research the A-share opportunities from 800V HVDC AI data center power architecture.
```

中文调用示例：

```text
调用投研 skill，研究 HVLP4 铜箔缺货对应的 A 股产业链标的。
```

## 仓库结构

```text
industry-chain-equity-research/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    research-output-template.md
```

## 免责声明

本仓库内容仅用于研究框架和信息组织，不构成投资建议。任何投资判断都需要结合最新公告、财报、行业数据、价格、估值和个人风险承受能力独立完成。
