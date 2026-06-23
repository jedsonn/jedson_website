# Jedson Pinto — Personal Website (Handoff)

This package contains a finished personal/academic website and everything needed to **host it on GitHub Pages** and **keep editing it**.

## TL;DR for Claude Code
1. `index.html` is the entire site in **one self-contained file** (fonts inlined, no build step, works offline). It is ready to deploy as-is.
2. Help the user push it to a GitHub repo and enable **GitHub Pages**.
3. For ongoing content edits (papers, bio, tags), see **"How to edit"** below. Recommended: reimplement as a clean static site so future edits are simple (the current `index.html` is a compiled bundle and is not meant to be hand-edited).

---

## What this is
A single-page academic homepage for Jedson Pinto (Assistant Professor of Accounting, UT Dallas). Features:
- Hero with centered name/title/links, photo placeholder, and bio.
- Research-interests strip + a BridgePHD callout.
- A research statement with **clickable themes** that filter the paper list.
- Collapsible sections — **Working Papers, Work in Progress, Publications, Other Publications** — each paper card expands to show a TL;DR and clickable theme tags.
- **Expand all / Collapse all** controls and a **theme filter bar** (3 themes: *Disclosure & Information Production*, *Capital Markets*, *ML/AI & Text*) with live counts.
- Coauthor markers (`*`, `+`, `++`) and journal badges (`FT50`, `UTD24`, `FT50#`) with a footnote legend.

## Files
- `index.html` — **deployable** self-contained site. This is what goes live.
- `src/Jedson Pinto.dc.html` — editable source (markup + a `class Component` logic block holding all paper data).
- `src/PaperCard.dc.html` — the paper-card sub-template.
- `src/support.js` — the runtime the source files depend on (do not edit).

> The `src/` files use a custom component runtime specific to the authoring tool they were built in. `index.html` is the compiled output of those files. **Outside that tool you cannot re-compile the source**, so for a maintainable long-term setup, prefer the rebuild option below.

---

## Deploy to GitHub Pages
```bash
# in an empty folder
git init
cp /path/to/index.html ./index.html        # filename MUST be index.html
git add index.html
git commit -m "Add personal website"
git branch -M main
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```
Then on GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / `root` → Save.**
Live at `https://<user>.github.io/<repo>/` within ~1 minute.

### Custom domain (jedsonpinto.com)
- **Settings → Pages → Custom domain** → enter `jedsonpinto.com`.
- At the DNS registrar add GitHub Pages' four `A` records (`185.199.108–111.153`) and a `CNAME` for `www` → `<user>.github.io`. GitHub shows exact values.

---

## How to edit

### Quick content tweaks (works on the bundle)
All paper data lives in a JS object array inside the site. Search `index.html` (or `src/Jedson Pinto.dc.html`) for these arrays and edit the entries:
- `wp = [ … ]` — Working Papers
- `wip = [ … ]` — Work in Progress
- `pub = [ … ]` — Publications
- `other = [ … ]` — Other Publications

Each entry looks like:
```js
{ title:"…", url:"https://…",
  coauthors:[{ name:"…", url:"https://…", mark:"++" }],   // mark: "*", "+", "++", "+,*"
  journal:"Accepted, Journal of Business Ethics",
  status:"conditionally",      // optional → amber "Conditionally Accepted" styling
  badges:["FT50","UTD24","FT50#"],   // FT50# renders FT50 with a superscript #
  tldr:"One-line summary.",
  tags:["Disclosure & Information Production","Capital Markets","ML/AI & Text"],
  link:{ url:"https://…", label:"data site" }   // optional extra link
}
```
The three filterable **themes** are exactly those three tag strings — a paper shows under a theme if that string is in its `tags`.

To change the **photo**: replace the placeholder `<div>` (search `headshot.jpg`) with `<img src="photo.jpg" style="width:200px;height:250px;border-radius:6px;object-fit:cover;object-position:center top;">` and commit `photo.jpg` alongside `index.html`.

### Recommended: rebuild as a clean static site
For a maintainable repo, recreate this as a plain `index.html` + `styles.css` + `script.js` (or a small framework). The current design is **high-fidelity** — match it exactly:

**Design tokens**
- Background `#fafaf8`, surface `#fff`, text `#2c2a25`, secondary `#6b6860`, tertiary/muted `#9a958c`, borders `#e8e6e1`.
- Accent (links, active filter, primary pill) `#1a5276`; accent-light `#eaf2f8`.
- Working-paper accent `#5b21b6` / light `#f3f0ff`; published journal text green `#2e7d32`; conditional/amber `#b45309`.
- Tag chip (idle) bg `#f0eeea`, text `#5a5750`, border `#e8e6e1`; (active) accent.
- Badges: FT50 `#fef3c7`/`#b45309`/`#fde68a`; UTD24 `#fee2e2`/`#7b341e`/`#fecaca`; FT50# same as FT50 with superscript `#`.
- Radius 5px cards / 20px pills. Card shadow `0 1px 3px rgba(0,0,0,.04)`.
- Fonts: headings/titles **Source Serif 4** (700/600); body **Source Sans 3** (300–600). Content column max-width **820px**.

**Behavior to preserve**
- Clicking a theme (filter bar, research statement, or a card's tag) filters all sections to papers containing that tag; clicking again or "Clear" resets. Non-active themes in the statement dim to ~0.32 opacity. A "Showing X of N…" line appears while filtered; paper numbers renumber from 1.
- Each card toggles its detail (TL;DR + tags) open/closed. Section headers collapse their whole list. Expand-all / Collapse-all act on all cards.
- Other Publications hide while a filter is active.

All exact copy, paper data, coauthor links, badges, and the footnote legend are in `src/Jedson Pinto.dc.html` — lift them verbatim.

## Fidelity
**High-fidelity.** Recreate pixel-for-pixel using the values above.
