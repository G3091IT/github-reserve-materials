# run-llama/liteparse

- **仓库名**：run-llama/liteparse
- **原文链接**：https://github.com/run-llama/liteparse
- **Star 数**：12987（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-11-04T17:08:17Z
- **许可证**：Apache-2.0
- **语言**：Rust
- **质量分 / 适配分 / 混合分**：96.9 / 50.0 / 75.8
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:pdf/document parse/extract

## 用途摘要
A fast, helpful, and open-source document parser

## 适配理由
✓ 命中任务词：pdf；△ 未命中：word/excel/比对/对与/与文/文档/档转/转换/换的/的库

## README 要点
# LiteParse

[![CI](https://github.com/run-llama/liteparse/actions/workflows/ci.yml/badge.svg)](https://github.com/run-llama/liteparse/actions/workflows/ci.yml)
|
[![Crates.io version](https://img.shields.io/crates/v/liteparse.svg)](https://crates.io/crates/liteparse)
|
[![npm version](https://img.shields.io/npm/v/@llamaindex/liteparse.svg)](https://www.npmjs.com/package/@llamaindex/liteparse)
|
[![wasm version](https://img.shields.io/npm/v/@llamaindex/liteparse-wasm.svg)](https://www.npmjs.com/package/@llamaindex/liteparse-wasm)
|
[![PyPI version](https://img.shields.io/pypi/v/liteparse.svg)](https://pypi.org/project/liteparse/)
|
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
|
[Docs](https://developers.llamaindex.ai/liteparse/)

English | [简体中文](README.zh-CN.md)

<img src="https://github.com/user-attachments/assets/07ba6a82-6bb1-4dea-b0ef-cad7df7d1622" alt="out" width="600">

> Looking for LiteParse V1? Follow this link to [the old code](https://github.com/run-llama/liteparse/tree/logan/liteparse-v1)

LiteParse is a standalone OSS PDF parsing tool focused exclusively on **fast and light** parsing. It provides high-quality spatial text parsing with bounding boxes, without proprietary LLM features or cloud dependencies. Everything runs locally on your machine.

**Hitting the limits of local parsing?**
For complex documents (dense tables, multi-column layouts, charts, handwritten text, or
scanned PDFs), you'll get significantly better results with [LlamaParse](https://developers.llamaindex.ai/python/cloud/llamaparse/?utm_source=github&utm_medium=liteparse),
our cloud-based document parser built for production document pipelines. LlamaParse handles the
hard stuff so your models see clean, structured data and markdown.

>  [Sign up for LlamaParse free](https://cloud.llamaindex.ai?utm_source=github&utm_medium=liteparse)

## Overview

- **Fast Text Parsing**: Spatial text parsing using PDFium, ~2-5ms per page
- **Flexible OCR System**:
  - **Built-in**: Tesseract (zero setup, bundled with the library)
  - **HTTP Servers**: Plug in any OCR server (EasyOCR, PaddleOCR, custom)
  - **Standard API**: Simple, well-defined OCR API specification
- **Complexity Detection**: Cheaply check whether a document needs OCR or heavier parsing — route, reject, or estimate cost before a full parse
- **Screenshot Generation**: Generate high-quality page screenshots for LLM agents
- **Multiple Output Formats**: Markdown, JSON, and Text
- **Markdown Output**: Structured Markdown with headings, tables, lists, images, and links — great for feeding LLMs and RAG pipelines
- **Bounding Boxes**: Precise text positioning information
- **Multi-language**: Use from Rust, Node.js/TypeScript, Python, or the browser (WASM)
- **Worker Pool Mode** (Python & Node.js): Parse in persistent worker processes for true parallelism (PDFium otherwise serializes concurrent parses) and hard per-parse timeouts — rogue documents are killed, identified by name, and never stall the pipeline
- **Multi-platform**: Linux, macOS (Intel/ARM), Windows

```mermaid
flowchart LR
      subgraph Input["Input Formats"]
          direction TB
          PDF["PDF"]
          DOCX["DOCX"]
          XLSX["XLSX"]
          PPTX["PPTX"]
          IMG["Images"]
      end

      subgraph Core["Rust Core"]
          direction TB
          CONV["Format Conversion\nLibreOffice / Rust image + resvg + usvg crates"]
          EXTRACT["Text Extraction\nPDFium C library"]
          OCR["Selective OCR\nTesseract / HTTP / Custom"]
          MERGE["OCR Merge\nNative text + OCR results"]
          PROJ["Grid Projection\nSpatial layout reconstruction"]
          CONV --> EXTRACT
          EXTRACT --> OCR --> MERGE --> PROJ
          EXTRACT --> MERGE
      end

      subgraph Output[" Output "]
          direction TB
          JSON["Structured JSON\ntext + bounding boxes"]
          TEXT["Plain Text\nlayout-preserved"]
          SCREEN["Screenshots\nPNG rendering"]
      end

      subgraph Bindings["Language Bindings"]
          direction TB
          NAPI["Node.js / TypeScript\nnapi-rs"]
          PYO3["Python\nPyO3"]
          WASM["Browser / WASM\nwasm-bindgen"]
          CLI["CLI\ncargo / npm / pip"]
          NAPI ~~~ PYO3 ~~~ WASM ~~~ CLI
      end

      PDF --> EXTRACT
      DOCX & XLSX & PPTX & IMG --> CONV
      PROJ --> JSON & TEXT & SCREEN
      JSON & TEXT & SCREEN --> Bindings

      style Input fill:#F5F5F5,color:#000000,stroke:#37D7FA,stroke-width:2px
      style Core fill:#F5F5F5,color:#000000,stroke:#3E18F9,stroke-width:2px
      style Output fill:#F5F5F5,color:#000000,stroke:#FF8705,stroke-width:2px
      style Bindings fill:#F5F5F5,color:#000000,stroke:#FF8DF2,stroke-width:2px

      style PDF fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px
      style DOCX fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px
      style XLSX fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px
      style PPTX fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px
      style IMG fill:#96E7F9,color:#000000,stroke:#37D7FA,stroke-width:1px

      style CONV fill:#92AEFF,color:#000000,stroke:#4B72FE,stroke-width:1px
      style EXTRACT fill:#92AEFF,color:#000000,stroke:#4B72FE,stroke-width:1px
      style OCR fill:#92AEFF,color:#000000,stroke:#4B72FE,stroke-width:1px
      style MERGE fill:#92AEFF,color:#000000,stroke:#4B72FE,stroke-width:1px
      style PROJ fill:#4B72FE,color:#FFFFFF,stroke:#3E18F9,stroke-width:2px

      style JSON fill:#FFBD74,color:#000000,stroke:#FF8705,stroke-width:1px
      style TEXT fill:#FFBD74,color:#000000,stroke:#FF8705,stroke-width:1px
      style SCREEN fill:#FFBD74,color:#000000,stroke:#FF8705,stroke-width:1px

      style NAPI fill:#FFBFF8,color:#000000,stroke:#FF8DF2,stroke-width:1px
      style PYO3 fill:#FFBFF8,color:#000000,stroke:#FF8DF2,stroke-width:1px
      style WASM fill:#FFBFF8,color:#000000,stroke:#FF8DF2,stroke-width:1px
      sty
...（截断，原文见链接）

## 核心代码片段（来源：run_benchmarks.sh）
```rust
#!/usr/bin/env bash
#
# run_benchmarks.sh — reproduce the LiteParse markdown benchmark sweep.
#
# Runs LiteParse (and, by default, the model-free competitors) across the three
# tracked benchmarks — olmOCR-bench, opendataloader-bench, ParseBench — and prints
# a comparison table per benchmark. See LAUNCH_BENCHMARKS.md for the published run.
#
# Usage:
#   ./run_benchmarks.sh [options]
#
# Options:
#   --liteparse-only        Only run LiteParse (skip all competitor tools).
#   --competitors-only      Only run the model-free competitors (keep existing LiteParse outputs).
#   --benches=LIST          Comma-separated subset of: olmocr,opendataloader,parsebench
#                           (default: all three).
#   --skip-build            Don't rebuild the lit binary / Python binding.
#   --out=DIR               Where to write logs + the summary (default: bench_results/latest).
#   --ocr=MODE              LiteParse OCR mode: none (default), tesseract, or paddle.
#                           paddle = the HTTP PaddleOCR server (ocr/paddleocr, port 8829;
#                           override with LITEPARSE_PADDLE_OCR_URL). OCR modes run with
#                           num_workers=4 and low harness concurrency — OCR is resource-hungry.
#                           Outputs land under mode-suffixed names (liteparse_tesseract, …) so
#                           all modes coexist and show up together in SUMMARY.md.
#   -h, --help              Show this help.
#
# Competitors (model-free, commercial): markitdown, opendataloader, pdf_inspector.
#   - opendataloader needs Java 11+ (the script auto-detects Homebrew openjdk@11/openjdk).
#   - pdf_inspector needs the `pdf2md` binary (cargo install pdf-inspector).
#   - nutrient is commercial and is NOT re-run here; see LAUNCH_BENCHMARKS.md for its
#     preserved opendataloader-bench numbers.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

LITEPARSE_ONLY=0
COMPETITORS_ONLY=0
SKIP_BUILD=0
BENCHES="olmocr opendataloader parsebench"
OUT="$ROOT/bench_results/latest"
OCR_MODE="none"

for arg in "$@"; do
  case "$arg" in
    --liteparse-only) LITEPARSE_ONLY=1 ;;
    --competitors-only) COMPETITORS_ONLY=1 ;;
    --skip-build)     SKIP_BUILD=1 ;;
    --benches=*)      BENCHES="${arg#*=}"; BENCHES="${BENCHES//,/ }" ;;
    --out=*)          OUT="${arg#*=}" ;;
    --ocr=*)          OCR_MODE="${arg#*=}" ;;
    -h|--help)        sed -n '2,30p' "${BASH_SOURCE[0]}"; exit 0 ;;
    *) echo "Unknown option: $arg" >&2; exit 2 ;;
  esac
done

mkdir -p "$OUT"
PY="$ROOT/.venv/bin/python"

# --- OCR mode → per-harness LiteParse engine/pipeline names ---------------
case "$OCR_MODE" in
  none)
    OLM_LP="liteparse"; OLM_LP_NAME="liteparse"; ODL_LP="liteparse"; PB_LP="liteparse_markdown"; PB_CONC=6 ;;
  tesseract)
    OLM_LP="liteparse:ocr_engine=tesseract:num_workers=4:name=liteparse_tesseract"; OLM_LP_NAME="liteparse_tesseract"
    ODL_LP="liteparse-tesseract"; PB_LP="liteparse_markdown_tesseract"; PB_CONC=3 ;;
  paddle)
    OLM_LP="liteparse:ocr_engine=paddle:num_workers=4:name=liteparse_paddle"; OLM_LP_NAME="liteparse_paddle"
    ODL_LP="liteparse-paddle"; PB_LP="liteparse_markdown_paddle"; PB_CONC=3
    PURL="${LITEPARSE_PADDLE_OCR_URL:-http://localhost:8829/ocr}"
    curl -s -m 5 -o /dev/null "${PURL%/ocr}/" || echo "WARNING: no PaddleOCR server answering at $PURL (start: cd ocr/paddleocr && uv run server.py)" >&2 ;;
  *) echo "Unknown --ocr mode: $OCR_MODE (none|tesseract|paddle)" >&2; exit 2 ;;
esac
TIMING="$OUT/timings.txt"
stamp() { echo "$(date +%s) $*" >> "$TIMING"; }

# --- Java 11+ detection (needed by the opendataloader competitor) -------------
JAVA11_BIN=""
for cand in /opt/homebrew/opt/openjdk@11/bin /opt/homebrew/opt/openjdk/bin /opt/homebrew/opt/openjdk@25/bin; do
  if [ -x "$cand/java" ]; then JAVA11_BIN="$cand"; break; fi
done
if [ -n "$JAVA11_BIN" ]; then export PATH="$JAVA11_BIN:$PATH"; fi

run_engines() {  # echoes the engine list for a benchmark, honoring --litepar
...（截断，原文见链接）
```
