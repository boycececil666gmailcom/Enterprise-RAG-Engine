#region Imports
from __future__ import annotations
import asyncio
import json
import os
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urljoin, urlparse
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlResult, CrawlerRunConfig, LLMExtractionStrategy, LLMConfig
from config import OPENROUTER_API_KEY
#endregion

#region Configuration
@dataclass(frozen=True)
class CrawlerConfig:
    """Centralized configuration parameters for documentation scraping."""
    max_depth: int = 2
    max_concurrency: int = 5
    css_selector: str = "article"
    llm_provider: str = "openrouter/deepseek/deepseek-v4-flash-0731"
    provider_routing: list[str] = field(default_factory=lambda: ["Decart"])
    output_filename: str = "scrape.json"
#endregion

#region Data Models
class PageSummary(BaseModel):
    """Pydantic schema for structured LLM extraction from documentation pages."""
    summary: str = Field(
        description="Summary of the Kanzi framework documentation page covering core concepts, APIs, and best practices."
    )
    keywords: list[str] = Field(
        description="Key technical topics and keywords for this page (around 3 to 5 items)."
    )
    links: dict[str, str] = Field(
        default_factory=dict,
        description="A dictionary mapping a summary/description of what each link leads to (key) to its target URL (value) found on this page."
    )


class DocumentNode(BaseModel):
    """Hierarchical document node representing a scraped page and its nested child pages."""
    url: str
    title: str
    depth_level: int
    summary: str = ""
    keywords: list[str] = Field(default_factory=list)
    markdown_content: str
    sub_documents: list[DocumentNode] = Field(
        default_factory=list,
        description="Child documents recursively scraped and nested inside this parent document."
    )
#endregion

#region URL Helpers
def normalize_url(url: str) -> str:
    """Strips fragment/anchor identifiers and surrounding whitespace from a URL."""
    return url.split('#')[0].strip()


def extract_section_prefix(url: str) -> str:
    """Extracts directory prefix: e.g. https://docs.kanzi.com/4.1.0/en/working-with/"""
    parsed = urlparse(url)
    path_parts = parsed.path.strip("/").split("/")
    if len(path_parts) >= 3:
        section_dir = "/".join(path_parts[:3])
        return f"{parsed.scheme}://{parsed.netloc}/{section_dir}/"
    return url.rsplit("/", 1)[0] + "/"
#endregion

#region Parsing Helpers
def derive_page_title(result: CrawlResult, current_url: str) -> str:
    """Derives a clean page title from metadata, markdown headers, or URL fallback."""
    metadata_title = (result.metadata or {}).get("title", "").strip()
    if metadata_title:
        return metadata_title

    if result.markdown:
        lines = [line.strip() for line in result.markdown.splitlines() if line.strip()]
        if lines and lines[0].startswith("#"):
            return lines[0].replace("#", "").split("[¶]")[0].strip()

    slug = current_url.rstrip("/").split("/")[-1].replace(".html", "").replace("-", " ")
    return slug.title() if slug else "Documentation Page"


def parse_extracted_metadata(content: str | None) -> tuple[str, list[str], dict[str, str]]:
    """Safely extracts summary, keywords, and outbound links from LLM JSON response."""
    if not content:
        return "", [], {}

    try:
        parsed = json.loads(content)
        data = parsed[0] if isinstance(parsed, list) and parsed else parsed
        if not isinstance(data, dict):
            return "", [], {}

        summary = data.get("summary", "")
        keywords = data.get("keywords", []) if isinstance(data.get("keywords"), list) else []
        links = data.get("links", {}) if isinstance(data.get("links"), dict) else {}
        return summary, keywords, links
    except (json.JSONDecodeError, TypeError):
        return "", [], {}
#endregion

#region Crawler Engine
class ConcurrentDocTreeCrawler:
    """Crawls documentation tree recursively and concurrently with bounded depth and rate limits."""

    def __init__(self, root_urls: list[str], config: CrawlerConfig | None = None):
        self.config = config or CrawlerConfig()
        self.root_urls = [normalize_url(u) for u in root_urls]
        self.semaphore = asyncio.Semaphore(self.config.max_concurrency)
        self.visited_urls: set[str] = set()
        self.visited_lock = asyncio.Lock()

        # Derive allowed section prefixes from root URLs
        self.allowed_prefixes: list[str] = [extract_section_prefix(u) for u in self.root_urls]
        self._log_initialization()
        self.run_config = self._build_run_config()

    def _log_initialization(self) -> None:
        print(f"Allowed Section Prefixes ({len(self.allowed_prefixes)}):")
        for prefix in self.allowed_prefixes:
            print(f"  - {prefix}")

    def _build_run_config(self) -> CrawlerRunConfig:
        """Constructs crawl4ai execution configuration with structured LLM extraction."""
        return CrawlerRunConfig(
            css_selector=self.config.css_selector,
            extraction_strategy=LLMExtractionStrategy(
                llm_config=LLMConfig(
                    provider=self.config.llm_provider,
                    api_token=OPENROUTER_API_KEY
                ),
                schema=PageSummary.model_json_schema(),
                extraction_type="schema",
                instruction=(
                    "Extract key concepts, page summary, keywords, and internal links "
                    "from this Kanzi documentation page. Output valid JSON only."
                ),
                extra_args={
                    "response_format": {"type": "json_object"},
                    "extra_body": {
                        "provider": {
                            "order": self.config.provider_routing,
                            "allow_fallbacks": True
                        }
                    }
                },
                force_json_response=True
            )
        )

    def is_allowed_section_url(self, url: str) -> bool:
        """Verifies if the URL belongs to an allowed documentation prefix."""
        return any(url.startswith(prefix) for prefix in self.allowed_prefixes)

    async def _try_mark_visited(self, url: str) -> bool:
        """Atomically checks and registers a URL as visited. Returns True if newly registered."""
        async with self.visited_lock:
            if url in self.visited_urls:
                return False
            self.visited_urls.add(url)
            return True

    async def _fetch_single_node(
        self,
        crawler: AsyncWebCrawler,
        url: str,
        depth: int
    ) -> tuple[DocumentNode | None, dict[str, str]]:
        """Fetches and parses a single documentation page under semaphore throttling."""
        indent = "  " * (depth - 1)
        print(f"{indent}[Depth {depth}/{self.config.max_depth} | In Progress: {len(self.visited_urls)}] Crawling: {url}")

        try:
            result: CrawlResult = await crawler.arun(url=url, config=self.run_config)
            if not result.success:
                print(f"{indent}  -> Failed: {result.error_message}")
                return None, {}

            summary, keywords, outbound_links = parse_extracted_metadata(result.extracted_content)
            title = derive_page_title(result, url)

            node = DocumentNode(
                url=url,
                title=title,
                depth_level=depth,
                summary=summary,
                keywords=keywords,
                markdown_content=result.markdown or ""
            )
            return node, outbound_links

        except Exception as e:
            print(f"{indent}  -> Error processing {url}: {e}")
            return None, {}

    async def _crawl_children_branches(
        self,
        crawler: AsyncWebCrawler,
        base_url: str,
        outbound_links: dict[str, str],
        child_depth: int
    ) -> list[DocumentNode]:
        """Discovers, validates, and concurrently crawls child pages."""
        child_tasks = []

        for _, raw_target in outbound_links.items():
            target_url = normalize_url(urljoin(base_url, raw_target))
            if not self.is_allowed_section_url(target_url):
                continue

            if await self._try_mark_visited(target_url):
                child_tasks.append(
                    self.crawl_node(
                        crawler=crawler,
                        current_url=target_url,
                        current_depth=child_depth
                    )
                )

        if not child_tasks:
            return []

        results = await asyncio.gather(*child_tasks, return_exceptions=False)
        return [child for child in results if child is not None]

    async def crawl_node(
        self,
        crawler: AsyncWebCrawler,
        current_url: str,
        current_depth: int = 1
    ) -> DocumentNode | None:
        """Recursively orchestrates page crawling and nested sub-document exploration."""
        url = normalize_url(current_url)
        if not self.is_allowed_section_url(url):
            return None

        async with self.semaphore:
            node, outbound_links = await self._fetch_single_node(crawler, url, current_depth)
            if not node:
                return None

        if current_depth < self.config.max_depth and outbound_links:
            children = await self._crawl_children_branches(
                crawler=crawler,
                base_url=url,
                outbound_links=outbound_links,
                child_depth=current_depth + 1
            )
            node.sub_documents.extend(children)

        return node

    async def crawl_all(self, crawler: AsyncWebCrawler) -> list[DocumentNode]:
        """High-level orchestration: registers root URLs and initiates concurrent branch crawling."""
        for root_url in self.root_urls:
            await self._try_mark_visited(root_url)

        tasks = [
            self.crawl_node(crawler=crawler, current_url=root_url, current_depth=1)
            for root_url in self.root_urls
        ]
        results = await asyncio.gather(*tasks)
        return [node for node in results if node is not None]
#endregion

#region Execution
async def main() -> None:
    root_urls = [
        "https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html",
        "https://docs.kanzi.com/4.1.0/en/working-with/working-with.html",
        "https://docs.kanzi.com/4.1.0/en/best-practices/best-practices.html"
    ]

    print("==================================================================")
    print("  Starting High-Speed Concurrent Doc Tree Crawler (Kanzi 4.1.0)")
    print("==================================================================")

    config = CrawlerConfig(max_depth=3, max_concurrency=30)
    crawler_engine = ConcurrentDocTreeCrawler(root_urls=root_urls, config=config)

    async with AsyncWebCrawler() as crawler:
        root_forest = await crawler_engine.crawl_all(crawler=crawler)

    # Save nested document tree
    output_path = os.path.join(os.path.dirname(__file__), config.output_filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        forest_dicts = [node.model_dump() for node in root_forest]
        json.dump(forest_dicts, f, ensure_ascii=False, indent=2)

    print(
        f"\nSuccessfully finished! Saved {len(root_forest)} root document trees "
        f"(total {len(crawler_engine.visited_urls)} pages) to {output_path}"
    )


if __name__ == "__main__":
    asyncio.run(main())
#endregion
