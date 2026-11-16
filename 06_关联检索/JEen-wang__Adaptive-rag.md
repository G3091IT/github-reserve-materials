# JEen-wang/Adaptive-rag

- **仓库名**：JEen-wang/Adaptive-rag
- **原文链接**：https://github.com/JEen-wang/Adaptive-rag
- **Star 数**：210（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-10-22T07:23:04Z
- **许可证**：MIT
- **语言**：Python
- **质量分 / 适配分 / 混合分**：87.4 / 47.6 / 69.5
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:rag/检索

## 用途摘要
按问题复杂度自动分流的电商客服 RAG：简单问题直接回答；复杂问题经过多跳检索并自我纠错；查单、退改通过工具调用完成，且高风险写操作必须先经人工确认。基于 FastAPI 和 LangGraph，混合检索并附带引用，内置离线评测与 Prometheus 指标。涵盖简历写法和项目面试拷打

## 适配理由
✓ 命中任务词：检索；△ 未命中：招投/投标/标文/文档/档分/分析/评标/知识/识库/库检/与投/标资/资料/料仓/仓库/库关/关联/联泛/泛化/化检

## README 要点


<h1 align="center">Adaptive RAG · 电商客服工作流</h1>

<p align="center"><strong>针对基于 FAQ 的传统客服系统长尾问题命中率极低，人工介入成本高的问题和常规 RAG 多跳推理能力差，幻觉问题严重的痛点设计并实现了基于 Adaptive-RAG 的多智能体电商客服系统。</strong></p>
<p align="center">FastAPI × LangGraph × 混合检索 · API、流式对话与 ChatGPT 风格 Web 工作台</p>

<p align="center">
  <a href="https://github.com/JEen-wang/Adaptive-rag/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/JEen-wang/Adaptive-rag/actions/workflows/ci.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-22c55e"></a>
  <img alt="Python 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white">
  <img alt="React and TypeScript" src="https://img.shields.io/badge/Web-React%20%2B%20TypeScript-149eca?logo=react&logoColor=white">

---
## 📷 项目快照
<p align="center">
  <img src="docs/assets/frontend-snapshot.webp" alt="Adaptive RAG Web 工作台：多条件退货提问，回答附带三条政策来源引用" width="900">
</p>

<p align="center"><sub>Web 工作台：多条件退货提问，回答附带 <code>return_policy</code> 与 <code>return_electronics</code> 三条来源引用</sub></p>

<a id="why"></a>

## 🎯 和玩具 RAG 项目的区别

跑通一次问答只需要几十行代码，真实客服的差距从第二个问题开始出现：

| 维度 | 玩具版通常怎么做 | 本项目的做法 | 关键实现 |
|:---|:---|:---|:---|
| **路由** | 所有问题都走向量检索 | 五路分流，问候不检索，越权直接拒答 | [策略路由](app/retrieval/adaptive.py) |
| **召回** | 单路向量 top-k | BM25 + 稠密向量 + RRF 融合 + Cross-Encoder 精排 | [混合检索](app/retrieval/hybrid.py) |
| **多跳** | 一次检索定结果 | 改写与补检，最多 3 跳 | [Self-RAG](app/retrieval/self_rag.py) |
| **写操作** | 模型直接调用工具 | 参数校验、权限、待确认、幂等与审计 | [工具与权限](app/tools/) |
| **幻觉** | 生成后直接返回 | 引用绑定、忠实度检查、自纠错、证据不足拒答 | [忠实度](app/agents/nodes/faithfulness.py) |
| **依赖故障** | 任一依赖不可用即失败 | 分层降级，`/capabilities` 报告实际后端 | [容器装配](app/services/container.py) |
| **上下文** | 历史全量拼进 Prompt | 128k 预算与三级压缩 | [记忆](app/memory/) |
| **评测** | 手动试几句 | 3 套离线集与可复现的口径 | [评测](eval/MEASURED.md) |
| **工程化** | 本地脚本跑通即完成 | 双版本 CI 门禁、三档部署、健康检查与指标 | [CI](.github/workflows/ci.yml) · [部署](docs/11-deployment.md) |
| **边界** | 默认宣称可用 | 明确列出未完成项 | [使用边界](#limitations) |

前四行决定答得对不对，中间三行决定故障时能不能退，最后三行决定别人能不能接手和验证。

> [!TIP]
> 每个回答都带 `strategy`、`citations` 与 `trace_id`，降级后状态可查询，指标与复现命令都在仓库里；尚未完成的部分见[使用边界](#limitations)。

<a id="overview"></a>

## ✨ 一眼看懂

> **Adaptive RAG** 的核心决策是：这个问题需要直接回答、检索一条证据、交叉核对多条证据、调用业务工具，还是拒绝处理？

电商客服里的问题跨度很大。「你好」无需查知识库；退货政策需要可靠出处；「定制商品超过七天但有质量问题」要同时判断定制、时效与质量例外；取消订单则必须检查订单状态、权限与确认。项目用明确的路由策略处理这些差异，避免把所有输入都塞进同一条向量检索链路。

| 能力 | 你能看到什么 | 关键实现 |
|:---|:---|:---|
| **按复杂度路由** | 每次回答带有 `strategy`，便于追踪实际路径 | [Graph 与节点](app/agents/graph.py) · [策略枚举](app/core/enums.py) |
| **有出处的检索** | BM25、稠密向量、RRF 融合与精排；回答可带 `citations` | [检索模块](app/retrieval/) |
| **多跳与自纠错** | 复合问题拆分检索，答案经过忠实度检查 | [智能体节点](app/agents/nodes/) |
| **人工确认** | 高风险写操作先返回 `pending_action`，确认后才执行 | [工具与权限](app/tools/) |
| **Web 对话工作台** | 流式显示、引用、本地会话搜索、深色模式与确认卡片 | [前端](frontend/) |
| **可测可观测** | 离线评测、回归测试、结构化日志与 Prometheus 指标 | [评测](eval/) · [可观测性](app/observability/) |

### 五条处理路径

| 策略 | 适合的问题 | 处理方式 |
|:---:|:---|:---|
| `DIRECT` | 问候、闲聊 | 直接生成，不做知识检索 |
| `SINGLE` | 单一政策问题 | 一轮混合检索与精排 |
| `MULTI` | 多条件、跨条款问题 | 查询改写、多路检索与自纠错 |
| `AGENT` | 查询订单、物流或发起业务操作 | 规划后调用受权限约束的工具 |
| `REFUSE` | 越权、注入或证据不足 | 拒答或引导人工处理 |

> [!TIP]
> 第一次了解项目，可以先看[架构图](#architecture)，再按[快速开始](#quickstart)提问。想看每条路径怎样落到代码，读[智能体与工具](docs/05-agents-and-tools.md)。

<a id="resume"></a>

## 📝 简历写法

> **📖 项目深挖 / 面试拷打**：写完简历先读 [《简历项目拷打：34 个高频追问与真实回答》](docs/project-deep-dive.md)。
> 每题按「新手答 → 高手答 → 追问 → 差距在哪」组织，覆盖路由、检索、工具权限、记忆、降级、指标口径，每个回答都能落到具体代码和 `eval/MEASURED.md` 的数字上；文末附三分钟自述、答题框架与「绝对不能说的 6 句话」。

**基于 Adaptive-RAG 的电商客服**

**项目概述：** 针对基于 FAQ 的传统客服系统长尾问题命中率极低，人工介入成本高的问题和常规 RAG 多跳推理能力差，幻觉问题严重的痛点设计并实现了基于 Adaptive-RAG 的多智能体电商客服系统。

- **架构设计：** 基于 LangGraph 搭建核心状态机，规划器与执行器，统一接入 15 个核心工具，实现流式输出与指数退避+抖动重试；解析意图识别，采用 Prompt-template+DeepSeek v3 构建意图路由节点并通过 LLM 自主决策分解子任务并调用工具，自建 100 条测试 query 测试意图识别准确率达到 97%。

- **检索阶段：** FAQ、退货策略、配送说明等文档进行预处理、切分、向量化索引。基于 Adaptive-RAG 实现科学感知的逻辑路由，动态调度检索策略，并通过问题改写和混合检索，解决多跳问题。

- **检索优化：** 基于 Self-RAG 构建多轮检索策略，并利用 RRF 算法对多源异构检索结果进行融合与去重，随后调用 Cohere 模型进行重排序。

  **Precision 58%→85%，Recall 63%→91%，Faithfulness 54%→88%，幻觉率下降 62%。**

- **上下文压缩与记忆管理：** 针对长会话导致的 Token 冗余及成本问题，开发 128k Token 预算管理模块（滑动窗口 + 动态摘要）；实现 3 层压缩流水线，在上下文利用率在 50%~70% 时自动收紧工具结果体积，>85% 时触发 auto-compact，达到从轻量级截断到全量摘要逐级递进的渐进式压缩。

- **Skill + MCP 的可插拔能力体系：** 支持按需加载退货处理、订单跟踪、商品推荐等标准化技能流程，并将本地工具与远程 MCP 工具统一为 Function Calling 接口。

- **兜底与护栏机制：** 设计任务分解和工具执行层双向引入 Fallback 机制；部署查询边界、幻觉检测与自纠错重试机制，将幻觉率控制在 4% 以下。

> **仓库实现说明：** 上述文字按简历原文展示。当前代码未接入 Cohere API，实际使用轻量级 `BAAI/bge-small-zh-v1.5` 做向量检索、本地 `BAAI/bge-reranker-base` 做精排；所列简历指标与仓库的[实测报告](eval/MEASURED.md)口径不同。Cohere Rerank 试用 API 密钥有免费限额，正式 API 使用按量收费，详见 [Cohere 定价说明](https://cohere.com/pricing)。

<a id="quickstart"></a>

## 🚀 快速开始

### 🐳 Docker 部署

需要 Docker Desktop，并确保 Docker Desktop 使用 WSL 2 后端。以下命令均在项目根目录执行。

#### 1. 默认演示

适合快速体验，使用 SQLite、BM25 和内存缓存 / 向量库，不需要 PostgreSQL、Redis、Qdrant 或外部 API 密钥。

```powershell
docker compose up --build -d
```

#### 2. 单机生产

使用 PostgreSQL、Redis 和单个 API 实例。先设置数据库密码：

```powershell
$env:POSTGRES_PASSWORD="your-password"
docker compose -f docker-compose.single.yml up --build -d
```

#### 3. 多实例生产

使用 PostgreSQL、Redis、Qdrant、两个 API 实例和 Nginx 负载均衡：

```powershell
$env:POSTGRES_PASSWORD="your-password"
docker compose -f docker-compose.multi.yml up --build -d
```

单机和多实例模式建议配置 `DEEPSEEK_API_KEY` 以启用生成式回答。启用本地 Embedding / Cross-Encoder 时，首次构建和启动可能下载模型，需要预留较大的磁盘和内存。

启动后访问 **http://127.0.0.1:8000**；API 文档见 **http://127.0.0.1:8000/docs**；健康检查见 **http://127.0.0.1:8000/api/v1/health**。

查看日志或停止服务：

```powershell
docker compose logs -f api
docker compose down
```

单机和多实例模式使用对应的 `-f` 参数执行 `logs` 和 `down`。没有 `DEEPSEEK_API_KEY` 时，系统使用离线证据回答；Redis、Qdrant、Embedding 或 Cross-Encoder 不可用时，会按代码中的降级策略继续运行。

不使用 Docker 时，需要 **Python 3.11+**；Web 开发另需满足[前端 Node.js 要求](frontend/README.md)。

### 1. 安装并启动 API

```bash
git clone https://github.com/JEen-wang/Adaptive-rag.git
cd Adaptive-rag
python3 -m venv
...（截断，原文见链接）

## 核心代码片段（来源：README.md）
```python


<h1 align="center">Adaptive RAG · 电商客服工作流</h1>

<p align="center"><strong>针对基于 FAQ 的传统客服系统长尾问题命中率极低，人工介入成本高的问题和常规 RAG 多跳推理能力差，幻觉问题严重的痛点设计并实现了基于 Adaptive-RAG 的多智能体电商客服系统。</strong></p>
<p align="center">FastAPI × LangGraph × 混合检索 · API、流式对话与 ChatGPT 风格 Web 工作台</p>

<p align="center">
  <a href="https://github.com/JEen-wang/Adaptive-rag/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/JEen-wang/Adaptive-rag/actions/workflows/ci.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-22c55e"></a>
  <img alt="Python 3.11+" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white">
  <img alt="React and TypeScript" src="https://img.shields.io/badge/Web-React%20%2B%20TypeScript-149eca?logo=react&logoColor=white">

---
## 📷 项目快照
<p align="center">
  <img src="docs/assets/frontend-snapshot.webp" alt="Adaptive RAG Web 工作台：多条件退货提问，回答附带三条政策来源引用" width="900">
</p>

<p align="center"><sub>Web 工作台：多条件退货提问，回答附带 <code>return_policy</code> 与 <code>return_electronics</code> 三条来源引用</sub></p>

<a id="why"></a>

## 🎯 和玩具 RAG 项目的区别

跑通一次问答只需要几十行代码，真实客服的差距从第二个问题开始出现：

| 维度 | 玩具版通常怎么做 | 本项目的做法 | 关键实现 |
|:---|:---|:---|:---|
| **路由** | 所有问题都走向量检索 | 五路分流，问候不检索，越权直接拒答 | [策略路由](app/retrieval/adaptive.py) |
| **召回** | 单路向量 top-k | BM25 + 稠密向量 + RRF 融合 + Cross-Encoder 精排 | [混合检索](app/retrieval/hybrid.py) |
| **多跳** | 一次检索定结果 | 改写与补检，最多 3 跳 | [Self-RAG](app/retrieval/self_rag.py) |
| **写操作** | 模型直接调用工具 | 参数校验、权限、待确认、幂等与审计 | [工具与权限](app/tools/) |
| **幻觉** | 生成后直接返回 | 引用绑定、忠实度检查、自纠错、证据不足拒答 | [忠实度](app/agents/nodes/faithfulness.py) |
| **依赖故障** | 任一依赖不可用即失败 | 分层降级，`/capabilities` 报告实际后端 | [容器装配](app/services/container.py) |
| **上下文** | 历史全量拼进 Prompt | 128k 预算与三级压缩 | [记忆](app/memory/) |
| **评测** | 手动试几句 | 3 套离线集与可复现的口径 | [评测](eval/MEASURED.md) |
| **工程化** | 本地脚本跑通即完成 | 双版本 CI 门禁、三档部署、健康检查与指标 | [CI](.github/workflows/ci.yml) · [部署](docs/11-deployment.md) |
| **边界** | 默认宣称可用 | 明确列出未完成项 | [使用边界](#limitations) |

前四行决定答得对不对，中间三行决定故障时能不能退，最后三行决定别人能不能接手和验证。

> [!TIP]
> 每个回答都带 `strategy`、`citations` 与 `trace_id`，降级后状态可查询，指标与复现命令都在仓库里；尚未完成的部分见[使用边界](#limitations)。

<a id="overview"></a>

## ✨ 一眼看懂

> **Adaptive RAG** 的核心决策是：这个问题需要直接回答、检索一条证据、交叉核对多条证据、调用业务工具，还是拒绝处理？

电商客服里的问题跨度很大。「你好」无需查知识库；退货政策需要可靠出处；「定制商品超过七天但有质量问题」要同时判断定制、时效与质量例外；取消订单则必须检查订单状态、权限与确认。项目用明确的路由策略处理这些差异，避免把所有输入都塞进同一条向量检索链路。

| 能力 | 你能看到什么 | 关键实现 |
|:---|:---|:---|
| **按复杂度路由** | 每次回答带有 `strategy`，便于追踪实际路径 | [Graph 与节点](app/agents/graph.py) · [策略枚举](app/core/enums.py) |
| **有出处的检索** | BM25、稠密向量、RRF 融合与精排；回答可带 `citations` | [检索模块](app/retrieval/) |
| **多跳与自纠错** | 复合问题拆分检索，答案经过忠实度检查 | [智能体节点](app/agents/nodes/) |
| **人工确认** | 高风险写操作先返回 `pending_action`，确认后才执行 | [工具与权限](app/tools/) |
| **Web 对话工作台** | 流式显示、引用、本地会话搜索、深色模式与确认卡片 | [前端](frontend/) |
| **可测可观测** | 离线评测、回归测试、结构化日志与 Prometheus 指标 | [评测](eval/) · [可观测性](app/observability/) |

### 五条处理路径

| 策略 | 适合的问题 | 处理方式 |
|:---:|:---|:---|
| `DIRECT` | 问候、闲聊 | 直接生成，不做知识检索 |
| `SINGLE` | 单一政策问题 | 一轮混合检索与精排 |
| `MULTI` | 多条件、跨条款问题 | 查询改写、多路检索与自纠错 |
| `AGENT` | 查询订单、物流或发起业务操作 | 规划后调用受权限约束的工具 |
| `REFUSE` | 越权、注入或证据不足 | 拒答或引导人工处理 |

> [!TIP]
> 第一次了解项目，可以先看[架构图](#architecture)，再按[快速开始](#quickstart)提问。想看每条路径怎样落到代码，读[智能体与工具](docs/05-agents-and-tools.md)。

<a id="resume"></a>

## 📝 简历写法

> **📖 项目深挖 / 面试拷打**：写完简历先读 [《简历项目拷打：34 个高频追问与真实回答》](docs/project-deep-dive.md)。
> 每题按「新手答 → 高手答 → 追问 → 差距在哪」组织，覆盖路由、检索、工具权限、记忆、降级、指标口径，每个回答都能落到具体代码和 `eval/MEASURED.md` 的数字上；文末附三分钟自述、答题框架与「绝对不能说的 6 句话」。

**基于 Adaptive-RAG 的电商客服**

**项目概述：** 针对基于 FAQ 的传统客服系统长尾问题命中率极低，人工介入成本高的问题和常规 RAG 多跳推理能力差，幻觉问题严重的痛点设计并实现了基于 Adaptive-RAG 的多智能体电商客服系统。

- **架构设计：** 基于 LangGraph 搭建核心状态机，规划器与执行器，统一接入 15 个核心工具，实现流式输出与指数退避+抖动重试；解析意图识别，采用 Prompt-template+DeepSeek v3 构建意图路由节点并通过 LLM 自主决策分解子任务并调用工具，自建 100 条测试 query 测试意图识别准确率达到 97%。

- **检索阶段：** FAQ、退货策略、配送说明等文档进行预处理、切分、向量化索引。基于 Adaptive-RAG 实现科学感知的逻辑路由，动态调度检索策略，并通
...（截断，原文见链接）
```
