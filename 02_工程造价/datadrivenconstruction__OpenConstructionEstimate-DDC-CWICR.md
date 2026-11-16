# datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR

- **仓库名**：datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR
- **原文链接**：https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR
- **Star 数**：283（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-08-21T19:22:00Z
- **许可证**：NOASSERTION
- **语言**：HTML
- **质量分 / 适配分 / 混合分**：75.9 / 12.0 / 47.1
- **结论**：ADOPT
- **标记**：LICENSE-UNCLEAR
- **领域适配**：人工预核验相关(强制收录，绕过领域闸门)

## 用途摘要
Open multilingual construction cost database for AI Agents - 55K+ work items, 27K+ resources, 30 regions. Semantic search via Qdrant vector DB

## 适配理由
人工预核验相关（强制收录，绕过领域闸门）：开源多语言「建筑工程工项 / 构件 / 资源（CWICR）」成本数据库，含 55K+ 工项、27K+ 资源、覆盖 30 个地区，并提供基于描述 / 照片 / CAD(BIM) 的工程量估算 n8n 流水线。直接对应"工程造价 / 工程量清单 / 算量"主题，可为本机投标报价测算提供工料机单价与工程量参照基准。（注：score_repo 因仓库描述未含中文/投标关键词而自动提示"可能不相关"，已据人工审计覆盖。）

## README 要点
<h3 align="center">DDC CWICR - Construction Work Items, Components & Resources </br>
  + Pipelines n8n for calculating estimates based on descriptions, photos, and CAD (BIM)</h3>

<p align="center">
  <a href="README.md"><b>🇬🇧 English</b></a> •
  <a href="README.zh-CN.md">🇨🇳 中文</a> •
  <a href="README.es.md">🇪🇸 Español</a> •
  <a href="README.pt-BR.md">🇧🇷 Português</a> •
  <a href="README.ru.md">🇷🇺 Русский</a> •
  <a href="README.ja.md">🇯🇵 日本語</a> •
  <a href="README.de.md">🇩🇪 Deutsch</a> •
  <a href="README.fr.md">🇫🇷 Français</a>
</p>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Work_Items-55,719-2563eb?style=for-the-badge" alt="Work Items">
  <img src="https://img.shields.io/badge/Resources-27,672-059669?style=for-the-badge" alt="Resources">
  <img src="https://img.shields.io/badge/Languages-23-d97706?style=for-the-badge" alt="Languages">
  <img src="https://img.shields.io/badge/Countries-30-dc2626?style=for-the-badge" alt="Countries">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0_+_Commercial-green?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Version-v0.1.1-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/Embeddings-OpenAI_3072d-412991?style=flat-square" alt="Embeddings">
  <img src="https://img.shields.io/badge/Vector_DB-Qdrant-dc382d?style=flat-square" alt="Qdrant">
  <img src="https://img.shields.io/badge/Automation-n8n-ea4b71?style=flat-square" alt="n8n">
</div>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate_bottom.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<h3 align="center">⚡ n8n Workflows</h3>
<p align="center"><code>Choose your input → Get cost estimate</code></p>

<br>

<table width="100%">
<tr>

<td align="center" valign="top" width="33%">
<br>
<h3>📝 Text</h3>
<p>Quick scope-to-estimate<br>from a short description</p>
<p><b>Input:</b> Telegram / chat message<br>
<b>Output:</b> Matched work items + estimate</p>
<br>
<a href="#1️⃣-text-estimator-bot">📖 Documentation</a>
<br><br>
<a href="./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Download_Workflow-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Download"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>📷 Photo / PDF</h3>
<p>Site photos, scanned BOQ,<br>photo-PDF from the field</p>
<p><b>Input:</b> Image or PDF pages<br>
<b>Output:</b> Extracted scope → estimate</p>
<br>
<a href="#2️⃣-photo-cost-estimator">📖 Photo Docs</a> · <a href="#3️⃣-universal-estimator-bot-text--photo--pdf">📖 Universal Bot</a>
<br><br>
<a href="./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Photo_Workflow-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Photo"/>
</a>
&nbsp;
<a href="./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Telegram_Bot-0A84FF?style=for-the-badge&logo=telegram&logoColor=white" alt="Bot"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>🧊 CAD / BIM</h3>
<p>Revit / IFC / DWG-based<br>quantification & estimating</p>
<p><b>Input:</b> Model export <br>
<b>Output:</b> 4D/5D estimate + breakdown</p>
<br>
<a href="#4️⃣-cad-bim-cost-estimation-pipeline">📖 Documentation</a>
<br><br>
<a href="./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Download_Workflow-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Download"/>
</a>
<br><br>
</td>

</tr>
</table>

<br>
<p align="center">
  <a href="https://openconstructionestimate.com">
    <img src="https://img.shields.io/badge/🌐_LIVE_DEMO_(only_database)-openconstructionestimate.com-2563eb?style=for-the-badge" alt="Live Demo">
  </a>
</p>

---

<h2 align="center">🏗️ OpenConstructionERP - Use This Database End-to-End</h2>

<p align="center">
  <b>Open-source ERP that ships this database pre-loaded.</b> Professional BoQ editor,
  AI-powered photo / PDF / CAD takeoff, 4D/5D planning, dashboards - all running on
  the 30-track CWICR cost data below.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=X06cIaroAeI">
    <img src="https://img.shields.io/badge/▶_Watch_full_demo_(12_min)-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube demo">
  </a>
  &nbsp;
  <a href="https://openconstructionerp.com">
    <img src="https://img.shields.io/badge/🌐_Live_app-openconstructionerp.com-2ea44f?style=for-the-badge" alt="Live app">
  </a>
  &nbsp;
  <a href="https://github.com/datadrivenconstruction/OpenConstructionERP">
    <img src="https://img.shields.io/badge/⭐_Source-github.com/datadrivenconstruction/OpenConstructionERP-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub repo">
  </a>
</p>

<p align="center">
  <a href="https://github.com/datadrivenconstruction/OpenConstructionERP">
    <img src="https://github.com/datadrivenconstruction/OpenConstructionERP/raw/main/docs/screenshots/hero-overview.jpg" width="95%" alt="OpenConstructionERP hero">
  </a>
</p>

### Get up and running in 30 seconds

```bash
pip install --upgrade openconstructionerp
openestimate                      # opens the desktop app at http://localhost:8080
```

The app launches with the **30 CWICR country tracks pre-installed** - start a new
project, pick a region, and the BoQ editor instantly suggests rates from
`ddc_de_berlin`, `ddc_au_sydney`, `ddc_hr_zagreb`, etc. with proper localised
prices and tran
...（截断，原文见链接）

## 核心代码片段（来源：DATA_DICTIONARY.md）
```html
# Data Dictionary - DDC CWICR

This document describes the physical layout, column semantics,
and provenance of the DDC CWICR dataset (Construction Work Items,
Costs & Resources). Licensing of the dataset is documented in
[LICENSE](./LICENSE) and [NOTICE](./NOTICE); this file describes
the *data* itself.

## Dataset shape (as of April 2026)

- **55,719** work items / rates
- **27,672** unique resources (labour / material / equipment)
- **30** language × region tracks (11 shipped + 19 derived)
- **93** columns in the primary work-items tables (canonical schema;
  EN_TORONTO has a 84-col legacy variant kept for compatibility,
  USA_USD adds 6 US-specific extras)

## Directory layout

Each language / region track has its own directory:

### Shipped tracks (11)

| Directory               | Language                          | Reference region     | Currency |
|-------------------------|-----------------------------------|----------------------|---------|
| `AR___DDC_CWICR/`       | Arabic                            | Dubai (UAE)          | AED |
| `DE___DDC_CWICR/`       | German                            | Berlin (Germany)     | EUR |
| `EN___DDC_CWICR/`       | English                           | Toronto (Canada)     | CAD |
| `ES___DDC_CWICR/`       | Spanish                           | Barcelona (Spain)    | EUR |
| `FR___DDC_CWICR/`       | French                            | Paris (France)       | EUR |
| `HI___DDC_CWICR/`       | Hindi                             | Mumbai (India)       | INR |
| `PT___DDC_CWICR/`       | Portuguese                        | São Paulo (Brazil)   | BRL |
| `RU___DDC_CWICR/`       | Russian                           | St. Petersburg (Russia) | RUB |
| `UK___DDC_CWICR/`       | English                           | United Kingdom       | GBP |
| `US___DDC_CWICR/`       | English                           | United States        | USD |
| `ZH___DDC_CWICR/`       | Chinese                           | Shanghai (China)     | CNY |

### Derived tracks (19, generated by the DDC country-track build pipeline)

| Directory               | Language                          | Reference region     | Currency |
|-------------------------|-----------------------------------|----------------------|---------|
| `AU___DDC_CWICR/`       | English                           | Sydney (Australia)   | AUD |
| `HR___DDC_CWICR/`       | Croatian                          | Zagreb (Croatia)     | EUR |
| `BG___DDC_CWICR/`       | Bulgarian                         | Sofia (Bulgaria)     | BGN |
| `JA___DDC_CWICR/`       | Japanese                          | Tokyo (Japan)        | JPY |
| `KO___DDC_CWICR/`       | Korean                            | Seoul (S. Korea)     | KRW |
| `IT___DDC_CWICR/`       | Italian                           | Rome (Italy)         | EUR |
| `NL___DDC_CWICR/`       | Dutch                             | Amsterdam (Netherlands) | EUR |
| `PL___DDC_CWICR/`       | Polish                            | Warsaw (Poland)      | PLN |
| `SV___DDC_CWICR/`       | Swedish                           | Stockholm (Sweden)   | SEK |
| `CS___DDC_CWICR/`       | Czech                             | Prague (Czechia)     | CZK |
| `TR___DDC_CWICR/`       | Turkish                           | Istanbul (Turkey)    | TRY |
| `ID___DDC_CWICR/`       | Indonesian                        | Jakarta (Indonesia)  | IDR |
| `VI___DDC_CWICR/`       | Vietnamese                        | Hanoi (Vietnam)      | VND |
| `TH___DDC_CWICR/`       | Thai                              | Bangkok (Thailand)   | THB |
| `RO___DDC_CWICR/`       | Romanian                          | Bucharest (Romania)  | RON |
| `MX___DDC_CWICR/`       | Spanish (Mexico)                  | Mexico City (Mexico) | MXN |
| `NZ___DDC_CWICR/`       | English                           | Auckland (New Zealand) | NZD |
| `NG___DDC_CWICR/`       | English                           | Lagos (Nigeria)      | NGN |
| `ZA___DDC_CWICR/`       | English                        
...（截断，原文见链接）
```
