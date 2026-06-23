# Jedson Pinto — Personal Website

A single-page academic homepage for **Jedson Pinto** (Assistant Professor of Accounting, UT Dallas),
hosted on **GitHub Pages**.

**Live:** https://jedsonn.github.io/jedson_website/

---

## What's here

| File | Purpose |
|------|---------|
| `index.html` | The entire site — a clean, hand-editable static page (HTML + CSS + a little JS). **Edit this.** |
| `photo.jpg` | The hero headshot (200×250 display, any portrait-ish image works). |
| `.nojekyll` | Tells GitHub Pages to serve the files as-is (no Jekyll build). |
| `src/` | The **original** authoring-tool source (`.dc.html` + `support.js`). Kept for reference only — not used by the live site. |

> Note: the site was originally delivered as a self-extracting "bundle" `index.html`. That version
> rendered empty paper cards in the browser, so it was rebuilt as the plain static page you see now.
> Everything (papers, links, badges, bio, the theme-filter behavior) is reproduced 1:1 and is now easy to edit.

---

## How to edit

Open `index.html`. Almost everything you'll want to change lives in two obvious places.

### 1. Papers — edit the `DATA` object (near the bottom, inside `<script>`)

There are four arrays: `wp` (Working Papers), `wip` (Work in Progress), `pub` (Publications),
`other` (Other Publications). Each paper is one object:

```js
{ title:"Paper title",
  url:"https://…",                          // optional — makes the title a link
  coauthors:[
    { name:"Coauthor Name", url:"https://…", mark:"++" }   // url & mark optional
  ],
  journal:"Accepted, Journal of …",          // optional (publications)
  status:"conditionally",                    // optional → renders the journal in amber
  badges:["FT50","UTD24","FT50#"],           // optional; FT50# = FT50 with a superscript #
  tldr:"One-line summary shown when the card is expanded.",
  tags:["Disclosure & Information Production","Capital Markets","ML/AI & Text"],
  link:{ url:"https://…", label:"data site" }  // optional extra link in the expanded card
}
```

- **Coauthor marks:** `"*"` (corresponding author), `"+"` (untenured at project start),
  `"++"` (PhD student at project start), or combinations like `"+,*"`.
- **Themes / filtering:** the three filterable themes are exactly these tag strings —
  `"Disclosure & Information Production"`, `"Capital Markets"`, `"ML/AI & Text"`.
  A paper appears under a theme if that string is in its `tags`. The theme counts in the filter
  bar update automatically.
- To add a paper, copy an existing object in the right array. To remove one, delete it. That's it.

### 2. Bio, name, nav, links

These are plain HTML near the top of `index.html` (the `<nav>`, `.hero`, `.strip`, and `.callout`
sections). Edit the text directly.

### Change the photo

Replace `photo.jpg` with your image (keep the same filename, or update the `<img class="photo" src="…">`).
A portrait crop around 200×250 looks best; the CSS does `object-fit: cover` so other sizes still work.

---

## Behavior (already implemented)

- Clicking a **theme** — in the filter bar, the research statement, or any card's tag — filters every
  section to papers with that tag, renumbers them, and shows a "Showing X of N…" line. Click again or
  **Clear** to reset. Non-active statement themes dim.
- Each **card** expands to show its TL;DR + tags. **Section headers** collapse their list.
  **Expand all / Collapse all** act on every card.
- **Other Publications** hide while a filter is active.
- Journal **badges**: `FT50` / `UTD24` / `FT50#`. Coauthor marks and the footnote legend are at the bottom.

---

## Design tokens (if you restyle)

- Background `#fafaf8`, surface `#fff`, text `#2c2a25`, secondary `#6b6860`, muted `#9a958c`, borders `#e8e6e1`.
- Accent `#1a5276` (links / active filter) + light `#eaf2f8`. Working-paper accent `#5b21b6` / light `#f3f0ff`.
- Published journal text green `#2e7d32`; conditional/amber `#b45309`.
- Fonts: **Source Serif 4** (titles/headings), **Source Sans 3** (body). Content column max-width **820px**.

All of these are CSS variables in `:root` at the top of `index.html`.

---

## Deploy / hosting

The site is already live from the `main` branch via GitHub Pages
(**Settings → Pages → Deploy from a branch → `main` / `root`**). Any push to `main` redeploys
automatically within ~1 minute.

### Custom domain (jedsonpinto.com)
- **Settings → Pages → Custom domain** → enter `jedsonpinto.com`.
- At your DNS registrar add GitHub Pages' four `A` records (`185.199.108–111.153`) and a `CNAME` for
  `www` → `jedsonn.github.io`. GitHub shows the exact values.
