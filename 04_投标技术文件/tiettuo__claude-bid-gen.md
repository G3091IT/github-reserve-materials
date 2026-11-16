---
title: tiettuo/claude-bid-gen
source: GitHub（tiettuo/claude-bid-gen）
topic: 04_投标技术文件
date: 2026-11-02
harvest_date: 2026-11-16
url: https://github.com/tiettuo/claude-bid-gen
tags: [公开学习库, 投标实务, AI投标, GitHub仓库]
---

# tiettuo/claude-bid-gen

- **仓库名**：tiettuo/claude-bid-gen
- **原文链接**：https://github.com/tiettuo/claude-bid-gen
- **Star 数**：9（取自 GitHub 搜索 API，待核实）
- **最近更新时间**：2026-11-02T02:37:21Z
- **许可证**：MIT
- **语言**：Python
- **质量分 / 适配分 / 混合分**：77.5 / 65.0 / 71.9
- **结论**：ADOPT
- **标记**：无
- **领域适配**：人工核验相关(强制收录)

## 用途摘要
AI 生成工程投标技术标/施工组织设计（Chinese construction tender technical proposals）。Extract→plan→write→assemble→compliance 全流程管道，Agent 通用（Claude Code / Codex / pi / hermas）。

## 适配理由
✓ 命中任务词：ai/投标/标技/技术；△ 未命中：术文/文件/件生/成与/与编/编写/写工

## README 要点
# bid-gen — 投标技术文件生成系统

[English](README.en.md)

工程类招投标的全流程施工组织设计生成管道，从原始招标 PDF/DOCX 抽取，到机器审校 + 合规检查 + 批量投标相似度防围标。

**当前形态**：脚本管道 + 智能体编排。可移植到任何支持 prompt + bash 工具调用的智能体（Claude Code / Codex / pi / hermas 等）。

---

## 目录结构

```
bid-gen/
├── README.md                    # 本文件
├── requirements.txt             # Python 依赖（必需 + 可选）
├── .env.example                 # API Key 模板
│
├── commands/
│   └── bid-gen.md               # 主提示词（693 行，Step 0-6 工作流定义）
│
├── skills/bid-gen/references/
│   └── extraction-methodology.md # v2 方法论：四阶段闭环 + 八条铁律 + 历史失败案例
│
├── scripts/                     # 26 个 Python 脚本（管道实现）
│   ├── bid_run.py               # 一键编排（Step 1-6）
│   ├── bid_status.py            # 实时进度（只读）
│   ├── bid_extract.py           # Step 1: PDF/Word/Excel 提取 + 分层视觉 OCR
│   ├── bid_vision.py            #         视觉模型（Qwen-VL / GLM-OCR）封装
│   ├── bid_fingerprint.py       #         PDF 指纹采集
│   ├── bid_skeleton_extract.py  # Step 1.5: 骨架 JSON（evaluation/outline/disqualification）
│   ├── bid_facts_extract.py     #           13 字段事实抽取
│   ├── bid_derive.py            #           Tier 2 派生
│   ├── bid_special_extract.py   #           Tier 4 特殊抽取
│   ├── bid_template_match.py    #           Tier 0 范本匹配
│   ├── bid_brain_translate.py   #           JSON → brain.md 自动翻译
│   ├── bid_plan_verify.py       # Step 2: 三铁律校验
│   ├── bid_chart_specs.py       #         图表规格派生
│   ├── bid_variants.py          # Step 2.5: 批量投标配置
│   ├── bid_writer.py            # Step 3: 章节生成（调下游模型）
│   ├── bid_expand.py            #         章节展开辅助
│   ├── bid_reviewer.py          # Step 3.5: 机器审校
│   ├── bid_assemble.py          # Step 4: DOCX 组装（最大脚本，2450 行）
│   ├── bid_charts.py            #         7 渲染器图表生成（2613 行）
│   ├── bid_charts_selftest.py   #         渲染器自检（14/14 应通过）
│   ├── bid_format_audit.py      #         格式审计
│   ├── bid_input_assemble.py    #         输入组装
│   ├── bid_compliance.py        # Step 5: 废标合规扫描
│   ├── bid_similarity.py        # Step 6: 交叉相似度（仅批量）
│   ├── bid_common.py            # 公共工具
│   └── bid_llm_client.py        # LLM 客户端封装
│
├── configs/
│   ├── bid_llm_config.json      # 6 家模型池（GLM/DeepSeek/Qwen/Kimi/MiniMax/豆包）
│   └── bid_vision_config.json   # 视觉 OCR 七类关键词触发规则
│
├── docs/
│   ├── chart_schemas.md         # 7 种图表渲染器精确 schema
│   └── bid-gen-flowchart.html   # 业务流程图（Mermaid，浏览器打开）
│
└── memory/                      # 经验沉淀（feedback 教训 + 脱敏项目案例）
    ├── feedback_bid_*.md        # 反馈教训（写代码必读）
    ├── reference_bid_*.md       # 参考资料
    └── project_*.md             # 历史项目案例（已脱敏：不含客户名/金额/编号）
```

---

## 部署到新智能体

### 1. 安装依赖

```bash
pip install -r requirements.txt
# macOS: brew install pandoc
# Ubuntu: apt-get install pandoc fonts-noto-cjk
```

### 2. 配置 API Keys

```bash
cp .env.example .env
# 编辑 .env 填入至少一家 LLM API Key（推荐 GLM_API_KEY + DASHSCOPE_API_KEY）
```

脚本默认从 `~/.env` 加载；如需自定义可设 `LLM_ENV_FILE=/path/to/.env`。

### 3. 设置 BID_GEN_HOME（可选）

```bash
export BID_GEN_HOME=/absolute/path/to/bid-gen
```

**不设也行** — 所有脚本会自动回落到 `Path(__file__).parent.parent`（即本目录），配置文件从 `configs/` 加载。

### 4. 健康检查

```bash
python $BID_GEN_HOME/scripts/bid_run.py --doctor
```

显示：Python 包是否齐全、26 个脚本是否完整、API Key 是否配置。

### 5. 跑一个真实项目

```bash
python $BID_GEN_HOME/scripts/bid_run.py /path/to/招标文件目录
```

`bid_run.py` 在投标项目目录的 `output/.bid_run.state.json` 维护 checkpoint，每步 `ok/fail/skip`。**Step 2 必须由 LLM 在对话里手工完成**（brain/plan/rules），脚本检测缺失会停下等待。

---

## 智能体集成要点

主提示词 `commands/bid-gen.md` 设计为 Claude Code 的 slash command 格式，使用 `$ARGUMENTS` 占位符接收用户输入的项目目录路径。集成到 hermas 或其他 agent 时：

1. **提示词加载**：把 `commands/bid-gen.md` 作为系统提示词的核心模块加载
2. **`$ARGUMENTS` 替换**：把 agent 接收的用户参数（投标项目目录路径）注入到 `$ARGUMENTS` 占位符
3. **`$BID_GEN_HOME` 替换**：可选 — 如果 agent 不会自动展开环境变量，可在加载提示词时把 `$BID_GEN_HOME` 替换为本目录绝对路径
4. **memory 加载**：把 `memory/` 19 个 .md 作为持久知识库（feedback 类是写代码时必须遵守的教训，project 类是真实案例参考）
5. **工具权限**：agent 需要 Bash（运行 Python 脚本）+ Read/Write/Edit（操作 brain/plan/rules .md 和章节 .md）

---

## 工作流概览（Step 0-6）

| 步骤 | 主脚本 | 输入 | 输出 |
|---|---|---|---|
| **Step 1** | `bid_extract.py` | 招标 PDF/DOCX/XLSX | `extracted/*.txt` + 视觉 OCR 段 |
| **Step 1.5** | `bid_skeleton_extract.py` | extracted/ | `evaluation_method.json` / `mandatory_outline.json` / `disqualification.json` |
| **Step 2** | （LLM 手工） | 三 JSON | `project_brain.md` / `chapter_plan.md` / `disqualification_rules.md` |
| **Step 2.4** | `bid_plan_verify.py` | brain + plan | 三铁律校验报告 |
| **Step 2.5** | `bid_variants.py` | brain | `variants.json`（批量投标配置） |
| **Step 3** | `bid_writer.py` 或 LLM | plan + brain | `output/[VXX/]0X_*.md` |
| **Step 3.5** | `bid_reviewer.py` | 章节 .md | `review.json` + 严重性分级 |
| **Step 4** | `bid_assemble.py` | 章节 .md | `*.docx` |
| **Step 5** | `bid_compliance.py` | 章节 .md + docx | `合规检查报告.md` |
| **Step 6** | `bid_similarity.py` | 多家 docx（批量） | `similarity_matrix.json` + `相似度检查报告.md` |

完整流程图见 `docs/bid-gen-flowchart.html`（Mermaid，可直接浏览器打开）。

---

## 核心原则（来自主提示词）

> **章节锚点 = 「技术标评分表」 ∪ 「施组编制大纲」（语义并集去重），不使用任何固定章节模板。**
> - **评分制项目**：评分表为主章节锚点
> - **合格制项目**：施组编制大纲为主章节锚点
> - 章节标题字面优先复制评分表/大纲原文，**禁止自造、概括**
> - 评委按评分表/大纲逐条找章节，找不到对应章节 = 扣分 / 废标

**v2 核心规则**：brain.md 第 5/6/7 节直接从 Step 1.5 三份 JSON 1:1 翻译，**禁止凭印象重写**（这是历史三个项目暴露的根因 — 详见 `skills/bid-gen/references/extraction-methodology.md`）。

---

## 维护说明

- **脚本之间通过目录共置 import**（如 `from bid_common import ...`），所以 `scripts/` 下 26 个 `.py` 必须保持在同一目录
- **新增依赖**：同步更新 `requirements.txt` 和 `scripts/bid_run.py` 的 `REQUIRED_PKGS` / `OPTIONAL_PKGS`
- **新增配置**：放入 `configs/`，脚本通过 `Path(os.environ.get("BID_GEN_HOME", str(Path(__file__).resolve().parent.parent))) / "configs" / "xxx.json"` 引用

---

## 版本来源

本仓库由早期的个人 Claude Code skill 部署整理为自包含项目：脚本、提示词、配置、记忆全部收拢在本目录，无外部硬编码路径。



## 核心代码片段（来源：CLAUDE.md）
```python
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`bid-gen-v3` generates Chinese construction-tender technical proposals (施工组织设计). It is a **script-backed pipeline orchestrated by a prompt**, not a generic proposal-writing assistant. The full operating contract lives in [commands/bid-gen.md](commands/bid-gen.md) (~37KB, Step 0–6); the agent-facing entry is [skills/bid-gen/SKILL.md](skills/bid-gen/SKILL.md). Run a real bid by pointing the orchestrator at a tender directory, not by improvising prose.

## Common commands

Run from repo root (`BID_GEN_HOME` defaults to this directory — `scripts/`'s parent — and rarely needs setting).

```bash
# Step −1: ingest a raw tender .zip → normalized tender dir (GBK filenames, recursive
# container unwrap for .XZZ/.GKZJ/.ZBWJ, canonical 招标文件.pdf promoted to the root)
python3 scripts/bid_ingest_zip.py "<项目>.zip" --out-dir "<parent dir>"

# Static-TOC page backfill (Word→PDF → PyMuPDF locate headings → fill @@TOCPGn@@).
# Never write w:updateFields into a generated DOCX — Word then always shows a modal
# "fields may refer to other files" alert that no preference can disable.
python3 scripts/bid_toc_fill.py "<tender_dir>"

# Health check (packages, scripts present, API keys). Run after any dep/env change.
python3 scripts/bid_run.py --doctor

# Initialize LLM config template if configs/bid_llm_config.json is missing
python3 scripts/bid_llm_client.py --init

# Full pipeline (auto-detects single vs. batch mode by presence of extracted/variants.json)
python3 scripts/bid_run.py "<tender_dir>"
python3 scripts/bid_run.py "<tender_dir>" --resume      # continue from last failed step
python3 scripts/bid_run.py "<tender_dir>" --from write --to assemble
python3 scripts/bid_run.py "<tender_dir>" --dry-run
python3 scripts/bid_run.py "<tender_dir>" --force-continue   # ignore review/similarity gates

# Loop orchestration: retry loop + budget circuit-breaker + failure ledger + Feishu alert
python3 scripts/bid_loop.py "<tender_dir>" [--max-cycles 3]

# Read-only progress / blockers
python3 scripts/bid_status.py "<tender_dir>"

# Chart renderer self-check (should be 14/14)
python3 scripts/bid_charts_selftest.py
```

**Tests** — plain pytest from repo root; no `pyproject.toml`/`pytest.ini`. [tests/conftest.py](tests/conftest.py) prepends `scripts/` to `sys.path` so tests `import bid_*` directly.

```bash
pytest -q
pytest tests/test_bid_loop.py -q                          # one file
pytest tests/test_bid_loop.py::test_name -q                # one test
```

After editing pipeline scripts, run the most relevant test file **plus** `bid_run.py --doctor`.

**System deps:** `pip install -r requirements.txt`; `pandoc` is a hard binary requirement for Step 4 (DOCX assembly) — `brew install pandoc` / `apt-get install pandoc`. Chinese fonts (PingFang/Noto CJK) needed for matplotlib chart rendering. Optional packages (simhash, jieba, PyMuPDF) degrade gracefully when missing.

## Architecture

### Pipeline and its two orchestration layers

The pipeline is the ordered `STEPS` list in [scripts/bid_run.py](scripts/bid_run.py) — **that list is the source of truth**, not the README (which lags behind). Current order (single-shot per tender dir):

```
extract → template → facts → derive → skeleton → special → input_assemble →
fingerprint → variants → plan_variants → chart_specs → write → review →
coherence_pass → assemble → verify → compliance → similarity → summary
```

> **连贯性主线注入(散装→茅台)**:`coherence_pass` 是可选工序(受 `configs/bid_coherence.json enabled` 开关控制,默认 off)。启用后还会触发工序A(`deployment_synthesize` 在 Step2 链 + plan 派生 `chapter_narrative.json` + writer Block1 难点精准注入)和工序B(post-writer `bid_chapter_intro` 重写引言回指主线)。详见 [memory/feedback_bid_coherence.md](memory/feedback_bid_coherence.md)。

Two layers coordinate this:

- **`bid_run.py`** — single-shot orchestrator. Writes per-step status (`ok`/`fail`/`skip`/`running`/`interrupted`) to `output/.bid_run.s
...（截断，原文见链接）
```
