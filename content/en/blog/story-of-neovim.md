+++
date = 2026-06-29
draft = false
title = 'NeoVim'
author = 'Abbas Endari'
description = 'In the age of AI and voice assistance, this how i make myself feel nostalgic.'
thumbnail = '/NeoVim.jpg'
+++

# Terminal, real home of any computer enthusiast.

Vim the simplest of all word processors, or in my slightly moderner case: "Neovim" is the step you get back before jumping far ahead! Yes, I know! At first it seems like a setback — with your 6-button mouse, or even worse your touch Apple Mouse, you wouldn't even consider going back to a simple Terminal app with almost no GUI and the weirdest set of shortcut keys to be more productive. But that itself is one of the biggest catches of learning your way around VIM: the simplicity, and simultaneous customizability of vim is actually liberating.

---

## Why I came back to the terminal

There's something almost romantic about typing in a terminal. No distracting sidebars, no update notifications popping up, no "helpful" AI assistants trying to autocomplete your thoughts before you've finished them. Just you, the text, and a cursor that blinks with patience.

I didn't start here. Like many, I began with VS Code, then JetBrains IDEs, then back to VS Code with a million extensions. Each switch promised productivity. Each delivered... more complexity. More RAM usage. More "wait, why is indexing taking 5 minutes?"

Then I watched a colleague edit a Kubernetes YAML file in vim — no, _neovim_ — at 3x my speed. No mouse. No menus. Just muscle memory and intent. That was the moment I thought: _maybe the step backward is actually the leap forward._

---

## The Neovim difference

Neovim isn't just "vim but newer." It's vim reimagined for the modern era:

- **Lua configuration** — goodbye Vimscript, hello actual programming language
- **Built-in LSP client** — first-class language server support out of the box
- **Treesitter integration** — real syntax understanding, not just regex highlighting
- **Remote plugin architecture** — plugins run in separate processes, no more freezing the editor
- **Active development** — nightly releases, responsive maintainers, LuaJIT speed

The learning curve is real. I won't sugarcoat it. Your first week will feel slow. Your fingers will rebel. You'll accidentally open 5 buffers and not know how to close them. But then — something clicks. The modal editing model stops being a puzzle and starts being an extension of your thought process.

---

## My current setup (the "stars" of the show)

After months of tweaking, here's what makes my daily driver sing:

### Plugin manager: `lazy.nvim`

Fast, declarative, with a gorgeous startup dashboard. Specifies plugins as a Lua table, handles dependencies, and only loads what's needed when it's needed.

```lua
-- lazy.nvim bootstrap
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({ "git", "clone", "--filter=blob:none", "https://github.com/folke/lazy.nvim.git", lazypath })
end
vim.opt.rtp:prepend(lazypath)
```

### Fuzzy finding: `telescope.nvim`

The command palette on steroids. Files, buffers, git history, LSP symbols, live grep — all with the same fuzzy matching muscle memory.

```lua
{ "nvim-telescope/telescope.nvim", dependencies = { "nvim-lua/plenary.nvim" } }
```

### Syntax & parsing: `nvim-treesitter`

Real AST parsing. Better highlighting, smarter text objects (select "function", "class", "comment"), and incremental selection that actually understands code structure.

```lua
{ "nvim-treesitter/nvim-treesitter", build = ":TSUpdate" }
```

### LSP & completion: `mason.nvim` + `nvim-lspconfig` + `blink.cmp`

Mason installs language servers. LSPConfig configures them. Blink.cmp (the newer, faster completion engine) handles suggestions. Together: IDE-level intelligence without the IDE bloat.

```lua
{ "williamboman/mason.nvim", config = true },
{ "neovim/nvim-lspconfig" },
{ "saghen/blink.cmp", version = "*" }
```

### Git integration: `gitsigns.nvim` + `fugitive.vim`

Inline git blame, hunk staging, diff view — all without leaving the editor. Fugitive for the heavy lifting (rebase, merge, push), gitsigns for the daily glance.

### Statusline: `lualine.nvim`

Clean, configurable, shows mode, filename, git branch, diagnostics, LSP status, file encoding — exactly what I need, nothing I don't.

### Theme: `catppuccin` (mocha variant)

Warm, readable, consistent across terminal and GUI. The kind of theme you stop noticing because it just _works_.

---

## The Hugo workflow: where it all comes together

This post? Written in neovim. Published via Hugo. The friction is near zero.

### Front matter? Handled.

A quick snippet (I use `luasnip`):

```lua
s("hugo", fmt([[
+++
date = {}
draft = true
title = '{}'
author = 'Abbas Endari'
description = '{}'
thumbnail = '{}'
+++
]], { f(os.date, "%Y-%m-%d"), i(1), i(2), i(3) }))
```

Type `hugo<Tab>`, fill the fields, done.

### Markdown editing? Delightful.

- `treesitter` gives me proper heading folding
- `markdown-preview.nvim` shows live render in browser (`:MarkdownPreview`)
- `vim-markdown` handles table formatting, TOC generation, checkbox toggling
- Custom keymap: `<leader>ml` inserts a link with clipboard URL automatically

### Images? Drag and drop.

A small autocmd watches my content folder — paste an image in the terminal (via `imgclip` or OSC 52), it saves to `static/img/`, inserts the correct Hugo path. No manual `mv` commands.

### Preview & deploy?

```bash
# Terminal 1 (tmux pane): hugo server -D
# Terminal 2 (neovim): write, save, see live reload
# Deploy: git push origin main → GitHub Actions builds & deploys
```

The loop is tight. Write → Save → Browser updates → Commit → Live. No GUI clicking. No context switching.

---

## What this enables (beyond blogging)

The same setup that makes blogging pleasant makes _everything_ pleasant:

- **Python/Go/Rust development** — LSP gives jump-to-def, hover docs, refactor across files
- **Kubernetes/Docker** — YAML LSP catches invalid manifests before `kubectl apply`
- **Quick scripts** — Open terminal, `nvim script.py`, write, run, done
- **Config files** — Dotfiles, SSH configs, systemd units — all with syntax awareness
- **Reading code** — Telescope + LSP = "show me all callers of this function" in 2 keystrokes

The editor becomes a _thinking tool_, not just a typing tool.

---

## The philosophy: invest once, compound forever

Here's the thing about neovim: the configuration _is_ the product.

Every hour you spend learning a keymap, writing a snippet, tuning a plugin — that hour pays dividends every single day after. Your config grows _with_ you. It encodes your workflow, your quirks, your preferences. No UI designer at Microsoft or JetBrains decides what's best for you. _You_ do.

And because it's plain Lua files in `~/.config/nvim/`, it's:

- Version controlled (my dotfiles repo)
- Portable (works on Linux, macOS, WSL, remote SSH via `nvim -c "lua require('lazy').sync()"`)
- Shareable (steal snippets from others, share yours)
- Auditable (no telemetry, no hidden state)

---

## What's next in this series

This post is the "why" and the "what." The upcoming posts will be the "how":

1. **From zero to configured** — bootstrapping `lazy.nvim`, essential settings, keymaps that matter
2. **LSP deep dive** — `mason`, `lspconfig`, `blink.cmp`, diagnostic UX, inlay hints
3. **Treesitter & text objects** — selecting "inside function," "around class," swapping parameters
4. **Telescope workflows** — custom pickers, live grep args, file browser, project switching
5. **Git superpowers** — `gitsigns` hunk operations, `fugitive` for rebase/merge, `diffview.nvim`
6. **Hugo-specific tooling** — front matter snippets, image handling, shortcodes, preview automation
7. **Theming & polish** — statusline, winbar, notifications, which-key, animation

Each post will be practical: config snippets you can copy, explanations of _why_ not just _what_, and the small details that make the difference between "it works" and "it feels like mine."

---

## Your turn

If you've read this far, you're either already a convert or vim-curious. Here's my challenge:

**Try it for 30 days.** Not "open it once a week." Daily driver. Force yourself through the dip. Remap Caps Lock to Escape. Print a cheatsheet. Watch ThePrimeagen or TJ DeVries on YouTube. Join `/r/neovim` or the Discord.

The first two weeks are awkward. Week three is "okay, I see it." Week four is "how did I ever work without this?"

And if you hate it? You learned modal editing, Lua basics, and how LSP works — all transferable. But I'd bet my mechanical keyboard you won't go back.

---

_This post was written in Neovim 0.10, rendered by Hugo 0.120, deployed via GitHub Actions. Config at [github.com/abbasendari/dotfiles](https://github.com/abbasendari/dotfiles) (shameless plug — PRs welcome)._

_Next in series: "From Zero to Configured — Bootstrapping Your Neovim Journey"_
