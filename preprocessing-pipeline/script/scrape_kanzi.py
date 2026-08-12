"""
Kanzi Framework 4.1.0 Documentation Scraper
Recursively scrapes all pages from https://docs.kanzi.com/4.1.0/en/
and saves them as Markdown files preserving the directory structure.
"""

import json
import os
import re
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests

# ─────────────────────────────────────────────
# region Configuration
# ─────────────────────────────────────────────

BASE_URL = "https://docs.kanzi.com/4.1.0/en/"
START_URL = "https://docs.kanzi.com/4.1.0/en/overview.html"
OUTPUT_DIR = Path(__file__).parent / "kanzi_docs"
REQUEST_DELAY = 0.3          # seconds between requests (be polite)
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# endregion

# ─────────────────────────────────────────────
# region ANSI Logging Helpers
# ─────────────────────────────────────────────

CYAN   = "\033[1;96m"
GREEN  = "\033[1;92m"
YELLOW = "\033[1;93m"
RED    = "\033[1;91m"
RESET  = "\033[0m"

SCRIPT_NAME = os.path.basename(__file__)


def log_step(index: str, total: str, message: str) -> None:
    print(f"\n{CYAN}========================================================{RESET}")
    print(f"{GREEN}>>> [{index}/{total}] [{SCRIPT_NAME}] {message}{RESET}")
    print(f"{CYAN}========================================================{RESET}\n")


def log_info(msg: str) -> None:
    print(f"  {GREEN}ok  {msg}{RESET}")


def log_warn(msg: str) -> None:
    print(f"  {YELLOW}!! {msg}{RESET}")


def log_error(msg: str) -> None:
    print(f"  {RED}xx  {msg}{RESET}")

# endregion

# ─────────────────────────────────────────────
# region HTML to Markdown Converter
# ─────────────────────────────────────────────

class SimpleHTMLToMarkdown(HTMLParser):
    """Lightweight HTML-to-Markdown converter focused on article content."""

    def __init__(self):
        super().__init__()
        self.result: list = []
        self._in_content = False
        self._skip_depth = 0
        self._tag_stack: list = []
        self._list_stack: list = []
        self._ol_counters: list = []
        self._in_code = False
        self._in_pre = False
        self._skip_tags = {
            "script", "style", "svg", "noscript", "form",
            "nav", "header", "footer", "aside", "input",
            "label", "button", "select", "option",
        }
        self._content_tags = {"article", "main"}
        self._pending_href = None
        self._link_text: list = []
        self._in_link = False
        self._title = ""
        self._in_title = False

    def _write(self, text: str) -> None:
        if self._in_content and self._skip_depth == 0:
            self.result.append(text)

    def handle_starttag(self, tag: str, attrs: list) -> None:
        attr_dict = dict(attrs)
        self._tag_stack.append(tag)

        if tag == "title":
            self._in_title = True
            return

        if tag in self._content_tags:
            self._in_content = True
            return

        if not self._in_content:
            return

        if tag in self._skip_tags:
            self._skip_depth += 1
            return

        if self._skip_depth > 0:
            return

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self._write("\n" + "#" * level + " ")
        elif tag == "p":
            self._write("\n\n")
        elif tag in ("strong", "b"):
            self._write("**")
        elif tag in ("em", "i"):
            self._write("*")
        elif tag == "code":
            if not self._in_pre:
                self._write("`")
            self._in_code = True
        elif tag == "pre":
            self._in_pre = True
            cls = attr_dict.get("class", "")
            m = re.search(r"highlight-(\w+)", cls)
            lang = m.group(1) if m else ""
            self._write(f"\n\n```{lang}\n")
        elif tag == "a":
            href = attr_dict.get("href", "")
            if href and not href.startswith("#"):
                self._pending_href = href
                self._in_link = True
                self._link_text = []
                self._write("[")
        elif tag == "ul":
            self._list_stack.append("ul")
            self._write("\n")
        elif tag == "ol":
            self._list_stack.append("ol")
            self._ol_counters.append(0)
            self._write("\n")
        elif tag == "li":
            if self._list_stack:
                kind = self._list_stack[-1]
                indent = "  " * (len(self._list_stack) - 1)
                if kind == "ul":
                    self._write(f"\n{indent}- ")
                else:
                    self._ol_counters[-1] += 1
                    n = self._ol_counters[-1]
                    self._write(f"\n{indent}{n}. ")
        elif tag == "blockquote":
            self._write("\n> ")
        elif tag == "tr":
            self._write("\n|")
        elif tag in ("th", "td"):
            self._write(" ")
        elif tag == "hr":
            self._write("\n\n---\n\n")
        elif tag == "br":
            self._write("  \n")
        elif tag == "img":
            alt = attr_dict.get("alt", "image")
            src = attr_dict.get("src", "")
            self._write(f"![{alt}]({src})")

    def handle_endtag(self, tag: str) -> None:
        if self._tag_stack and self._tag_stack[-1] == tag:
            self._tag_stack.pop()

        if tag == "title":
            self._in_title = False
            return

        if tag in self._content_tags:
            self._in_content = False
            return

        if tag in self._skip_tags:
            if self._skip_depth > 0:
                self._skip_depth -= 1
            return

        if self._skip_depth > 0:
            return

        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._write("\n")
        elif tag in ("strong", "b"):
            self._write("**")
        elif tag in ("em", "i"):
            self._write("*")
        elif tag == "code":
            self._in_code = False
            if not self._in_pre:
                self._write("`")
        elif tag == "pre":
            self._in_pre = False
            self._in_code = False
            self._write("\n```\n")
        elif tag == "a":
            if self._pending_href and self._in_link:
                self._write(f"]({self._pending_href})")
                self._pending_href = None
                self._in_link = False
                self._link_text = []
        elif tag == "ul":
            if self._list_stack:
                self._list_stack.pop()
            self._write("\n")
        elif tag == "ol":
            if self._list_stack:
                self._list_stack.pop()
            if self._ol_counters:
                self._ol_counters.pop()
            self._write("\n")
        elif tag in ("th", "td"):
            self._write(" |")

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title += data
            return

        if not self._in_content or self._skip_depth > 0:
            return

        if self._in_link:
            self._link_text.append(data)

        text = data
        if not self._in_pre and not self._in_code:
            text = re.sub(r"\s+", " ", text)

        self._write(text)

    def get_markdown(self) -> str:
        return "".join(self.result).strip()

    def get_title(self) -> str:
        return self._title.strip()


def html_to_markdown(html: str, page_url: str):
    """Convert HTML to Markdown. Returns (title, markdown_content)."""
    parser = SimpleHTMLToMarkdown()
    parser.feed(html)
    title = parser.get_title()
    md = parser.get_markdown()
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    header = f"---\ntitle: {title}\nsource: {page_url}\n---\n\n"
    return title, header + md

# endregion

# ─────────────────────────────────────────────
# region Link Extractor
# ─────────────────────────────────────────────

def extract_sidebar_links(html: str, base_url: str) -> list:
    """Extract all toctree links from the sidebar."""
    pattern = re.compile(
        r'class="[^"]*toctree-l\d+[^"]*"[^>]*>\\s*<a[^>]+href="([^"#][^"]*)"',
        re.DOTALL,
    )
    # Alternative: grab all <a href> inside li.toctree-* items
    all_hrefs = re.findall(
        r'<li class="toctree-l[^"]*"[^>]*>.*?<a[^>]+href="([^"#][^"]*\.html)"',
        html,
        re.DOTALL,
    )
    links: list = []
    seen: set = set()
    for href in all_hrefs:
        if href.startswith("http"):
            abs_url = href
        else:
            abs_url = urljoin(base_url, href)
        abs_url = abs_url.split("#")[0]
        parsed = urlparse(abs_url)
        if "docs.kanzi.com" not in parsed.netloc:
            continue
        if "/4.1.0/" not in parsed.path:
            continue
        if abs_url not in seen:
            seen.add(abs_url)
            links.append(abs_url)
    return links

# endregion

# ─────────────────────────────────────────────
# region HTTP Helpers
# ─────────────────────────────────────────────

def fetch_html(session: requests.Session, url: str):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
            if resp.status_code == 200:
                return resp.text
            elif resp.status_code == 404:
                log_warn(f"404: {url}")
                return None
            else:
                log_warn(f"HTTP {resp.status_code} (attempt {attempt}): {url}")
        except requests.RequestException as exc:
            log_warn(f"Error attempt {attempt}: {exc}")
        if attempt < MAX_RETRIES:
            time.sleep(REQUEST_DELAY * 3)
    return None

# endregion

# ─────────────────────────────────────────────
# region File Path Builder
# ─────────────────────────────────────────────

def url_to_filepath(url: str, output_dir: Path) -> Path:
    """Map a docs URL to a local .md filepath."""
    parsed = urlparse(url)
    path = parsed.path
    prefix = "/4.1.0/en/"
    if path.startswith(prefix):
        rel_path = path[len(prefix):]
    elif "/4.1.0/" in path:
        idx = path.index("/4.1.0/") + len("/4.1.0/")
        rel_path = path[idx:]
    else:
        rel_path = path.lstrip("/")
    rel_path = re.sub(r"\.html?$", ".md", rel_path)
    if not rel_path:
        rel_path = "index.md"
    return output_dir / rel_path

# endregion

# ─────────────────────────────────────────────
# region Main Scraper
# ─────────────────────────────────────────────

def collect_all_urls(session: requests.Session) -> list:
    log_step("1", "4", "Fetching start page and collecting sidebar URLs")
    html = fetch_html(session, START_URL)
    if not html:
        raise RuntimeError(f"Failed to fetch start page: {START_URL}")
    urls = [START_URL] + extract_sidebar_links(html, START_URL)
    log_info(f"Discovered {len(urls)} URLs from sidebar")
    return urls


def scrape_and_save(session: requests.Session, urls: list) -> dict:
    log_step("2", "4", f"Downloading and converting {len(urls)} pages")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stats = {"success": 0, "skipped": 0, "failed": 0, "total": len(urls)}

    for i, url in enumerate(urls, start=1):
        filepath = url_to_filepath(url, OUTPUT_DIR)
        try:
            rel = filepath.relative_to(OUTPUT_DIR)
        except ValueError:
            rel = filepath

        print(f"  [{i:4d}/{len(urls)}] {rel}", end=" ... ", flush=True)

        html = fetch_html(session, url)
        if html is None:
            print(f"{RED}FAILED{RESET}")
            stats["failed"] += 1
            time.sleep(REQUEST_DELAY)
            continue

        title, md = html_to_markdown(html, url)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(md, encoding="utf-8")
        print(f"{GREEN}OK{RESET}  ({len(md):,} chars)")
        stats["success"] += 1
        time.sleep(REQUEST_DELAY)

    return stats


def save_index(urls: list) -> None:
    log_step("3", "4", "Saving URL index (scraped_index.json)")
    index_path = OUTPUT_DIR / "scraped_index.json"
    data = {
        "base_url": BASE_URL,
        "start_url": START_URL,
        "total_pages": len(urls),
        "pages": [
            {
                "url": u,
                "local_path": str(url_to_filepath(u, OUTPUT_DIR).relative_to(OUTPUT_DIR)),
            }
            for u in urls
        ],
    }
    index_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    log_info(f"Index saved: {index_path}")


def print_summary(stats: dict) -> None:
    log_step("4", "4", "Scraping complete")
    log_info(f"Total        : {stats['total']}")
    log_info(f"Success      : {stats['success']}")
    log_warn(f"Failed       : {stats['failed']}")
    log_info(f"Output folder: {OUTPUT_DIR.resolve()}")

# endregion

# ─────────────────────────────────────────────
# region Entry Point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print(f"\n{CYAN}{'='*56}{RESET}")
    print(f"{GREEN}  Kanzi 4.1.0 Documentation Scraper  [{SCRIPT_NAME}]{RESET}")
    print(f"{CYAN}{'='*56}{RESET}\n")

    with requests.Session() as session:
        urls = collect_all_urls(session)
        stats = scrape_and_save(session, urls)
        save_index(urls)
        print_summary(stats)

# endregion
