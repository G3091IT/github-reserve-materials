---
title: AI 投标技术文件资料整理（五主题分类）
source: GitHub 公开仓库（github-tools-scout 实时检索 + 储备仓库既有归档）
topic: 04_投标技术文件
date: 2026-11-16
harvest_date: 2026-11-16
url: https://github.com/G3091IT/github-reserve-materials
tags: [公开学习库, 投标实务, AI投标, 技术标, GitHub资料]
---

# AI 投标技术文件资料整理（五主题分类）

> 来源：GitHub 公开仓库，经 github-tools-scout 实时检索打分 + 储备仓库既有归档交叉整理。
> 检索时间：2026-11-16。结论分级：ADOPT=可优先采纳 / REVIEW=先核对 / AVOID=弃坑。
> 说明：以下"主要内容与用途"基于各仓库 README 与方法论文档的**已核实内容**；"可借鉴之处"为**基于文档的推断**，已标注。

## 检索到的相关仓库总览（按结论分级）

| 仓库 | 结论 | 质量/适配 | 星标 | 许可证 | 一句话定位 |
|---|---|---|---|---|---|
| FB208/OpenBidKit_Yibiao | ADOPT | 96.4/53.7 | 3338 | AGPL-3.0 | AI 标书编写工具箱：生成、知识库、查重、废标项检查 |
| guangshu100/BidMaster-Pro | ADOPT | 85.3/56.6 | 455 | AGPL-3.0 | 全流程智能招投标 Agent：解读/生成/检查/排版 |
| tiettuo/claude-bid-gen | ADOPT | 77.5/70.0 | 9 | MIT | 工程投标技术标/施工组织设计全流程生成管道 |
| HunterLzap/rag-tender | ADOPT | 74.9/56.6 | 96 | MIT | 本地化 RAG 标书解析、资质匹配、红线提醒 |
| zeronezer/bidcraft | ADOPT | 74.2/65.0 | 85 | Apache-2.0 | 对话式标书编制系统，AI 编制技术标 |
| hello-fengsir/godbiao | ADOPT | 72.3/60.0 | 31 | MIT | AI 标书比对 + 制标参数化管理 |
| matongAI-lab/tender-review-kit | ADOPT | 78.4/47.9 | 52 | MIT | 投标审核工具包，关键词/规则识别风险 |
| yoligehude14753/docforge | REVIEW | 64.0/50.0 | 15 | MIT | AI 投标/方案文档生成器 |
| tianlian0/paper_checking_system | REVIEW | 69.4/48.7 | 520 | GPL-2.0 | 文本查重系统（标书查重、防串标），STALE>1y |
| danielcopper/romm-tender | 误收 | — | 215 | GPL-3.0 | 实为 Steam Deck ROM 插件，名含 tender 但与投标无关 |
| fakelilway/TenderDoc-Generator | AVOID | 57.5/12.0 | 5 | 无 | 多智能体招标文档生成，无许可证 |
| xinsuifan-web/Tender-Assistant-V2.5 | AVOID | 56.1/50.0 | 86 | 无 | 招标投标工作流 AI Agent 原型，无许可证 |
| xinsuifan-web/Cloud-Platform-for-Construction-Project-Bidding | AVOID | 52.8/50.0 | 43 | 无 | 建设工程招投标 SaaS 平台，无许可证 |

---

## 一、定义与适用范围

**主要内容**：各仓库对"AI 投标技术文件"的界定与适用场景。

- **tiettuo/claude-bid-gen**（来源类型：开源项目·方法论文档）：将 AI 投标技术文件定义为**工程类招投标的全流程施工组织设计/技术标生成管道**——从原始招标 PDF/DOCX 抽取，到机器审校 + 合规检查 + 批量投标相似度防围标。适用：工程投标技术标、施工组织设计。（已核实）
- **zeronezer/bidcraft**（开源项目·README）：界定技术标为**工程文档真实结构**——施工组织设计动辄几百页、几十万字，其中真正"因项目而异"的不到 20%，剩下 80% 是抄改+拼装。适用：工程投标技术标编制，目标是"把抄改拼装的 80% 交给 AI，把人的时间还给 20% 的判断"。（已核实）
- **guangshu100/BidMaster-Pro**（开源项目·README）：将 AI 投标技术文件定位为**全流程智能招投标 Agent**，覆盖招标解读、投标生成、投标检查、文档排版四阶段。适用：从招标公告到可交付 docx 的全流程。（已核实）
- **hello-fengsir/godbiao**（开源项目·README）：界定 AI 投标为两大动作——**评标**（上传标书自动逐条核查）与**制标**（参数化管理一键导出）。适用：标书核查与制标。（已核实）

**用途**：明确 AI 投标技术文件的边界——核心是**工程投标技术标/施工组织设计**的生成与核查，部分工具延伸至商务标、查重、废标检查。

---

## 二、编写规范与格式要求

**主要内容**：各仓库对投标技术文件格式、结构、排版的规范要求。

- **tiettuo/claude-bid-gen**（开源项目·文档）：提供 `docs/chart_schemas.md`（**7 种图表渲染器精确 schema**）、`bid-gen-flowchart.html`（Mermaid 业务流程图）、`bid_format_audit.py`（**格式审计**脚本）、`bid_plan_verify.py`（**三铁律校验**）、`bid_assemble.py`（DOCX 组装，2450 行）。（已核实）
- **guangshu100/BidMaster-Pro**（开源项目·README）：文档输出模块规定——**智能排版**（字体/段落）、**模板配置**、**多格式导出**（docx 为唯一中间格式，可导 doc/PDF）、**格式检查/差异对比**（与期望模板逐项对比可自动修正）、**修订模式**（多人协作批注）。（已核实）
- **zeronezer/bidcraft**（开源项目·README）：**目录生成**——招标文件规定了目录就优先采用，没规定则按工程类型生成；**Mermaid 关系图**（流程/组织类图用 Mermaid 表达、编辑器实时渲染）；**全局事实表**（每个数字都有出处、可追溯）。（已核实）
- **hello-fengsir/godbiao**（开源项目·README）：**格式评估**——检测标书格式问题（字体、排版、缺失章节等）。（已核实）

**用途**：提供投标技术文件在结构、图表、排版、格式校验上的具体规范与可执行检查项。

---

## 三、核心内容构成（技术方案、资质证明、评分要点等）

**主要内容**：投标技术文件应包含的核心要素，各仓库的结构化拆解。

- **zeronezer/bidcraft**（开源项目·README）：**招标文件解析**结构化落库——标段划分、评分办法、技术要求、编制要求、规定的目录结构；**标段隔离**（正文不混入其他标段工点）；**知识库**（历史施组→知识页：编制方式+要点+典型表图）；**工艺工法库**；**逐章编写思路**；**正文流式生成**；**全局事实表**（工期/里程/数量）。（已核实）
- **guangshu100/BidMaster-Pro**（开源项目·README）：**招标解读**——识别评分标准、资质要求、技术参数，生成**评分矩阵**；**投标生成**——大纲生成、内容创作、知识检索、AI 配图；**投标检查**——资格审查（企业资质/业绩/人员）、一致性校验、重复率检测、价格合理性、**21 项专业检查**（保证金/签字盖章/有效期等）；**MinerU OCR**扫描件抽取。（已核实）
- **tiettuo/claude-bid-gen**（开源项目·文档）：**骨架 JSON**（evaluation/outline/disqualification）、**13 字段事实抽取**、Tier 2 派生、Tier 4 特殊抽取、**范本匹配**、**机器审校**、**废标合规扫描**、**交叉相似度**（批量防围标）。（已核实）
- **hello-fengsir/godbiao**（开源项目·README）：**逐项核查**——AI 提取招标要求，逐条比对投标响应（三路并行分析）；**关键信息提取**——金额、货期、资质等商务关键项。（已核实）
- **HunterLzap/rag-tender**（开源项目·摘要）：**资质匹配**与红线提醒。（已核实）
- **matongAI-lab/tender-review-kit**（开源项目·摘要）：用关键词、规则和自动化检查辅助识别**投标风险**。（已核实）

**用途**：明确投标技术文件的核心构成——技术方案（施工组织设计/施组）、资质证明、评分要点、商务关键项、合规/废标要素。

---

## 四、常见撰写技巧与注意事项

**主要内容**：编写过程中的技巧、避坑与质量保障。

- **tiettuo/claude-bid-gen**（开源项目·方法论文档 `extraction-methodology.md`）：**四阶段闭环 + 八条铁律 + 历史失败案例**；**三铁律校验**（Step 2）；**机器审校**（Step 3.5）；**废标合规扫描**（Step 5）；**交叉相似度防围标**（Step 6）。（已核实）
- **zeronezer/bidcraft**（开源项目·README）：**先对齐思路再动手写**（逐章编写思路，避免几十万字写完才发现方向偏）；**人是审核者与决策者，不是打字员**；**全局事实表**杜绝"同一个数在文档里出现三种写法"；**经验学习**（每次改稿/否决/提意见沉淀为写法偏好）；**废标风险的话不能写**（建模进编制流程）。（已核实）
- **guangshu100/BidMaster-Pro**（开源项目·README）：**21 项合规检查**（保证金/签字盖章/有效期/一致性/重复率/价格合理性）；**风险预警**（多维度标记潜在废标风险点）；**评分矩阵**对照。（已核实）
- **hello-fengsir/godbiao**（开源项目·README）：**逐条核查防止标书出错**。（已核实）
- **HunterLzap/rag-tender**（开源项目·摘要）：**红线提醒**。（已核实）

**用途**：提供编写阶段的质量保障技巧——思路先行、事实可溯、合规检查、防废标、防围标、经验沉淀。

---

## 五、可参考的行业案例与相关标准

**主要内容**：可参考的案例与标准。

- **tiettuo/claude-bid-gen**（开源项目·文档）：`chart_schemas.md`（7 种图表渲染 schema）、`bid-gen-flowchart.html`（业务流程图）——**可作结构规范参考**。（已核实）
- **guangshu100/BidMaster-Pro**（开源项目·README）：**评分矩阵**、**21 项合规检查规则**——**可作检查标准参考**。（已核实）
- **zeronezer/bidcraft**（开源项目·README）：以**虚构演示项目**（云岭至江口高速公路 YJ-3 合同段）演示完整编制流程——**可作流程案例参考**（但为虚构演示，非真实中标案例）。（已核实）

**⚠ 缺失说明（重要）**：
- GitHub 上**未检索到权威的国家/行业标准文件**（如 GB/T、住建部/发改委发布的投标技术文件编制标准）。此类标准文件需从**国家发改委、住建部、各省市公共资源交易中心**等官方渠道获取，不在 GitHub 公开仓库范畴。**本类在 GitHub 渠道下部分缺失。**
- 上述仓库均为**开源实现/方法论**，可作实践参考，但**不能替代官方标准文本**。

---

## 附：AI 投标文件高分 / 获奖文本清单

**⚠ 明确说明：本类资料缺失。**

- 经多组定向检索（`bid document template sample`、`tender bid winning proposal`、`bid proposal sample docx`、`tender winning document`、`construction proposal template`、`标书 范本 模板`、`标书 中标 案例` 等），**均无结果**。
- **原因**：AI 投标文件的高分/获奖文本多为**企业内部或涉密内容**，**不在 GitHub 公开**。GitHub 公开仓库提供的是**工具、方法论、流程演示**，而非真实的高分/获奖标书文本。
- **可参考的替代**：部分仓库提供**功能演示样例**（如 bidcraft 的虚构演示项目、claude-bid-gen 的图表 schema 与流程图），但**这些是功能演示，非高分/获奖文本**，不能作为"高分获奖文本"使用。
- **结论**：在 GitHub 渠道下，**AI 投标文件高分/获奖文本这一类别缺失**，需从企业自有中标标书库、行业评奖公示、公共资源交易中心中标公示等渠道获取。

---

## 出处（MLA）

各仓库 README 与方法论文档，经 github-tools-scout 实时检索，2026-11-16 访问。主要来源：

tiettuo. "claude-bid-gen: 投标技术文件生成系统." *GitHub*, github.com/tiettuo/claude-bid-gen, 2026-11-16 访问。

zeronezer. "标书匠 BidCraft · 对话式标书编制系统." *GitHub*, github.com/zeronezer/bidcraft, 2026-11-16 访问。

guangshu100. "BidMaster Pro - 全流程智能招投标平台." *GitHub*, github.com/guangshu100/BidMaster-Pro, 2026-11-16 访问。

hello-fengsir. "神奇阿标 God Biao · AI 智能招投标工具." *GitHub*, github.com/hello-fengsir/godbiao, 2026-11-16 访问。

FB208. "OpenBidKit_Yibiao · AI 标书编写工具." *GitHub*, github.com/FB208/OpenBidKit_Yibiao, 2026-11-16 访问。

HunterLzap. "rag-tender · 招投标 RAG 助手." *GitHub*, github.com/HunterLzap/rag-tender, 2026-11-16 访问。

matongAI-lab. "tender-review-kit · 投标审核工具包." *GitHub*, github.com/matongAI-lab/tender-review-kit, 2026-11-16 访问。
