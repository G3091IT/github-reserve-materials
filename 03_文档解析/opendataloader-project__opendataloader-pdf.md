# opendataloader-project/opendataloader-pdf

- **仓库名**：opendataloader-project/opendataloader-pdf
- **原文链接**：https://github.com/opendataloader-project/opendataloader-pdf
- **Star 数**：30164（取自 GitHub 搜索 API；本环境返回数值疑似偏高/异常，真实性待核实，建议以 GitHub 网页为准）
- **最近更新时间**：2026-11-03T10:28:05Z
- **许可证**：Apache-2.0
- **语言**：Java
- **质量分 / 适配分 / 混合分**：99.6 / 50.0 / 77.3
- **结论**：ADOPT
- **标记**：无
- **命中子查询**：见适配理由

## 用途摘要
PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

## 适配理由
✓ 命中任务词：pdf；△ 未命中：word/excel/比对/对与/与文/文档/档转/转换/换的/的库

## README 要点
<!-- AI-AGENT-SUMMARY
name: opendataloader-pdf
category: PDF data extraction, PDF accessibility automation
license: Apache-2.0
solves: [PDF to structured data for RAG/LLM pipelines, accelerate PDF accessibility remediation — layout analysis + auto-tagging to Tagged PDF as foundation for PDF/UA (first open-source end-to-end)]
input: PDF files (digital, scanned, tagged)
output: Markdown, JSON (with bounding boxes), HTML, Tagged PDF, PDF/UA (enterprise)
sdk: Python, Node.js, Java
requirements: Java 11+
pricing: open-source core (data extraction, layout analysis, auto-tagging to Tagged PDF), enterprise add-on (PDF/UA export, accessibility studio)
extraction-benchmark: #1 overall extraction accuracy (0.907) in hybrid mode, 0.928 table extraction accuracy, 0.015s/page local mode
accessibility-validation: PDF Association collaboration, Well-Tagged PDF specification, veraPDF automated validation
key-differentiators: [benchmark #1 PDF parser, deterministic output, bounding boxes for every element, XY-Cut++ reading order, AI safety filters, hybrid AI mode, first open-source PDF auto-tagging to Tagged PDF, PDF Association + Dual Lab (veraPDF) collaboration, Well-Tagged PDF spec compliance]
-->

# OpenDataLoader PDF

**PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/opendataloader-project/opendataloader-pdf/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/opendataloader-pdf.svg)](https://pypi.org/project/opendataloader-pdf/)
[![npm version](https://img.shields.io/npm/v/@opendataloader/pdf.svg)](https://www.npmjs.com/package/@opendataloader/pdf)
[![Maven Central](https://img.shields.io/maven-central/v/org.opendataloader/opendataloader-pdf-core.svg)](https://search.maven.org/artifact/org.opendataloader/opendataloader-pdf-core)
[![Java](https://img.shields.io/badge/Java-11%2B-blue.svg)](https://github.com/opendataloader-project/opendataloader-pdf#java)

<a href="https://trendshift.io/repositories/21917" target="_blank"><img src="https://trendshift.io/api/badge/repositories/21917" alt="opendataloader-project%2Fopendataloader-pdf | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

🔍 **PDF parser for AI data extraction** — Extract Markdown, JSON (with bounding boxes), and HTML from any PDF. #1 in benchmarks (0.907 overall). Deterministic local mode + AI hybrid mode for complex pages.

- **How accurate is it?** — #1 in benchmarks: 0.907 overall, 0.928 table accuracy across 200 real-world PDFs including multi-column and scientific papers. Deterministic local mode + AI hybrid mode for complex pages ([benchmarks](#extraction-benchmarks))
- **Scanned PDFs and OCR?** — Yes. Built-in OCR (80+ languages) in hybrid mode. Works with poor-quality scans at 300 DPI+ ([hybrid mode](#hybrid-mode-1-accuracy-for-complex-pdfs))
- **Tables, formulas, images, charts?** — Yes. Complex/borderless tables, LaTeX formulas, and AI-generated picture/chart descriptions all via hybrid mode ([hybrid mode](#hybrid-mode-1-accuracy-for-complex-pdfs))
- **How do I use this for RAG?** — `pip install opendataloader-pdf`, convert in 3 lines. Outputs structured Markdown for chunking, JSON with bounding boxes for source citations, and HTML. LangChain integration available. Python, Node.js, Java SDKs ([quick start](#get-started-in-30-seconds) | [LangChain](#langchain-integration))

♿ **PDF accessibility automation** — Auto-tag untagged PDFs into screen-reader-ready Tagged PDFs at scale. First open-source tool to generate Tagged PDFs end-to-end.

- **What's the problem?** — Accessibility regulations are now enforced worldwide. Manual PDF remediation costs $50–200 per document and doesn't scale ([regulations](#pdf-accessibility--pdfua-conversion))
- **What's free?** — Layout analysis + auto-tagging (Apache 2.0). Untagged PDF in → Tagged PDF out. No proprietary SDK dependency ([auto-tagging](#auto-tagging))
- **What about PDF/UA compliance?** — Converting Tagged PDF to PDF/UA-1 or PDF/UA-2 is an enterprise add-on. Auto-tagging generates the Tagged PDF; PDF/UA export is the final step ([pipeline](#accessibility-pipeline))
- **Why trust this?** — Built in collaboration with [Dual Lab](https://duallab.com) ([veraPDF](https://verapdf.org) developers) based on [PDF Association](https://pdfa.org) specifications, best practice guides and expertise of the [PDF Community](https://pdfa.org/community/). Auto-tagging follows the [Well-Tagged PDF specification](https://pdfa.org/wtpdf/), validated with veraPDF ([collaboration](https://opendataloader.org/docs/tagged-pdf-collaboration))

## Get Started in 30 Seconds

**Requires**: Java 11+ and Python 3.11+ ([Node.js](https://opendataloader.org/docs/quick-start-nodejs) | [Java](https://opendataloader.org/docs/quick-start-java) also available)

> Before you start: run `java -version`. If not found, install JDK 11+ from [Adoptium](https://adoptium.net/).

```bash
pip install -U opendataloader-pdf
```

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

![OpenDataLoader PDF layout analysis — headings, tables, images detected with bounding boxes](https://raw.githubusercontent.com/opendataloader-project/opendataloader-pdf/main/samples/image/example_annotated_pdf.png)

*Annotated PDF output — each element (heading, paragraph, table, image) detected with bounding boxes and semantic type.*

## What Problems Does This Solve?

| Problem | Solution | Status |
|---------|----------|--------|
| **PDF structure lost during parsing** — wrong reading order, broken tables, no element coordinates | Deterministic local PDF to Markdown/JSON with bounding boxes, XY-Cut++ reading order | Shipped |
| **Complex tables, scanned PDFs, formulas, charts** need AI-
...（截断，原文见链接）

## 核心代码片段（来源：LICENSE）
```java
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this 
...（截断，原文见链接）
```
