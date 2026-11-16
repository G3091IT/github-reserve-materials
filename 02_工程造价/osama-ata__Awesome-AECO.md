# osama-ata/Awesome-AECO

- **仓库名**：osama-ata/Awesome-AECO
- **原文链接**：https://github.com/osama-ata/Awesome-AECO
- **Star 数**：41（取自 GitHub 搜索 API；本环境数值可能偏高，待核实）
- **最近更新时间**：2026-11-06T13:11:03Z
- **许可证**：CC0-1.0
- **语言**：HTML
- **质量分 / 适配分 / 混合分**：82.2 / 12.0 / 50.6
- **结论**：ADOPT
- **标记**：无
- **领域适配**：领域词:cost estimation/bim

## 用途摘要
A curated list of open-source AECO (Architecture, Engineering, Construction, Operations) tools: BIM, IFC, CAD, Revit, simulation, structural analysis, parametric design, digital twins, GIS, cost estimation and AI.

## 适配理由
⚠ 未命中任何任务关键词，可能不相关

## README 要点
# Awesome AECO [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

AECO stands for Architecture, Engineering, Construction, and Operations. It refers to the integrated process of designing, building, and managing a building or infrastructure project throughout its lifecycle, from the initial design to ongoing maintenance and operations. This process involves various disciplines working together to create and manage a built environment.

> A curated list of awesome AECO resources, tools, and technologies.
> Inspired by [Awesome](https://github.com/sindresorhus/awesome).

## Contents

- [Awesome AECO](#awesome-aeco-)
  - [Contents](#contents)
  - [BIM (Building Information Modeling)](#bim-building-information-modeling)
  - [CAD (Computer-Aided Design)](#cad-computer-aided-design)
  - [Revit Plugins \& Extensions](#revit-plugins--extensions)
  - [Simulation \& Analysis](#simulation--analysis)
  - [Energy \& Sustainability](#energy--sustainability)
  - [Parametric \& Computational Design](#parametric--computational-design)
  - [IoT \& Smart Buildings](#iot--smart-buildings)
  - [Facility \& Asset Management](#facility--asset-management)
  - [Generative Design](#generative-design)
  - [Construction Automation \& Robotics](#construction-automation--robotics)
  - [AI \& Automation for AECO](#ai--automation-for-aeco)
  - [Digital Twins](#digital-twins)
  - [GIS \& Mapping](#gis--mapping)
  - [Project Management](#project-management)
  - [Cost Estimation \& Quantity Takeoff](#cost-estimation--quantity-takeoff)
  - [FAQ](#faq)
  - [Related Lists](#related-lists)
  - [Contribute](#contribute)
  - [License](#license)

---

## BIM (Building Information Modeling)

- **IfcOpenShell**
  Open-source toolkit and geometry engine for BuildingSMART IFC files. Enables reading, writing, and modifying BIM models via a C++ library and Python API.
  *GitHub: [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell)*

- **xBIM Toolkit**
  The eXtensible BIM Toolkit for .NET, providing libraries to work with IFC data (read, create, validate). Allows developers on the Microsoft stack to build BIM applications.
  *GitHub: [xBimTeam/XbimEssentials](https://github.com/xBimTeam/XbimEssentials)*

- **BIMserver**
  Open-source BIM server platform (Java) that stores and manages building models using IFC. Acts as a model database with versioning and multi-user collaboration.
  *GitHub: [opensourceBIM/BIMserver](https://github.com/opensourceBIM/BIMserver)*

- **IFC.js**
  JavaScript toolkit (WASM-powered) for bringing IFC BIM data into web applications. Includes `web-ifc` for fast parsing and `web-ifc-three` for viewing in Three.js.
  *GitHub: [ThatOpen/engine_web-ifc](https://github.com/ThatOpen/engine_web-ifc)*

- **That Open Engine Fragments**
  High-performance 3D engine for efficiently handling massive amounts of BIM data using the Fragments format.
  *GitHub: [ThatOpen/engine_fragment](https://github.com/ThatOpen/engine_fragment)*

- **That Open UI Components**
  Collection of web components designed for Building Information Modeling (BIM) applications.
  *GitHub: [ThatOpen/engine_ui-components](https://github.com/ThatOpen/engine_ui-components)*

- **Speckle**
  Open-source AEC data platform ("Git for BIM") that enables real-time collaboration and interoperability by streaming geometry and data between design tools.
  *GitHub: [specklesystems/speckle-server](https://github.com/specklesystems/speckle-server)*

- **BHoM (Buildings and Habitats object Model)**
  A collaborative computational framework and data schema for the built environment. Defines a core object model for AEC domains (structure, environment, MEP, etc.).
  *GitHub: [BHoM/BHoM](https://github.com/BHoM/BHoM)*

- **Revit SDK Samples**
  Revit SDK documentation and samples demonstrating Revit API usage for automation and plugin development, maintained by Autodesk's Jeremy Tammik.
  *GitHub: [jeremytammik/RevitSdkSamples](https://github.com/jeremytammik/RevitSdkSamples)*

- **BIMsurfer**
  Web-based BIM viewer for IFC models with clash detection and collaboration features.
  *GitHub: [opensourceBIM/BIMsurfer](https://github.com/opensourceBIM/BIMsurfer)*

- **GomeraX**
  Experimental IFC viewer with AI-powered BIM assistant. Features WebGL and WebGPU rendering, advanced sectioning, first-person navigation, element clustering, and natural language commands for model interaction via local LLM.
  *GitHub: [salpbes/GomeraX](https://github.com/salpbes/GomeraX)*

- **dotBIM (.bim)**
  Minimalist file format for BIM.
  *GitHub: [paireks/dotbim](https://github.com/paireks/dotbim)*

- **xeokit convert**
  Convert BIM and AEC models directly into XKT files with JavaScript for super fast loading into xeokit.
  *GitHub: [xeokit/xeokit-convert](https://github.com/xeokit/xeokit-convert)*

- **xeokit BIM Viewer**
  Bundled BIM Viewer built on top of xeokit SDK with features like measurements, tree view explorer, annotations, slicing, first-person navigation.
  *GitHub: [xeokit/xeokit-bim-viewer](https://github.com/xeokit/xeokit-bim-viewer)*

- **xeokit SDK**
  Productive open-source JavaScript SDK and 3D engine with its own WebGL renderer and extensive library of feature examples for viewing BIM, IFC, BCF, Revit, Point Clouds and other with real-world coordinates and double precision with XKT format.
  *GitHub: [xeokit/xeokit-sdk](https://github.com/xeokit/xeokit-sdk)*

- **IFClite**
  Open-source toolkit for working with IFC files in the browser, on a server, or in a desktop app. Features a WebGPU 3D viewer, IFC4/IFC4X3 support, BCF collaboration, IDS compliance checking, bSDD lookup, 2D drawing generation, and export to IFC, glTF, CSV, JSON, and Parquet.
  *GitHub: [LTplus-AG/ifc-lite](https://github.com/LTplus-AG/ifc-lite)*

- **goifc**
  Pure-Go, cgo-free IFC reader: parses STEP, walks the spatial and semantic model, tessellates geometry, and labels every quantity with where it came from (authored Qto or derived from geometry). Geometry bound
...（截断，原文见链接）

## 核心代码片段（来源：LICENSE）
```html
Creative Commons Legal Code

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.

Statement of Purpose

The laws of most jurisdictions throughout the world automatically confer
exclusive Copyright and Related Rights (defined below) upon the creator
and subsequent owner(s) (each and all, an "owner") of an original work of
authorship and/or a database (each, a "Work").

Certain owners wish to permanently relinquish those rights to a Work for
the purpose of contributing to a commons of creative, cultural and
scientific works ("Commons") that the public can reliably and without fear
of later claims of infringement build upon, modify, incorporate in other
works, reuse and redistribute as freely as possible in any form whatsoever
and for any purposes, including without limitation commercial purposes.
These owners may contribute to the Commons to promote the ideal of a free
culture and the further production of creative, cultural and scientific
works, or to gain reputation or greater distribution for their Work in
part through the use and efforts of others.

For these and/or other purposes and motivations, and without any
expectation of additional consideration or compensation, the person
associating CC0 with a Work (the "Affirmer"), to the extent that he or she
is an owner of Copyright and Related Rights in the Work, voluntarily
elects to apply CC0 to the Work and publicly distribute the Work under its
terms, with knowledge of his or her Copyright and Related Rights in the
Work and the meaning and intended legal effect of CC0 on those rights.

1. Copyright and Related Rights. A Work made available under CC0 may be
protected by copyright and related or neighboring rights ("Copyright and
Related Rights"). Copyright and Related Rights include, but are not
limited to, the following:

  i. the right to reproduce, adapt, distribute, perform, display,
     communicate, and translate a Work;
 ii. moral rights retained by the original author(s) and/or performer(s);
iii. publicity and privacy rights pertaining to a person's image or
     likeness depicted in a Work;
 iv. rights protecting against unfair competition in regards to a Work,
     subject to the limitations in paragraph 4(a), below;
  v. rights protecting the extraction, dissemination, use and reuse of data
     in a Work;
 vi. database rights (such as those arising under Directive 96/9/EC of the
     European Parliament and of the Council of 11 March 1996 on the legal
     protection of databases, and under any national implementation
     thereof, including any amended or successor version of such
     directive); and
vii. other similar, equivalent or corresponding rights throughout the
     world based on applicable law or treaty, and any national
     implementations thereof.

2. Waiver. To the greatest extent permitted by, but not in contravention
of, applicable law, Affirmer hereby overtly, fully, permanently,
irrevocably and unconditionally waives, abandons, and surrenders all of
Affirmer's Copyright and Related Rights and associated claims and causes
of action, whether now known or unknown (including existing as well as
future claims and causes of action), in the Work (i) in all territories
worldwide, (ii) for the maximum duration provided by applicable law or
treaty (including future time extensions), (iii) in any current or future
medium and for any number of copies, and (iv) for any purpose whatsoever,
including without limitation commercial, advertising or promotional
purposes (the "Waiver"). Affirmer makes t
...（截断，原文见链接）
```
