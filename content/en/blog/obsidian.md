+++
title = 'Obsidian: Your Second Brain, Built on Plain Text'
date = 2025-05-18T21:30:03+03:30
draft = false
author = "Abbas Endari"
description = "Why Obsidian is the best note-taking app for thinkers, builders, and anyone who values their data. Part One: Introduction and the Why."
tags = ["Admin", "Software", "Productivity", "PKM"]
thumbnail ="/Obsidian_logo.png"
+++

# Obsidian: Your Second Brain, Built on Plain Text

## Let's agree on one thing

**Obsidian is easily one of the best choices you can make when it comes to note-taking apps.**

Over the years, I've tried more note-taking apps than I can count — from good old Windows Notepad and Samsung Notes (back when it was still called S Note!) all the way to Notion, MS Word, Apple Notes, Google Keep, Evernote, OneNote, Roam Research, Logseq, and Craft. You name it, I've dabbled with it.

But in the end, only two tools have consistently pulled me back: **Neovim in the terminal** and **Obsidian**.

They share a philosophy: **your data, your control, your workflow.** No vendor lock-in. No proprietary formats. No subscription required to read your own thoughts.

In this blog series, I'll first convince you why Obsidian deserves a place in your toolkit — then show you how to turn it into your most powerful productivity weapon yet.

---

## Let's start with the "Why"

Why not?

- **It's free** (for personal use — the core app costs $0)
- **It's Markdown-based** — your notes are plain `.md` files
- **It's insanely flexible** thanks to a huge collection of community plugins (1,500+ and counting)
- **Your notes stay yours** — stored locally, synced however *you* choose (iCloud, Syncthing, Git, Obsidian Sync, Remotely Save, whatever)
- **It runs everywhere** — Windows, macOS, Linux, iOS, Android
- **It works offline** — no cloud dependency to read or write your own mind

Of course, there are many more reasons why Obsidian might be the perfect choice for you. (Said Yoda, probably.)

But hey, maybe you're a Notion person — lost in infinite pages and toggles — and beyond redemption. 😄

---

## The Core Insight: Notes as a Graph, Not a Tree

Traditional note apps (Notion, Evernote, OneNote) force a **hierarchy**: notebooks → sections → pages. You decide upfront where something belongs. But knowledge doesn't work that way.

Obsidian introduces **links** (`[[WikiLinks]]`) and a **graph view** that visualizes connections between notes. This mirrors how your brain actually works — associative, not hierarchical.

```
Traditional:  Notebook → Project A → Meeting Notes → "API design"
Obsidian:     "API design" ←→ "REST best practices" ←→ "Authentication" ←→ "JWT tokens"
```

When you link notes, you build a **knowledge graph**. Over time, patterns emerge. Clusters form. You discover connections you didn't consciously make. This is the "second brain" promise — not storage, *synthesis*.

---

## The File-Over-App Philosophy

> "If you want to own your data for the next 50 years, store it in plain text files." — Steph Ango (Obsidian CEO)

This is the hill Obsidian dies on. Your vault is a folder of `.md` files. That's it.

| What this means for you |
|-------------------------|
| **No migration needed** — open your vault in VS Code, Neovim, Typora, or `cat` |
| **Version control** — `git init` your vault, commit daily, never lose a thought |
| **Scriptable** — Python, bash, or Obsidian plugins can manipulate your notes programmatically |
| **Future-proof** — Markdown will be readable long after Obsidian (the company) is gone |
| **Portable** — copy the folder to a USB, another computer, a server — it just works |

Compare this to Notion: export is a ZIP of JSON/CSV/Markdown that loses databases, relations, and formatting. Good luck reconstructing your workspace.

---

## But... Isn't It Just a Markdown Viewer?

**No.** That's like saying Neovim is "just a text editor."

Out of the box, Obsidian gives you:

- **WikiLinks** (`[[Note Name]]`) with autocomplete
- **Backlinks** — see every note that links *to* the current one
- **Graph View** — interactive force-directed graph of your vault
- **Canvas** — infinite spatial whiteboard for visual thinking
- **Daily Notes** — one-click journaling with templates
- **Command Palette** — `Ctrl/Cmd+P` for everything (VS Code style)
- **Vim keybindings** — first-class, not an afterthought
- **Split panes** — vertical/horizontal, infinite nesting
- **Search** — regex, boolean, field-based, saved searches
- **Properties (YAML frontmatter)** — structured metadata per note

And that's before plugins.

---

## The Plugin Ecosystem: Where Obsidian Becomes *Yours*

Core plugins (built-in, toggleable): **Canvas, Daily Notes, Graph View, Outliner, Slides, Templates, Workspaces, Sync, Publish.**

Community plugins (1,500+): this is where the magic happens.

### My Essential Plugin Stack

| Category | Plugins | Why |
|----------|---------|-----|
| **Task Management** | `Tasks`, `Dataview` | Query tasks across vault: `tasks not done` → see everything |
| **Knowledge Synthesis** | `Dataview`, `DataviewJS`, `Excalidraw` | Query notes as data; hand-drawn diagrams that *are* Markdown |
| **Writing & Editing** | `Linter`, `Advanced Tables`, `Various Complements` | Auto-format, spreadsheet-like tables, smart autocomplete |
| **Navigation** | `Omnisearch`, `Quick Switcher++`, `Strange New Worlds` | Fuzzy find anything; discover unlinked connections |
| **Productivity** | `Templater`, `Periodic Notes`, `Kanban` | Dynamic templates; weekly/monthly notes; project boards |
| **Academic/Reference** | `Zotero Integration`, `Citation` | Reference manager inside your notes |
| **Developer Tools** | `Code Block Customizer`, `Copy Code Block`, `Obsidian Git` | Dev-friendly editing; auto-commit vault to Git |

### Dataview Example: Living Dashboards

```dataview
TABLE status, due, priority
FROM "Projects"
WHERE status != "done"
SORT priority DESC, due ASC
```

This renders a live table that updates as you edit notes. No database. No backend. Just Markdown with YAML frontmatter.

---

## Sync: You Choose the Plumbing

Obsidian doesn't force a sync solution. Pick your poison:

| Method | Cost | Pros | Cons |
|--------|------|------|------|
| **Obsidian Sync** | $8/mo | E2E encrypted, version history, selective sync, mobile-first | Paid, proprietary |
| **iCloud / Google Drive / OneDrive** | Free (with storage) | Native OS integration, free tier | No E2E encryption, conflict-prone on mobile |
| **Syncthing** | Free | P2P, no cloud, E2E encrypted, cross-platform | No iOS support (use Möbius Sync), setup friction |
| **Git + GitHub/GitLab** | Free | Version history, free, programmable, public/private | Manual commits, conflicts need resolution, no mobile Git client |
| **Remotely Save (plugin)** | Free | Supports S3, WebDAV, OneDrive, Dropbox, etc. | Plugin-dependent, config required |
| **Obsidian LiveSync (plugin)** | Free | Self-hosted CouchDB, E2E encrypted, real-time | Requires server, technical setup |

**My setup:** Git for version history + Obsidian Sync for frictionless mobile/desktop sync. Best of both worlds.

---

## Mobile: It Actually Works

Historically, mobile Markdown apps were painful. Obsidian mobile is a **first-class citizen**:

- Same plugin architecture (most community plugins work)
- Touch-optimized UI (swipe for backlinks, long-press for context menus)
- Offline-first — edit on a plane, sync when you land
- Obsidian Sync or Remotely Save handles background sync
- iOS Shortcuts integration for quick capture

I write ~40% of my notes on iPhone now. The friction is gone.

---

## A Peek at My Vault Structure

```
📁 Vault/
├── 📁 00-Inbox/           # Quick capture, process daily
├── 📁 01-Daily/           # Daily notes (auto-created via Periodic Notes)
├── 📁 02-Projects/        # Active projects (each = folder with index.md)
├── 📁 03-Areas/           # Ongoing responsibilities (Health, Finance, Career)
├── 📁 04-Resources/       # Reference material (articles, specs, snippets)
├── 📁 05-Archive/         # Completed/on-hold projects
├── 📁 99-Meta/            # Templates, scripts, MOCs, settings
│   ├── 📁 Templates/      # Templater templates
│   ├── 📁 MOCs/           # Maps of Content (index notes)
│   └── 📁 Scripts/        # Python/JS for automation
└── 📁 Attachments/        # Images, PDFs (auto-organized by plugin)
```

This follows **PARA** (Projects, Areas, Resources, Archives) — popularized by Tiago Forte, adapted for Obsidian's linking model.

---

## The Learning Curve: Honest Assessment

| Phase | Duration | Feeling |
|-------|----------|---------|
| **Install & write** | Day 1 | "Okay, it's a Markdown editor" |
| **Discover links & graph** | Week 1 | "Oh, connections *matter*" |
| **First plugins (Tasks, Dataview)** | Week 2-3 | "Wait, I can query my notes?" |
| **Build templates & workflows** | Month 1 | "This is *my* system now" |
| **MOCs & synthesis** | Month 2+ | "I'm thinking *with* my notes" |

The dip is real. Week 2 you'll wonder if it's worth it. Push through. The compounding starts when you stop *filing* and start *linking*.

---

## What's Next in This Series

This post is the "why." The upcoming posts are the "how":

1. **Vault Setup & Core Configuration** — settings that matter, folder structure, core plugins to enable
2. **The Plugin Deep Dive** — Tasks, Dataview, Templater, Excalibraw, Kanban — config snippets included
3. **Daily Notes & Periodic Notes** — journaling, weekly reviews, templates that save hours
4. **Knowledge Synthesis: MOCs, Dataview, & the Graph** — turning links into insight
5. **Mobile & Sync Mastery** — frictionless capture, conflict-free sync, iOS Shortcuts
6. **Developer Workflows** — code snippets, API docs, diagram-as-code, Git integration
7. **Advanced: Scripting, Automation, & Custom Plugin Development** — Python API, Obsidian URI scheme, building your own tools

Each post will be practical: config you can copy, workflows you can adopt, and the small details that make the difference between "it works" and "it thinks with me."

---

## Your Turn

If you've read this far, you're either already convinced or PKM-curious. Here's my challenge:

**Try it for 30 days.** Not "open it once a week." Daily driver. Create a vault. Write one note a day. Link it to yesterday's note. Install *Tasks* and *Dataview*. Build one template.

Week one: awkward. Week two: "okay, I see it." Week three: "how did I ever think without this?"

And if you hate it? Your notes are a folder of `.md` files. Open them in VS Code, Neovim, or `grep`. Zero lock-in. But I'd bet my mechanical keyboard you won't go back.

---

_This post was written in Obsidian 1.6, rendered by Hugo 0.120, deployed via GitHub Actions. Vault structure inspired by [PARA](https://fortelabs.com/blog/para/) and [Luhmann's Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)._

_Next in series: "Vault Setup & Core Configuration — The Foundation That Scales"_