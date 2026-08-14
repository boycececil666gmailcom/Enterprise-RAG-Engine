import os
import json
import asyncio
from urllib.parse import urljoin
from crawl4ai import AsyncWebCrawler, CrawlResult, LLMExtractionStrategy, LLMConfig
BASE_URL = "https://docs.kanzi.com/4.1.0/en/"
START_URLS = [
    "https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html",
    "https://docs.kanzi.com/4.1.0/en/best-practices/best-practices.html"
]



async def scrape_docs() -> list[dict[str, str]]:
    visited = set()
    to_visit = set(START_URLS)
    documents = []

    async with AsyncWebCrawler() as crawler:
        while to_visit:
            current_url = to_visit.pop()
            
            # Remove fragment if any
            current_url = current_url.split('#')[0]

            if current_url in visited:
                continue
                
            visited.add(current_url)
            print(f"Scraping: {current_url}")
            
            try:
                # Crawl the page, extract only the main article to avoid noise
                result: CrawlResult = await crawler.arun(
                    url=current_url,
                    css_selector="article",
                    extraction_strategy=LLMExtractionStrategy(
                        llm_config=LLMConfig(provider="ollama/qwen2.5:7b", base_url="http://localhost:11434"),
                        instruction="Kanziフレームワークの公式ドキュメントです。このページを日本語で要約してください。要約のみを出力してください。"
                    )
                )
                
                if not result.success:
                    print(f"Failed to fetch {current_url}: {result.error_message}")
                    continue
                    
                content: str = result.markdown
                summary: str = result.extracted_content or ""
                
                # Fetch title from metadata or derive from URL
                title = ""
                if isinstance(result.metadata, dict):
                    title = result.metadata.get("title", "")


                if content:
                    documents.append({
                        "url": current_url,
                        "title": title,
                        "content": content,
                        "summary": summary
                    })
                
                # Extract internal links from Crawl4AI result
                internal_links = result.links.get("internal", [])
                for link_obj in internal_links:
                    href = link_obj.get("href")
                    if not href:
                        continue
                        
                    full_url = urljoin(current_url, href).split('#')[0]
                    if full_url not in visited:
                        to_visit.add(full_url)

            except Exception as e:
                print(f"Error processing {current_url}: {e}")

    return documents


