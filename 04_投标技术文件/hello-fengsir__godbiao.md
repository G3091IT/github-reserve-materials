---
title: hello-fengsir/godbiao
source: GitHub（hello-fengsir/godbiao）
topic: 04_投标技术文件
date: 2026-06-14
harvest_date: 2026-11-16
url: https://github.com/hello-fengsir/godbiao
tags: [公开学习库, 投标实务, AI投标, GitHub仓库]
---

# hello-fengsir/godbiao

- **仓库名**：hello-fengsir/godbiao
- **原文链接**：https://github.com/hello-fengsir/godbiao
- **Star 数**：31（取自 GitHub 搜索 API，待核实）
- **最近更新时间**：2026-06-14T01:40:10Z
- **许可证**：MIT
- **语言**：HTML
- **质量分 / 适配分 / 混合分**：72.3 / 60.0 / 66.8
- **结论**：ADOPT
- **标记**：无
- **领域适配**：人工核验相关(强制收录)

## 用途摘要
AI 智能标书比对系统 — 上传投标文件+招标要求，逐条核查，防止标书出错

## 适配理由
✓ 命中任务词：ai/投标/文件；△ 未命中：标技/技术/术文/件生/成与/与编/编写/写工

## README 要点
# 🦸 神奇阿标 (God Biao)

> AI 智能招投标工具 — 评标：上传标书自动逐条核查 · 制标：参数化管理一键导出

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-v2.1-3b82f6.svg)](https://github.com/hello-fengsir/godbiao/releases/tag/v2.1)

---

## ✨ v2.1 更新内容 🆕

| 模块 | 功能 |
|---|---|
| 📱 **手机端适配** | 全面响应式布局 — 顶部汉堡菜单、侧边栏抽屉、看板自适应、表格横向滚动 |
| 🔧 **进度条修复** | 评标三阶段进度实时显示（比对 → 格式 → 关键信息） |
| 🔧 **数据解析修复** | 修复 items/results 字段不匹配导致评标结果为空的问题 |
| 🔧 **模型选择修复** | 修复 API Key 添加模型时无法选择模型服务商的问题 |
| 🔧 **测试连接修复** | 修复 test_key 函数解包错误 |
| 🎨 **UI 优化** | Modal 弹窗手机端宽度自适应、KPI 卡片字体缩小、表格优化 |

## ✨ v2.0 新增功能

| 模块 | 功能 |
|---|---|
| 🏗️ **制标工具** | 技术参数管理系统 — 类别 → 产品线 → 参数 三级联动 |
| 📊 **Excel 批量导入** | 支持 `.xlsx` 拖拽上传，按产品线批量导入技术参数 |
| 📥 **Word 一键导出** | 按 [分类] 自动分组，生成规范技术参数表（2 列：序号 / 名称） |
| 🏷️ **型号管理** | 每个产品线支持多型号管理（名称 + 规格描述） |
| 🗂️ **分类管理** | 自定义类别，级联管理产品线与参数 |
| 🔧 **代码重构** | 三文件架构拆分（`app.py` 评标 + `bid_api.py` 制标 + `models.py` 数据层），零硬编码 |

---

## ✨ 原有功能 (v1.x)

- 📄 **多格式解析** — PDF / Word / 图片(OCR) / 纯文本全支持
- 🤖 **多模型对比** — 支持 DeepSeek / OpenAI / 通义千问等 10+ 大模型
- 📊 **逐项核查** — AI 自动提取招标要求，逐条比对投标响应（三路并行分析）
- 📝 **格式评估** — 检测标书格式问题（字体、排版、缺失章节等）
- 🔑 **关键信息提取** — 自动抓取金额、货期、资质等商务关键项
- 🔒 **零密钥存储** — API Key 仅存浏览器 localStorage，服务器不落盘
- 🐳 **一键部署** — Docker Compose 开箱即用

---

## 🚀 快速开始

### 前置要求

- Docker & Docker Compose
- 任意兼容 OpenAI API 的大模型 Key（如 DeepSeek / OpenAI / 通义千问）

### 部署

```bash
git clone https://github.com/hello-fengsir/godbiao.git
cd godbiao

# 可选：创建 .env 文件配置默认 API Key
cp .env.example .env
# 编辑 .env 填入你的 Key（也可不填，在前端页面设置）

docker compose up -d
```

打开浏览器访问 `http://localhost:8880`

### 两大工具

| 工具 | 路径 | 用途 |
|---|---|---|
| 📋 **评标** | `/review` | 上传投标文件 + 招标要求 → AI 逐项核查 |
| 🏗️ **制标** | `/bidding` | 产品线 → 参数管理 → 一键导出 Word 技术参数表 |

### 评标流程

1. 首页点击 **⚙️ 模型设置** → 选择提供商 → 粘贴 API Key → 保存
2. 选择评标模式（合并/分离）
3. 上传投标文件 + 填写招标要求
4. 预览确认 → 开始 AI 比对
5. 查看结果：逐项满足度 + 格式评分 + 关键信息提取

### 制标流程

1. 切换到 **📋 制标** 页面
2. 选择 / 新建类别和产品线
3. 📥 导入参数（Excel 批量导入）或逐条添加
4. 编辑参数名称和竞争分析备注
5. 👁 预览 → 📥 导出 Word

📖 详细产品文档请参阅 [docs/PRODUCT.md](docs/PRODUCT.md)

---

## 📁 项目结构

```
godbiao/
├── app.py              # 主入口 + 评标路由（FastAPI）
├── bid_api.py          # 制标路由（APIRouter, /api/bid/*）
├── models.py           # 统一数据层（评标 + 制标共 5 张表）
├── config.py           # 模型预置列表 & 配置
├── llm_client.py       # LLM 调用封装（三路并行：比对/格式/关键信息）
├── parser.py           # 文件解析（PDF/Word/OCR/TXT）
├── import_products.py  # Excel → SQLite 批量导入工具
├── templates/
│   ├── index.html      # 评标首页（上传 + 历史记录，手机端适配）
│   ├── bidding.html    # 制标页面（类别→产品线→参数管理）
│   ├── review.html     # 预览页
│   └── result.html     # 结果页（逐项核查 + 关键信息）
├── static/
├── docker-compose.yml
├── Dockerfile
└── .env.example
```

## 🗃️ 数据模型

```
bid_categories (类别)
  └── bid_product_lines (产品线)
        ├── bid_parameters (技术参数, hardware/software)
        └── bid_product_models (型号)
```

所有 CRUD 通过 RESTful API 暴露，前端完全数据驱动。

---

## 🎨 截图

### 评标首页 — 上传投标文件 + 招标要求

<p align="center">
  <img src="screenshots/homepage.png" width="800" alt="评标首页">
</p>

### 制标工具 — 类别→产品线→参数管理 + 一键导出 Word

<p align="center">
  <img src="screenshots/bidding.png" width="800" alt="制标工具">
</p>

### 模型设置 — 支持 10+ 大模型

<p align="center">
  <img src="screenshots/model-settings.png" width="800" alt="模型设置">
</p>

---

## ☕ 赞赏

如果这个项目对你有帮助，欢迎请作者喝杯咖啡~

<p align="center">
  <img src="static/zanshang.jpg" width="300" alt="赞赏码">
</p>

## ⚠️ 免责声明

本项目仅供学习交流使用，禁止用于任何商业用途。使用者须自行承担因使用本项目产生的任何法律风险与责任。

## 📸 产品截图

<!-- 请将截图放入 images/ 目录 -->
| 评标系统 | 比对结果 | 制标系统 |
|---|---|---|
| ![评标系统](images/评标系统.png) | ![比对结果](images/比对结果.png) | ![制标系统](images/制标系统.png) |

## 📄 License

> 本文档由 GitHub Actions 自动通知测试更新

MIT License © [峰Sir](https://github.com/hello-fengsir)


## 核心代码片段（来源：app.py）
```html
"""
神奇阿标 (God Biao) 主应用
"""
import json
import uuid
import sqlite3
import os
import shutil
import glob
from datetime import datetime, timedelta
from io import BytesIO

from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from config import BASE_DIR, UPLOAD_DIR, DB_PATH, MODEL_PRESETS
from parser import parse_file
from llm_client import compare_bid, evaluate_format, extract_key_info, test_api_key
from models import init_all_tables, job_create, job_get, job_update, job_trim, job_cleanup_old
from bid_api import router as bid_router

# ── App 初始化 ──

app = FastAPI(title="神奇阿标 - God Biao")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
UPLOAD_DIR.mkdir(exist_ok=True)

# 挂载制标 API
app.include_router(bid_router)

# 初始化所有表
init_all_tables()

# ── 全局状态 ──

_compare_progress: dict = {}  # job_id → {phase, content_done, format_done, started_at, error}
MAX_HISTORY = 3


# ═══════════════════════════════════════════════════
# 页面路由
# ═══════════════════════════════════════════════════

@app.get("/review", response_class=HTMLResponse)
async def review_page(request: Request):
    cleanup_uploads()
    tpl = templates.env.get_template("index.html")
    return HTMLResponse(tpl.render({"request": request}))


@app.get("/")
async def root():
    return RedirectResponse(url="/review")


@app.get("/bidding", response_class=HTMLResponse)
def bidding_page(request: Request):
    tpl = templates.env.get_template("bidding.html")
    return HTMLResponse(tpl.render({"request": request}))


@app.get("/result/{job_id}", response_class=HTMLResponse)
async def result_page(request: Request, job_id: str):
    row = job_get(job_id)
    if not row:
        return HTMLResponse("<h2>任务未找到</h2>", 404)

    job = dict(row)
    result_data = {}
    if job.get("result_json"):
        try:
            result_data = json.loads(job["result_json"])
        except:
            pass

    # 提取内容比对结果
    results = result_data.get("items", result_data.get("results", []))
    total = len(results)
    full_pass = sum(1 for r in results if r.get("status") == "满足")
    partial = sum(1 for r in results if r.get("status") == "部分满足")
    failed = sum(1 for r in results if r.get("status") in ("不满足", "缺失"))
    full_pass_pct = round(full_pass / total * 100) if total else 0
    partial_pct = round(partial / total * 100) if total else 0
    failed_pct = round(failed / total * 100) if total else 0

    # 提取格式评估结果
    fmt_eval = result_data.get("format_eval", {})
    fmt_score = fmt_eval.get("score", 0)
    fmt_overall = fmt_eval.get("overall", "")
    fmt_items = fmt_eval.get("items", [])

    # 提取关键信息
    key_info = result_data.get("key_info", {})

    tpl = templates.env.get_template("result.html")
    return HTMLResponse(tpl.render({
        "request": request,
        "job": job,
        "bid_filename": job.get("bid_filename", ""),
        "model": job.get("model_used", result_data.get("model", "")),
        "tokens": job.get("tokens_used", result_data.get("tokens_used", 0)),
        "eval_mode": job.get("eval_mode", "combined"),
        "overall": result_data.get("overall", ""),
        "results": results,
        "total": total,
        "full_pass": full_pass,
        "full_pass_pct": full_pass_pct,
        "partial": partial,
        "partial_pct": partial_pct,
        "failed": failed,
        "failed_pct": failed_pct,
        "fmt_score": fmt_score,
        "fmt_overall": fmt_overall,
        "fmt_items": fmt_items,
        "key_info": key_info,
    }))


# ═══════════════════════════════════════════════════
# 评标 API
# ═══════════════════════════════════════════════════

@app.post("/upload")
async def upload(
    request: Request,
    bid_file: UploadFile = File(None),
    tech_file: UploadFile = File(Non
...（截断，原文见链接）
```
