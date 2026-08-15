#region Imports
from __future__ import annotations
import asyncio
import json
import os
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlparse

from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlResult, CrawlerRunConfig, LLMExtractionStrategy, LLMConfig
from config import OPENROUTER_API_KEY
#endregion

#region Configuration
@dataclass(frozen=True)
class CrawlerConfig:
    """Configuration for documentation scraping."""
    max_depth: int = 3
    max_concurrency: int = 30
    css_selector: str = "article"
    llm_provider: str = "openrouter/deepseek/deepseek-v4-flash-0731"
    provider_routing: list[str] = field(default_factory=lambda: ["Decart"])
    output_filename: str = "1.scrape.json"
#endregion

#region Data Models
class PageSummary(BaseModel):
    """Schema for structured LLM extraction from documentation pages."""
    summary: str = Field(description="Summary of the documentation page covering concepts, APIs, and best practices.")
    keywords: list[str] = Field(description="Key technical topics and keywords (3 to 5 items).")
    links: dict[str, str] = Field(default_factory=dict, description="Mapping of link description to target URL found on page.")


class DocumentNode(BaseModel):
    """Hierarchical node representing a scraped page and nested child pages."""
    url: str
    title: str
    depth_level: int
    summary: str = ""
    keywords: list[str] = Field(default_factory=list)
    markdown_content: str = ""
    sub_documents: list[DocumentNode] = Field(default_factory=list)
#endregion

#region Helpers
def normalize_url(url: str) -> str:
    """Strips anchors and whitespace from URL."""
    return url.split("#")[0].strip()


def extract_section_prefix(url: str) -> str:
    """Extracts top directory prefix from URL."""
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    if len(parts) >= 3:
        return f"{parsed.scheme}://{parsed.netloc}/{'/'.join(parts[:3])}/"
    return url.rsplit("/", 1)[0] + "/"


def derive_page_title(result: CrawlResult, url: str) -> str:
    """Extracts clean page title from metadata, markdown headers, or URL."""
    meta_title = (result.metadata or {}).get("title", "").strip()
    if meta_title:
        return meta_title
    if result.markdown:
        lines = [line.strip() for line in result.markdown.splitlines() if line.strip()]
        if lines and lines[0].startswith("#"):
            return lines[0].replace("#", "").split("[¶]")[0].strip()
    slug = url.rstrip("/").split("/")[-1].replace(".html", "").replace("-", " ")
    return slug.title() if slug else "Documentation Page"


def parse_extracted_metadata(content: str | None) -> tuple[str, list[str], dict[str, str]]:
    """Extracts summary, keywords, and links from LLM extraction result."""
    if not content:
        return "", [], {}
    try:
        data = json.loads(content)
        if isinstance(data, list) and data:
            data = data[0]
        if isinstance(data, dict):
            return data.get("summary", ""), data.get("keywords", []), data.get("links", {})
    except (json.JSONDecodeError, TypeError):
        pass
    return "", [], {}
#endregion

#region Crawler
class DocTreeCrawler:
    """Recursively crawls documentation trees concurrently with bounded depth."""

    def __init__(self, root_urls: list[str], config: CrawlerConfig | None = None):
        self.config = config or CrawlerConfig()
        self.root_urls = [normalize_url(u) for u in root_urls]
        self.semaphore = asyncio.Semaphore(self.config.max_concurrency)
        self.visited: set[str] = set()
        self.lock = asyncio.Lock()
        self.prefixes = [extract_section_prefix(u) for u in self.root_urls]
        self.run_config = CrawlerRunConfig(
            css_selector=self.config.css_selector,
            extraction_strategy=LLMExtractionStrategy(
                llm_config=LLMConfig(provider=self.config.llm_provider, api_token=OPENROUTER_API_KEY),
                schema=PageSummary.model_json_schema(),
                extraction_type="schema",
                instruction="Extract page summary, keywords, and internal links. Output valid JSON only.",
                extra_args={
                    "response_format": {"type": "json_object"},
                    "extra_body": {"provider": {"order": self.config.provider_routing, "allow_fallbacks": True}}
                },
                force_json_response=True
            )
        )

    def is_allowed(self, url: str) -> bool:
        return any(url.startswith(prefix) for prefix in self.prefixes)

    async def crawl_node(self, crawler: AsyncWebCrawler, url: str, depth: int = 1) -> DocumentNode | None:
        url = normalize_url(url)
        if not self.is_allowed(url):
            return None

        async with self.lock:
            if url in self.visited:
                return None
            self.visited.add(url)

        indent = "  " * (depth - 1)
        print(f"{indent}[Depth {depth}/{self.config.max_depth}] Crawling: {url}")

        async with self.semaphore:
            try:
                res: CrawlResult = await crawler.arun(url=url, config=self.run_config)
                if not res.success:
                    return None
                summary, keywords, links = parse_extracted_metadata(res.extracted_content)
                node = DocumentNode(
                    url=url,
                    title=derive_page_title(res, url),
                    depth_level=depth,
                    summary=summary,
                    keywords=keywords,
                    markdown_content=res.markdown or ""
                )
            except Exception as e:
                print(f"{indent}Error crawling {url}: {e}")
                return None

        if depth < self.config.max_depth and links:
            child_urls = [normalize_url(urljoin(url, target)) for target in links.values()]
            tasks = [self.crawl_node(crawler, u, depth + 1) for u in child_urls if self.is_allowed(u)]
            children = await asyncio.gather(*tasks)
            node.sub_documents = [c for c in children if c is not None]

        return node

    async def crawl_all(self, crawler: AsyncWebCrawler) -> list[DocumentNode]:
        tasks = [self.crawl_node(crawler, u, depth=1) for u in self.root_urls]
        results = await asyncio.gather(*tasks)
        return [node for node in results if node is not None]
#endregion

#region Main
async def main() -> None:
    root_urls = [
        "https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html",
        "https://docs.kanzi.com/4.1.0/en/working-with/working-with.html",
        "https://docs.kanzi.com/4.1.0/en/best-practices/best-practices.html"
    ]
    config = CrawlerConfig()
    crawler_engine = DocTreeCrawler(root_urls=root_urls, config=config)

    print(f"[Crawler] Starting concurrent doc scraping ({len(root_urls)} root sections)...")
    async with AsyncWebCrawler() as crawler:
        forest = await crawler_engine.crawl_all(crawler=crawler)

    out_file = Path(__file__).resolve().parent / config.output_filename
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump([n.model_dump() for n in forest], f, ensure_ascii=False, indent=2)

    print(f"[Crawler] Completed: saved {len(forest)} trees ({len(crawler_engine.visited)} pages) to {out_file.name}")


if __name__ == "__main__":
    asyncio.run(main())
#endregion
