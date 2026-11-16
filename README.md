# GitHub 储备资料仓库 · 总索引

- **采集日期**：2026-11-16
- **采集方式**：只读抓取公开仓库（github_scout 实时搜索+打分 + 领域关键词闸门过滤），全程未上传/未修改用户其他资料
- **API 调用**：核心 7 次 / 搜索 7 次
- **限流状态**：已触发 403，部分主题顺延至次日

## 各主题收录数量（累计，含历史）
- 01_招投标：5 个
- 02_工程造价：6 个
- 03_文档解析：6 个
- 04_投标技术文件：2 个
- 05_工程资料管理：2 个
- 06_关联检索：4 个

## 仓库清单（累计）
- [ADOPT] **FB208/OpenBidKit_Yibiao** — 01_招投标/FB208__OpenBidKit_Yibiao.md
- [ADOPT] **HunterLzap/rag-tender** — 01_招投标/HunterLzap__rag-tender.md
- [ADOPT] **danielcopper/romm-tender** — 01_招投标/danielcopper__romm-tender.md
- [ADOPT] **guangshu100/BidMaster-Pro** — 01_招投标/guangshu100__BidMaster-Pro.md
- [ADOPT] **matongAI-lab/tender-review-kit** — 01_招投标/matongAI-lab__tender-review-kit.md
- [ADOPT] **BruceLee1024/zaojia-database** — 02_工程造价/BruceLee1024__zaojia-database.md
- [ADOPT] **Kentucky-ai/opentakeoff** — 02_工程造价/Kentucky-ai__opentakeoff.md
- [ADOPT] **datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR** — 02_工程造价/datadrivenconstruction__OpenConstructionEstimate-DDC-CWICR.md
- [ADOPT] **getcadcraft/takeoffcraft** — 02_工程造价/getcadcraft__takeoffcraft.md
- [ADOPT] **jayden-lg/costing-master** — 02_工程造价/jayden-lg__costing-master.md
- [ADOPT] **osama-ata/Awesome-AECO** — 02_工程造价/osama-ata__Awesome-AECO.md
- [ADOPT] **Graphify-Labs/graphify** — 03_文档解析/Graphify-Labs__graphify.md
- [ADOPT] **chrisryugj/kordoc** — 03_文档解析/chrisryugj__kordoc.md
- [ADOPT] **happycola233/tchMaterial-parser** — 03_文档解析/happycola233__tchMaterial-parser.md
- [ADOPT] **landing-ai/ade-cli** — 03_文档解析/landing-ai__ade-cli.md
- [ADOPT] **opendataloader-project/opendataloader-pdf** — 03_文档解析/opendataloader-project__opendataloader-pdf.md
- [ADOPT] **run-llama/liteparse** — 03_文档解析/run-llama__liteparse.md
- [REVIEW] **tianlian0/paper_checking_system** — 04_投标技术文件/tianlian0__paper_checking_system.md
- [ADOPT] **zeronezer/bidcraft** — 04_投标技术文件/zeronezer__bidcraft.md
- [ADOPT] **3xxx/engineercms** — 05_工程资料管理/3xxx__engineercms.md
- [ADOPT] **datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction** — 05_工程资料管理/datadrivenconstruction__DDC_Skills_for_AI_Agents_in_Construction.md
- [ADOPT] **IAAR-Shanghai/Awesome-AI-Memory** — 06_关联检索/IAAR-Shanghai__Awesome-AI-Memory.md
- [ADOPT] **JEen-wang/Adaptive-rag** — 06_关联检索/JEen-wang__Adaptive-rag.md
- [ADOPT] **chaitin/PandaWiki** — 06_关联检索/chaitin__PandaWiki.md
- [ADOPT] **lhh737/KnowledgeBase-RAG-LLM-System** — 06_关联检索/lhh737__KnowledgeBase-RAG-LLM-System.md

## 本次运行新增
- 本次运行无新增（幂等跳过/限流顺延均属正常）

## 排除说明
- `_excluded/` 目录存放因「领域闸门/负向过滤」判定为无关（如政治类高分噪声仓库）而剔除的候选，保留以供审计。

本索引由自动化任务每晚更新；采集脚本见仓库根目录 `scout_runner.py`。