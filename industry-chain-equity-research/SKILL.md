---
name: industry-chain-equity-research
description: 科技与AI产业链投研标的挖掘与定量验证流程。Use when Codex needs to research AI产业链、AI服务器、GPU/ASIC、HBM、CoWoS/先进封装、半导体设备材料、云平台、模型API、Agent/SaaS、PCB、光模块、MLCC/被动元件、功率半导体等链条，按美国为主中国为辅的全球产业链框架，先从问题、BOM、拓扑、供应商、客户认证、产能瓶颈、价格传导和商业化收入中挖掘候选公司，再建立供需缺口、利润池、竞争强度、利润弹性、三年情景预测和估值比较。
---

# Industry Chain Equity Research

## Overview

Use this skill to turn a qualitative technology-industry chain idea into a disciplined equity research workflow. Start from the problem a chain solves, reconstruct the real product and business chain, discover companies from evidence, then force every candidate through quantitative supply-demand, profit-pool, competition, profit, and valuation checks.

This skill is not investment advice. Treat outputs as research hypotheses that require source-backed data, explicit assumptions, and downside falsification.

## Quick Start

For a rough note, transcript, or social-media style thesis, do not start by listing familiar stocks. Start by building the chain:

1. Define the problem being solved: data and compute turning into automated decisions, content, code, search, recommendation, API calls, or enterprise workflows.
2. Identify where value converts into revenue, profit, and cash flow: token cost decline, usage growth, enterprise willingness to pay, cloud ROIC, or hardware shortage.
3. Reconstruct the product BOM, system topology, capacity bottlenecks, and commercial flow from sources.
4. Map the chain by layer, with US/global leaders first and China-related players second; do not force a China proxy if the actual profit pool is offshore.
5. Discover companies from filings, supplier lists, customer certifications, capacity announcements, industry reports, and price trackers.
6. Quantify only after the chain and company exposure are evidence-backed.

Use `references/research-output-template.md` as the final output structure.

## AI Industry Chain Lens

For AI, the core question is not "AI is good." The investable question is: who benefits when token cost falls, token usage rises, and AI usage turns into revenue, profit, and cash flow. The highest certainty often starts in infrastructure because hyperscalers and model companies still compete for compute even when downstream application monetization is uncertain.

Use a US/global-first and China-second lens:

- Treat US/global leaders as the primary profit-pool and bottleneck map.
- Treat China companies as domestic substitution, capacity catch-up, application localization, or policy-constrained alternatives.
- Keep overseas, private, and non-listed companies in the map when they explain bottlenecks, pricing, or substitution.
- Separate "global leader economics" from "China proxy economics"; they may have different margins, customers, export-control constraints, and valuation logic.

### Eight-Layer AI Framework

Analyze AI from supply bottleneck to demand realization:

| Layer | Solves | Global core players | China-related players | Profit/competition judgment |
|---|---|---|---|---|
| Semiconductor equipment / EDA / materials | Tools and materials for advanced chip production | ASML, Applied Materials, Lam Research, KLA, Synopsys, Cadence | 北方华创, 中微公司, 华大九天, 上海微电子 | High margins and strong barriers; China logic is mainly domestic substitution |
| Foundry / advanced packaging | Manufacturing AI chips and solving process / CoWoS / packaging bottlenecks | TSMC, Samsung Foundry, Intel Foundry | SMIC, 华虹, 长电科技, 通富微电 | High profit pool; TSMC and advanced packaging are key bottlenecks |
| AI GPU / accelerator | Training and inference compute | Nvidia, AMD, Broadcom, Marvell, Google TPU, Amazon Trainium/Inferentia, Microsoft Maia | Huawei Ascend, 寒武纪, 海光, 壁仞, 摩尔线程 | Highest profit pool now; Nvidia dominant short term, ASIC share may rise long term |
| HBM / memory / storage | Feeds data to GPU and relieves memory bandwidth bottleneck | SK Hynix, Samsung, Micron, Western Digital | 长江存储, 长鑫存储 | Margins rising with tight HBM supply; cyclical risk remains |
| Server / network / liquid cooling / power | Turns chips into deployable clusters | Dell, Supermicro, Arista, Cisco, Vertiv, Eaton, Schneider, Corning | 工业富联, 浪潮信息, 中际旭创, 新易盛, 曙光, 英维克 | Profit splits; network/power/liquid cooling often better than generic ODM |
| Cloud / IaaS | Sells compute capacity to model companies and enterprises | AWS, Microsoft Azure, Google Cloud, Oracle Cloud, CoreWeave | 阿里云, 腾讯云, 华为云, 百度智能云, 火山引擎 | Revenue certainty can be high, but capex burden and ROIC decide valuation |
| Foundation model / API | Turns compute into intelligence and API products | OpenAI, Anthropic, Google DeepMind, Meta, xAI, Mistral | DeepSeek, 阿里通义, 百度文心, 智谱, 月之暗面, MiniMax, 百川 | Growth can be high, but inference cost, open-source pressure, and API pricing matter |
| Application / Agent / SaaS | Embeds AI into workflows and user outcomes | Microsoft, Adobe, Salesforce, ServiceNow, Palantir, Intuit, Datadog | 金山办公, 科大讯飞, 同花顺, 用友, 金蝶, 万兴, 昆仑万维 | Long-term alpha may exist, but feature commoditization and retention risk are high |

### Profit Pool And Crowding Ranking

Use this as a starting hypothesis, then verify with current filings and data:

1. AI GPU / accelerator platform: currently the strongest profit pool if ecosystem lock-in, software stack, supply allocation, and pricing remain intact.
2. HBM: high and rising when GPU memory bandwidth is the binding constraint.
3. Advanced foundry / advanced packaging: high profit pool when CoWoS or advanced nodes constrain AI chip supply.
4. AI network / power / liquid cooling: medium-high profit pool as clusters shift from single-card procurement to system engineering.
5. Cloud platform: revenue can be large and sticky, but depreciation and utilization decide ROIC.
6. Model API: wide dispersion; strong brands and best models may monetize, but open-source and API price cuts compress profit.
7. Generic application layer: easiest to be rolled if the product is a feature rather than a standalone workflow with retention and pricing power.
8. Server ODM: often one of the easiest to be rolled unless tied to high-end liquid cooling, rack-scale integration, or scarce customer access.

### Key Variables Dashboard

Track these before upgrading a thesis:

- Hyperscaler capex and its mix between training, inference, network, power, and data centers.
- GPU delivery, HBM capacity / pricing, CoWoS capacity, and advanced packaging allocation.
- Inference token growth and cost per token decline.
- Enterprise AI paid conversion, retention, seat expansion, ARPU, and gross margin.
- Data center power, grid connection, cooling, land, and permitting constraints.
- US export controls and China's domestic substitution progress.
- Open-source model pressure on API pricing.
- Cloud vendor depreciation cycle, utilization, and ROIC.
- Model benchmark progress versus actual enterprise adoption.
- Inventory, order backlog, lead times, and cancellation signals across hardware layers.

## Workflow

### 1. Frame the seed precisely

Identify:

- Seed event: price move, earnings revision, shortage, policy, product launch, capacity bottleneck, or overseas leader rerating.
- Seed product: GPU, ASIC, HBM, CoWoS, AI服务器, 光模块, PCB, MLCC, 液冷, 电力设备, 模型API, Agent/SaaS, etc.
- Seed company: the stock or overseas leader that started the idea.
- Chain layer: downstream demand, same-system component, upstream material/equipment, same-category substitute, or capacity-spillover beneficiary.
- Time window: current year, next year, or three-year scenario horizon.

Separate explicit facts from inferred links. If the user provides a historically validated case, treat it as a forward-test: check whether the workflow would have surfaced the relevant product links, profit pools, and companies before the price move.

### 2. Build the product chain before naming stocks

Do the industry-chain digging first:

- Same-system BOM: for the seed product, identify required components, materials, equipment, consumables, and integration links. Example: AI服务器 -> GPU/CPU/HBM/PCB/电源/散热/连接器/光模块/MLCC/电感/线缆.
- Topology and unit intensity: understand why scale changes component usage. Example: AI集群网络拓扑 can increase optical-module and high-speed interconnect intensity.
- Upstream decomposition: break hot components into materials and process bottlenecks. Example: PCB -> 覆铜板 -> 电子布/树脂/铜箔; MLCC -> 陶瓷粉体/内电极/载带/离型膜/烧结设备.
- Adjacent substitution: identify whether high-end shortage squeezes mid/low-end capacity, whether overseas supply tightness benefits domestic substitutes, and whether non-listed leaders reveal listed peers.
- Downstream validation: confirm which end customers or use cases are actually pulling demand, not merely thematically related.
- Business-model flow: show how the layer makes money, who pays, whether revenue is usage-based / capacity-based / license-based / hardware shipment-based, and what can compress margin.

Do not output a company just because it is a familiar name in the sector. Every company must be tied to a specific product, customer, capacity, or certification link.

### 3. Discover companies from evidence

Use a search-and-evidence loop:

- Find product names and technical synonyms first, then search companies. Do not only search stock names.
- Use annual reports, IPO prospectuses, investor Q&A, exchange announcements, patents, customer certification notes, industry association data, price trackers, import/export data, and credible industry reports.
- Build a longlist by chain node: global leaders, domestic listed companies, private companies, upstream suppliers, equipment/material bottlenecks, and indirect beneficiaries.
- For each company, record evidence quality: direct supplier disclosure, customer certification, capacity announcement, product page only, or market rumor.
- Keep private or overseas companies in the map if they explain capacity, price, or substitution pressure, even if they are not directly investable.
- For AI cases, explicitly record whether the company belongs to infrastructure capex, cloud revenue, model API revenue, or application monetization. These are different investment questions.

### 4. Quantify before ranking

Do not rank candidates on story quality alone. Build a minimal model:

- Demand: current demand, unit intensity, future volume driver, and three-year demand under optimistic/base/bear cases.
- Supply: current effective capacity, utilization, inventory, new capacity under construction, qualification cycle, and realistic ramp timing.
- Gap: demand minus effective supply, duration of shortage/surplus, and sensitivity to utilization/ramp assumptions.
- Price: historical price range, current quote, expected price increase/decrease, and pass-through timing.
- Profit: revenue sensitivity, gross margin sensitivity, operating leverage, tax/minority-interest effects if material, and net profit increment.
- Valuation: use PE, PB, PS, EV/EBITDA, or another metric that matches the business model; compare current valuation to its own history and peers.
- Competition: identify whether the layer is protected by technology, ecosystem, capacity, customer qualification, regulation, or whether it is exposed to commoditization and price war.

Prefer exact formulas with cited source numbers. If data is missing, state the assumption and show how the conclusion changes if the assumption is wrong.

### 5. Output the decision table

Use the template in `references/research-output-template.md`. The final comparison must include:

- Candidate company or target direction.
- Chain role and expansion route.
- Evidence that connects the company to the chain node.
- Layer profit-pool judgment and competition intensity.
- Core catalyst and main constraint.
- Supply-demand gap and expected duration.
- Price elasticity and profit elasticity.
- Three-year optimistic/base/bear financial assumptions.
- Current implied valuation based on next-year or forward scenario metrics.
- Key falsification signals.

Rank by measurable upside/downside, not by narrative excitement. Highlight the lowest valuation with the highest earnings elasticity only if the underlying assumptions survive the bear case.

## Data Discipline

- Use recent filings, exchange announcements, investor relations materials, industry association data, price trackers, customs data, channel checks, or credible sell-side/industry reports when available.
- For live market data, verify with current sources before citing prices, market caps, or valuation percentiles.
- Distinguish China-listed companies, overseas leaders, private suppliers, products, materials, and broad themes.
- Never present a company as investable only because it is mentioned in a chain. Require exposure, capacity, margin, valuation, and timing evidence.
- Avoid hard-coded stock pools. The candidate set is incomplete until the chain map, supplier map, and capacity map have been searched.
- Do not freeze current numeric examples into the skill. When citing capex, revenue growth, margins, HBM price, CoWoS capacity, or API pricing, verify with current filings and dated sources.
- Always include at least one reason the thesis could fail.

## Validation Standard

When validating this skill on a historical case, success means:

- It reconstructs the relevant product chain and AI layer, including non-obvious links such as MLCC/passive components, power, liquid cooling, CoWoS, HBM, or API pricing when the system or business model supports them.
- It finds companies through evidence sources, not a prewritten candidate list.
- It labels missed branches and explains what additional searches are needed.
- It separates market-validated hindsight from facts that would have been knowable at the time.
- It identifies which layers are likely profit pools and which layers are easiest to be rolled.
- It produces a researchable longlist plus a quantified shortlist, rather than claiming to find every possible company.

## Bundled Resources

- `references/research-output-template.md`: A concise research-note template for chain maps, candidate tables, supply-demand models, profit sensitivity, valuation comparison, and falsification checks.
