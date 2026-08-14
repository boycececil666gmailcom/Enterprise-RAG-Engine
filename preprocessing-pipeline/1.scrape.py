#region Imports
import os
import json
import asyncio
from typing import Any
from urllib.parse import urljoin
from pydantic import BaseModel, Field
from crawl4ai import AsyncWebCrawler, CrawlResult, CrawlerRunConfig, LLMExtractionStrategy, LLMConfig
#endregion

#region Schema
class PageSummary(BaseModel):
    summary: str = Field(description="Summary of the Kanzi framework documentation page covering core concepts and best practices.")
    keywords: list[str] = Field(description="Key topics and keywords for this page (around 3 to 5 items).")
    links: dict[str, str] = Field(
        default_factory=dict,
        description="A dictionary mapping a summary/description of what each link leads to (key) to its target URL (value) found on this page."
    )
#endregion

#region Constants
URLS = {
    "https://docs.kanzi.com/4.1.0/en/working-with/working-with.html",
    "https://docs.kanzi.com/4.1.0/en/kanzi-fundamentals/kanzi-fundamentals.html",
    "https://docs.kanzi.com/4.1.0/en/best-practices/best-practices.html"
}
#endregion

#region Scraper
async def scrape_docs() -> list[dict[str, Any]]:
    visited = set()
    to_visit = set(URLS)
    documents = []

    # 1. Local Ollama config (Original)
    ollama_crawler_config = CrawlerRunConfig(
        css_selector="article",
        extraction_strategy=LLMExtractionStrategy(
            llm_config=LLMConfig(provider="ollama/qwen2.5:7b", base_url="http://localhost:11434"),
            schema=PageSummary.model_json_schema(),
            extraction_type="schema",
            instruction="This is official documentation for the Kanzi framework. Extract the key information from this page and strictly output according to the specified JSON schema, including the page summary, key topics/keywords, and a dictionary of links found on this page where the key is a summary of what that destination link leads to and the value is the URL. Output valid JSON only.",
            extra_args={"format": "json"},
            force_json_response=True
        )
    )

    # 2. OpenRouter DeepSeek config (Decart provider)
    try:
        from config import OPENROUTER_API_KEY
    except Exception:
        OPENROUTER_API_KEY = ""

    openrouter_crawler_config = CrawlerRunConfig(
        css_selector="article",
        extraction_strategy=LLMExtractionStrategy(
            llm_config=LLMConfig(
                provider="openrouter/deepseek/deepseek-v4-flash-0731",
                api_token=OPENROUTER_API_KEY
            ),
            schema=PageSummary.model_json_schema(),
            extraction_type="schema",
            instruction="Extract key concepts and links from this Kanzi documentation page to populate a concrete JSON instance. IMPORTANT: Do NOT output schema definition metadata (do NOT output keys like 'properties', 'type', 'title', or 'required'). Output only the populated JSON object with 'summary' (str), 'keywords' (list[str]), and 'links' (dict[str, str]). Output valid JSON only.",
            extra_args={
                "response_format": {"type": "json_object"},
                "extra_body": {
                    "provider": {
                        "order": ["Decart"],
                        "allow_fallbacks": True
                    }
                }
            },
            force_json_response=True
        )
    )

    async with AsyncWebCrawler() as crawler:
        while to_visit:
            current_url = to_visit.pop()
            
            # Remove fragment if any
            current_url = current_url.split('#')[0]

            if current_url in visited:
                continue
                
            visited.add(current_url)            
            try:
                # Crawl the page with CrawlerRunConfig to apply CSS selector & extraction
                result: CrawlResult = await crawler.arun(
                    url=current_url,
                    config=openrouter_crawler_config
                )
                
                if not result.success:
                    print(f"Failed to fetch {current_url}: {result.error_message}")
                    continue



                documents.append({
                    "url": current_url,
                    "title": (result.metadata or {}).get("title", ""),
                    "content": result.markdown,
                    "LLM_extract": json.loads(result.extracted_content) if result.extracted_content else None
                })

            except Exception as e:
                print(f"Error processing {current_url}: {e}")

    return documents
#endregion

#region Main
async def main():
    print("Starting Kanzi documentation scraper...")
    documents = await scrape_docs()
    
    output_path = os.path.join(os.path.dirname(__file__), 'scrape.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully saved {len(documents)} pages to {output_path}")

if __name__ == "__main__":
    asyncio.run(main())
#endregion

