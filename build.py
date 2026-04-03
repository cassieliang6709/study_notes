#!/usr/bin/env python3
"""
Simple static site builder for study_notes.
Converts all .md files to .html using the same layout/CSS as the Jekyll setup.
Output goes to _site/.
"""

import os
import re
import shutil
import sys
from pathlib import Path
import markdown as md

# ── Config ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.resolve()
SITE_DIR = ROOT / "_site"
ASSETS_SRC = ROOT / "assets"
ASSETS_DST = SITE_DIR / "assets"

SITE_TITLE = "Study Notes"
SITE_DESC = "Personal study notes for algorithms, Python, OOD, and interview practice"

EXCLUDE_DIRS = {"_site", "vendor", ".jekyll-cache", ".sass-cache", ".git",
                "resources", ".claude", ".bundle",
                ".obsidian", "_layouts", "assets", ".vercel"}
EXCLUDE_FILES = {"Gemfile", "Gemfile.lock", "vercel.json", "README.md",
                 "build.py", "_config.yml"}

NAV_ITEMS = [
    ("Home",        "/"),
    ("Algorithms",  "/algorithms/"),
    ("Extended",    "/algorithms/extended_problem_detailed/"),
    ("BQ Prep",     "/bq_prep/"),
    ("Python",      "/python/"),
    ("OOD",         "/ood/"),
    ("Books",       "/books/"),
    ("Resources",   "/resources/"),
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def strip_frontmatter(text):
    """Return (meta_dict, body) after stripping YAML frontmatter."""
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            front = text[3:end].strip()
            body = text[end + 4:].lstrip("\n")
            for line in front.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip().lower()] = v.strip()
            return meta, body
    return meta, text


def get_excerpt(html, length=160):
    """Extract plain-text excerpt from rendered HTML."""
    plain = re.sub(r"<[^>]+>", "", html)
    plain = " ".join(plain.split())
    return plain[:length] + ("…" if len(plain) > length else "")


def rel_url(path, page_url):
    """Return a relative URL from page_url to path (both absolute from site root)."""
    page_parts = page_url.rstrip("/").split("/")
    depth = len(page_parts) - 1
    prefix = "../" * depth if depth > 0 else ""
    return prefix + path.lstrip("/")


def active_class(page_url, nav_href):
    if nav_href == "/" and page_url in ("/", "/index.html"):
        return " is-active"
    if nav_href != "/" and page_url.startswith(nav_href):
        return " is-active"
    return ""


def build_nav(page_url):
    items = []
    for label, href in NAV_ITEMS:
        cls = active_class(page_url, href)
        items.append(f'<a href="{rel_url(href, page_url)}"{cls}>{label}</a>')
    return "\n".join(items)


def build_quick_links(page_url):
    links = [
        ("Pattern Roadmap",  "/algorithms/extended_problem_patterns_cn.html"),
        ("LeetCode Detailed", "/algorithms/leetcode_100_detailed/"),
        ("Extended Problems", "/algorithms/extended_problem_detailed/"),
        ("OOD Cases",        "/ood/ood_cases/"),
        ("Books",            "/books/"),
        ("GitHub Repo",      "https://github.com/cassieliang6709/study_notes"),
    ]
    return "\n".join(
        f'<a href="{rel_url(h, page_url) if not h.startswith("http") else h}">{l}</a>'
        for l, h in links
    )


# ── CSS (strip Jekyll frontmatter) ────────────────────────────────────────────

def get_css():
    css_path = ASSETS_SRC / "css" / "style.css"
    raw = css_path.read_text(encoding="utf-8")
    _, body = strip_frontmatter(raw)
    return body


# ── Layout ────────────────────────────────────────────────────────────────────

def render_layout(page_url, page_title, page_excerpt, content, inline_css):
    is_home = page_url in ("/", "/index.html")
    body_class = "page-home" if is_home else "page-doc"
    banner_kicker = "Learning Workspace" if is_home else "Knowledge Page"
    banner_title = SITE_TITLE if is_home else (page_title or SITE_TITLE)
    banner_text = (
        "一个更有节奏感的学习入口，把笔记、题单和练习放进同一个可快速切换的工作台。"
        if is_home
        else (page_excerpt or SITE_DESC)
    )

    nav_html = build_nav(page_url)
    quick_html = build_quick_links(page_url)
    assets_prefix = rel_url("/assets", page_url)

    return f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{(page_title + " | ") if page_title else ""}{SITE_TITLE}</title>
    <meta name="description" content="{page_excerpt or SITE_DESC}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="{assets_prefix}/css/style.css" />
  </head>
  <body class="{body_class}">
    <a id="top"></a>
    <div class="page-aurora" aria-hidden="true">
      <span class="aurora aurora-one"></span>
      <span class="aurora aurora-two"></span>
      <span class="aurora aurora-three"></span>
    </div>
    <div class="page-shell">
      <main class="content-frame">
        <div class="site-layout">
          <aside class="toc-panel" id="toc-panel" hidden>
            <div class="toc-card">
              <p class="toc-kicker">Quick Map</p>
              <nav id="toc-nav" aria-label="Table of contents"></nav>
            </div>
          </aside>
          <div class="main-column">
            <header class="page-banner">
              <div class="page-banner-copy">
                <p class="page-banner-kicker">{banner_kicker}</p>
                <h1 class="page-banner-title">{banner_title}</h1>
                <p class="page-banner-text">{banner_text}</p>
              </div>
              <div class="page-banner-meta">
                <span>Readable layout</span>
                <span>Fast navigation</span>
                <a href="https://github.com/cassieliang6709/study_notes">Repository</a>
              </div>
            </header>
            <article class="content-card" id="article-content">
              {content}
            </article>
          </div>
          <aside class="site-rail">
            <section class="rail-card rail-brand">
              <a class="brand" href="{rel_url("/", page_url)}">
                <span class="brand-kicker">Cassie Liang</span>
                <span class="brand-title">{SITE_TITLE}</span>
              </a>
              <p class="site-tagline">{SITE_DESC}</p>
              <div class="rail-badges">
                <span class="rail-badge badge-focus">Focus</span>
                <span class="rail-badge badge-notes">Notes</span>
                <span class="rail-badge badge-practice">Practice</span>
              </div>
            </section>
            <section class="rail-card">
              <p class="rail-label">Main Navigation</p>
              <nav class="site-nav" aria-label="Primary">
                {nav_html}
              </nav>
            </section>
            <section class="rail-card rail-secondary">
              <p class="rail-label">Quick Access</p>
              <nav class="rail-links" aria-label="Quick links">
                {quick_html}
              </nav>
            </section>
          </aside>
        </div>
      </main>
      <footer class="site-footer">
        <span>Built with Python · {SITE_TITLE}</span>
        <a href="https://github.com/cassieliang6709/study_notes">View Repository</a>
      </footer>
    </div>
    <a class="back-to-top" href="#top" aria-label="Back to top">Top</a>
    <script src="{assets_prefix}/js/site.js"></script>
  </body>
</html>"""


# ── Directory index ────────────────────────────────────────────────────────────

def build_dir_index(dir_path, page_url, rel_path):
    """Build a simple index.html listing for directories that have no index.md."""
    name = dir_path.name
    title = name.replace("_", " ").title()

    md_files = sorted(dir_path.glob("*.md"))
    subdirs = sorted(d for d in dir_path.iterdir() if d.is_dir()
                     and d.name not in EXCLUDE_DIRS)

    items = []
    for f in md_files:
        if f.name == "index.md":
            continue
        stem = f.stem
        label = stem.replace("_", " ").replace("-", " ")
        items.append(f'<li><a href="{stem}.html">{label}</a></li>')
    for d in subdirs:
        items.append(f'<li><a href="{d.name}/">{d.name.replace("_", " ").title()}</a></li>')

    content = f"<h1>{title}</h1>\n<ul>\n" + "\n".join(items) + "\n</ul>"
    return render_layout(page_url, title, title, content, "")


# ── Markdown converter ────────────────────────────────────────────────────────

EXTENSIONS = [
    "markdown.extensions.fenced_code",
    "markdown.extensions.tables",
    "markdown.extensions.toc",
    "markdown.extensions.nl2br",
    "markdown.extensions.sane_lists",
    "markdown.extensions.attr_list",
]

def convert_md(text):
    return md.markdown(text, extensions=EXTENSIONS)


# ── Build ─────────────────────────────────────────────────────────────────────

def should_exclude(path):
    parts = set(path.parts)
    return bool(parts & EXCLUDE_DIRS)


def process_md_file(src_path, dst_path, page_url):
    raw = src_path.read_text(encoding="utf-8")
    meta, body = strip_frontmatter(raw)
    html_content = convert_md(body)
    excerpt = get_excerpt(html_content)
    page_title = meta.get("title", src_path.stem.replace("_", " ").replace("-", " ").title())
    page_html = render_layout(page_url, page_title, excerpt, html_content, "")
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text(page_html, encoding="utf-8")


def build():
    # Clean and recreate _site
    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    SITE_DIR.mkdir(parents=True)

    # Copy assets (strip frontmatter from style.css)
    ASSETS_DST.mkdir(parents=True)
    css_dst = ASSETS_DST / "css"
    css_dst.mkdir(parents=True)
    (css_dst / "style.css").write_text(get_css(), encoding="utf-8")

    js_dst = ASSETS_DST / "js"
    js_dst.mkdir(parents=True)
    js_src = ASSETS_SRC / "js" / "site.js"
    if js_src.exists():
        shutil.copy2(js_src, js_dst / "site.js")

    count = 0

    # Walk source tree
    for root, dirs, files in os.walk(ROOT):
        root_path = Path(root)
        rel = root_path.relative_to(ROOT)

        # Prune excluded dirs in-place
        dirs[:] = [d for d in sorted(dirs) if d not in EXCLUDE_DIRS]

        # Skip excluded paths
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue

        for fname in sorted(files):
            if fname in EXCLUDE_FILES:
                continue
            if not fname.endswith(".md"):
                continue

            src = root_path / fname
            rel_file = rel / fname

            if fname == "index.md":
                # index.md → <dir>/index.html
                rel_html = rel / "index.html"
                page_url = "/" + str(rel).replace("\\", "/") + "/"
                if str(rel) == ".":
                    page_url = "/"
            else:
                stem = Path(fname).stem
                rel_html = rel / (stem + ".html")
                page_url = "/" + str(rel_html).replace("\\", "/")

            dst = SITE_DIR / rel_html
            print(f"  {rel_file}  →  {rel_html}")
            process_md_file(src, dst, page_url)
            count += 1

        # Generate index.html for dirs that have no index.md
        if str(rel) != "." and not (root_path / "index.md").exists():
            dst_index = SITE_DIR / rel / "index.html"
            if not dst_index.exists():
                page_url = "/" + str(rel).replace("\\", "/") + "/"
                dst_index.parent.mkdir(parents=True, exist_ok=True)
                dst_index.write_text(build_dir_index(root_path, page_url, rel), encoding="utf-8")
                print(f"  [auto-index] {rel}/index.html")

    print(f"\nDone. Built {count} pages → {SITE_DIR}")


if __name__ == "__main__":
    build()
