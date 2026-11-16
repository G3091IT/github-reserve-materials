# Graphify-Labs/graphify

- **仓库名**：Graphify-Labs/graphify
- **原文链接**：https://github.com/Graphify-Labs/graphify
- **Star 数**：141663（取自 GitHub 搜索 API；本环境返回数值疑似偏高/异常，真实性待核实，建议以 GitHub 网页为准）
- **最近更新时间**：2026-11-02T19:38:53Z
- **许可证**：Apache-2.0
- **语言**：Python
- **质量分 / 适配分 / 混合分**：99.6 / 50.0 / 77.3
- **结论**：ADOPT
- **标记**：无
- **命中子查询**：见适配理由

## 用途摘要
Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

## 适配理由
✓ 命中任务词：pdf；△ 未命中：word/excel/比对/对与/与文/文档/档转/转换/换的/的库

## README 要点
<p align="center">
  <a href="https://graphify.com"><img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graphify-logo.png" width="360" height="189" alt="Graphify"/></a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/25296?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-25296" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/25296" alt="Graphify-Labs%2Fgraphify | Trendshift" width="250" height="55"/></a>
</p>

<div align="center">
<details><summary><b>Read this in other languages</b></summary>

<a href="README.md">English</a> | <a href="docs/translations/README.zh-CN.md">简体中文</a> | <a href="docs/translations/README.ja-JP.md">日本語</a> | <a href="docs/translations/README.ko-KR.md">한국어</a> | <a href="docs/translations/README.de-DE.md">Deutsch</a> | <a href="docs/translations/README.fr-FR.md">Français</a> | <a href="docs/translations/README.es-ES.md">Español</a> | <a href="docs/translations/README.hi-IN.md">हिन्दी</a> | <a href="docs/translations/README.pt-BR.md">Português</a> | <a href="docs/translations/README.ru-RU.md">Русский</a> | <a href="docs/translations/README.ar-SA.md">العربية</a> | <a href="docs/translations/README.fa-IR.md">فارسی</a> | <a href="docs/translations/README.it-IT.md">Italiano</a> | <a href="docs/translations/README.pl-PL.md">Polski</a> | <a href="docs/translations/README.nl-NL.md">Nederlands</a> | <a href="docs/translations/README.tr-TR.md">Türkçe</a> | <a href="docs/translations/README.uk-UA.md">Українська</a> | <a href="docs/translations/README.vi-VN.md">Tiếng Việt</a> | <a href="docs/translations/README.id-ID.md">Bahasa Indonesia</a> | <a href="docs/translations/README.sv-SE.md">Svenska</a> | <a href="docs/translations/README.el-GR.md">Ελληνικά</a> | <a href="docs/translations/README.ro-RO.md">Română</a> | <a href="docs/translations/README.cs-CZ.md">Čeština</a> | <a href="docs/translations/README.fi-FI.md">Suomi</a> | <a href="docs/translations/README.da-DK.md">Dansk</a> | <a href="docs/translations/README.no-NO.md">Norsk</a> | <a href="docs/translations/README.hu-HU.md">Magyar</a> | <a href="docs/translations/README.th-TH.md">ภาษาไทย</a> | <a href="docs/translations/README.uz-UZ.md">Oʻzbekcha</a> | <a href="docs/translations/README.zh-TW.md">繁體中文</a> | <a href="docs/translations/README.fil-PH.md">Filipino</a> | <a href="docs/translations/README.he-IL.md">עברית</a>

</details>
</div>

<p align="center">
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://github.com/Graphify-Labs/graphify/actions/workflows/ci.yml"><img src="https://github.com/Graphify-Labs/graphify/actions/workflows/ci.yml/badge.svg?branch=v8" alt="CI"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue" alt="License: Apache-2.0"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://img.shields.io/pepy/dt/graphifyy?color=blue&label=downloads" alt="Downloads"/></a>
  <a href="https://docs.graphify.com"><img src="https://img.shields.io/badge/Docs-docs.graphify.com-0b7285?style=flat&logo=readthedocs&logoColor=white" alt="Docs"/></a>
  <a href="https://app.graphify.com/login"><img src="https://img.shields.io/badge/Graphify%20Cloud-app.graphify.com-118d4f?style=flat&logoColor=white" alt="Graphify Cloud"/></a>
  <a href="https://discord.gg/graphify"><img src="https://img.shields.io/badge/Discord-Join-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"/></a>
  <a href="https://www.youtube.com/@graphifylabs"><img src="https://img.shields.io/badge/YouTube-Graphify%20Labs-FF0000?style=flat&logo=youtube&logoColor=white" alt="YouTube"/></a>
  <a href="https://www.linkedin.com/company/graphify-labs"><img src="https://img.shields.io/badge/LinkedIn-Graphify%20Labs-0077B5?logo=linkedin" alt="LinkedIn"/></a>
  <a href="https://www.ycombinator.com/companies/graphify-labs"><img src="https://img.shields.io/badge/Y%20Combinator-S26-F0652F?style=flat&logo=ycombinator&logoColor=white" alt="YC S26"/></a>
</p>

<p align="center">
  <b>Cut agent token spend by 80%.</b> Graphify Cloud is always-on memory that governs your agents, keeps code quality high, and proves correctness with formal verification. <a href="https://app.graphify.com/login"><b>Start a free 14-day trial &rarr;</b></a>
</p>

Type `/graphify` in your AI coding assistant and it maps your entire project (code, docs, PDFs, images, videos) into a **knowledge graph** you can **query instead of grepping** through files.

- **Code maps for free, fully local.** Code is parsed with tree-sitter AST: deterministic, no LLM, nothing leaves your machine. (Docs, PDFs, images and video use your assistant's model, or a configured API key, for a semantic pass.)
- **Every edge is explained.** Each connection is tagged `EXTRACTED` (explicit in the source) or `INFERRED` (resolved by graphify), so you can tell what was read directly from what was inferred.
- **Not a vector index.** No embeddings, no vector store: a real graph you traverse. Ask a question, trace the path between two things, or explain one concept.

> [!NOTE]
> **Want this always-on?** [Graphify Cloud](https://app.graphify.com/login) keeps the graph live across your entire SDLC: monorepo and cross-repo support, formal verification, and code review with a bird's-eye view of your SDLC, plus connectors for Sentry, Jira, and more so incidents and tickets sit in the same graph as your code. **[Start a free 14-day trial at app.graphify.com](https://app.graphify.com/login)**.

<p align="center">
  <img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graph-hero.png" alt="graphify's interactive graph.html showing the FastAPI codebase as a force-directed knowledge graph with a legend of detected communities" width="900">
</p>
<p align="center">
  <em>The FastAPI codebase mapped by graphify. Every node is a concept, colors are detect
...（截断，原文见链接）

## 核心代码片段（来源：ARCHITECTURE.md）
```python
# Architecture

graphify is a Claude Code skill backed by a Python library. The skill orchestrates the library; the library can be used standalone.

## Pipeline

```
detect()  →  extract()  →  build()  →  cluster()  →  analyze helpers  →  report.generate()  →  export.to_*()
```

Each stage lives in its own module and they communicate through plain Python dicts and NetworkX graphs. While designed to minimize shared state, some stages (like extractors) rely on ambient module-level state around the active scan root. Most stages are a single function; `analyze.py` and `export.py` are sets of sibling functions rather than one entry point.

## Module responsibilities

Signatures below are the real ones - `tests/test_architecture_doc.py` imports every symbol named here, so this table cannot drift from the code.

| Module | Entry point(s) | Input → Output |
|--------|----------------|----------------|
| `detect.py` | `detect(root)` | directory → scan summary dict: `files` grouped by category, plus `total_files`, `total_words`, `warning`, `scan_root`, … |
| `extract.py` | `extract(paths, *, root=None, ...)`, `collect_files(target)` | **list** of file paths → `{nodes, edges}` dict. `collect_files` expands a directory into that list, and lives here, not in `detect.py` |
| `build.py` | `build(extractions)`, `build_from_json(extraction)` | extraction dict(s) → `nx.Graph` |
| `cluster.py` | `cluster(G)` | graph → `{community_id: [node_id, ...]}` (the graph is not mutated) |
| `analyze.py` | `god_nodes(G)`, `surprising_connections(G)`, `suggest_questions(G, communities, community_labels)`, `find_import_cycles(G)`, `graph_diff(G_old, G_new)` | graph → one list/dict per analysis. There is no single `analyze()` entry point |
| `report.py` | `generate(G, communities, cohesion_scores, community_labels, ...)` | graph + analysis → GRAPH_REPORT.md string |
| `export.py` | `to_json`, `to_html`, `to_obsidian`, `to_svg`, `to_graphml`, `to_canvas`, `to_cypher` | graph → graph.json, graph.html, Obsidian vault, graph.svg, … one function per format |
| `wiki.py` | `to_wiki(G, communities, output_dir, ...)` | graph → one markdown article per community + `index.md` |
| `callflow_html.py` | `write_callflow_html(...)` | graphify-out files → Mermaid architecture/call-flow HTML |
| `ingest.py` | `ingest(url, target_dir, ...)` | URL → file saved to corpus dir |
| `cache.py` | `check_semantic_cache(files, root)`, `save_semantic_cache(nodes, edges, ...)` | files → cached nodes / edges / hyperedges + the list of files still needing extraction |
| `security.py` | `validate_url`, `safe_fetch`, `validate_graph_path`, `sanitize_label` | URL / path / label → validated value, or raises |
| `validate.py` | `validate_extraction(data)`, `assert_valid(data)` | extraction dict → **list of schema error strings** (`validate_extraction` returns them; `assert_valid` raises) |
| `serve.py` | `serve(graph_path)`, `serve_http(graph_path, *, host, port, ...)` | graph file path → MCP stdio server / HTTP server |
| `watch.py` | `watch(watch_path, debounce=3.0)`, `check_update(watch_path)` | directory → rebuild on change; `check_update` reports whether a re-extraction is pending |
| `benchmark.py` | `run_benchmark(graph_path)` | graph file → corpus vs subgraph token comparison |

Detection counts words from text and converted documents. Supported raster images,
audio and video stay in the discovered corpus, but their raw bytes are never decoded
for word counting; detection also bypasses any older cached counts for them. SVG
remains text-readable, and PDF/Office files retain their existing text converters.
This avoids reading and splitting entire binary media files just to size the corpus.

### Calling `extract()` from your own code

`extract()` takes a **list** of paths, and `root` is keyword-only and optional:

```python
from pathlib import Path
from graphify.extract import extract

paths = [Path("src/lib/content.ts"), Path("src/pages/index.astro")]
result = extract(paths, root=Path("."
...（截断，原文见链接）
```
