#region Imports & Setup
import asyncio
import json
import logging
import os
import sys
from pathlib import Path
from typing import List, Optional

import litellm
import os
os.environ['LITELLM_LOG'] = 'DEBUG'
from pydantic import BaseModel, Field

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("Crawl4AI-Pipeline")

# Path Configurations
PIPELINE_DIR = Path(__file__).resolve().parent
DOCS_DIR = (PIPELINE_DIR / "doc").resolve()
OUTPUT_JSON = (PIPELINE_DIR / "rag_chunks.json").resolve()
#endregion


#region Pydantic Schema Definition
class KanziDocSection(BaseModel):
    """Pydantic schema for structured document extraction using Crawl4AI and LLM."""
    page_title: str = Field(description="Title of the documentation page")
    section_title: str = Field(description="Section heading or main topic name")
    child_content: str = Field(description="Granular text chunk (approx 200-250 characters) summarizing key concepts or instructions for vector search")
    parent_content: str = Field(description="Complete rich section context (approx 1500-2000 characters) for LLM response generation")
    code_snippets: List[str] = Field(default_factory=list, description="Code examples extracted from the section if present")
#endregion


#region Crawl4AI Extraction Engine
async def extract_url_with_ollama(
    crawler: "AsyncWebCrawler",
    url: str,
    model_provider: str = "ollama/qwen2.5:7b"
) -> List[KanziDocSection]:
    """
    Extracts structured documentation sections from a URL using Crawl4AI to scrape,
    and litellm + Ollama to parse structured JSON.
    """
    import litellm
    import json
    
    logger.info(f"Extracting structured sections from: {url}")
    
    result = await crawler.arun(
        url=url,
        bypass_cache=True
    )

    if not result.success or not result.markdown:
        logger.warning(f"Failed or empty scrape for URL: {url}")
        return []
        
    logger.info(f"Scraped {len(result.markdown)} characters of markdown.")

    # Chunk the markdown to fit in context (approx 4000 chars per chunk)
    chunk_size = 4000
    markdown_chunks = [result.markdown[i:i+chunk_size] for i in range(0, len(result.markdown), chunk_size)]
    
    sections = []
    
    instruction = (
        "Analyze this documentation page chunk and extract structured sections. "
        "Return a JSON object with a single key 'sections' containing a list of objects. "
        "Each object must have exactly these keys: "
        "'page_title' (string), 'section_title' (string), "
        "'child_content' (string, ~200-250 chars summary), "
        "'parent_content' (string, full section context), "
        "'code_snippets' (list of strings, code examples if any)."
    )
    
    for i, chunk in enumerate(markdown_chunks):
        if len(chunk.strip()) < 50:
            continue
            
        logger.info(f"Processing chunk {i+1}/{len(markdown_chunks)} with LLM...")
        try:
            response = litellm.completion(
                model=model_provider,
                messages=[
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": f"Document Chunk:\n\n{chunk}"}
                ],
                api_base="http://localhost:11434",
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            parsed = json.loads(content)
            
            if "sections" in parsed:
                for item in parsed["sections"]:
                    sections.append(KanziDocSection(**item))
                    
        except Exception as e:
            logger.error(f"Error processing chunk {i+1}: {e}")
            
    logger.info(f"Successfully extracted {len(sections)} sections from {url}")
    return sections
#endregion


#region Dataset Processing & Export
def convert_sections_to_chunks(sections: List[KanziDocSection], source_url: str, local_path: str) -> List[dict]:
    """
    Converts extracted Pydantic KanziDocSection objects into vector database chunk schema.
    """
    chunks = []
    for idx, sec in enumerate(sections, start=1):
        chunk_id = f"{local_path}#chunk-{idx}"
        
        # Build child content with context prefix
        ctx_prefix = f"[Document Context: {sec.page_title} > {sec.section_title}]"
        child_text = f"{ctx_prefix}\n\n{sec.child_content}" if not sec.child_content.startswith("[Document Context:") else sec.child_content
        parent_text = f"{ctx_prefix}\n\n{sec.parent_content}" if not sec.parent_content.startswith("[Document Context:") else sec.parent_content

        chunk_record = {
            "id": chunk_id,
            "child_content": child_text,
            "chunk_type": "code" if sec.code_snippets else "prose",
            "metadata": {
                "source_url": source_url,
                "local_path": local_path,
                "page_title": sec.page_title,
                "chunk_type": "code" if sec.code_snippets else "prose",
                "parent_id": f"{local_path}#sec-{idx}",
                "parent_content": parent_text
            }
        }
        chunks.append(chunk_record)
        
    return chunks


def export_rag_chunks_dataset(all_chunks: List[dict], output_json: Path) -> None:
    """
    Exports combined chunk records to rag_chunks.json.
    """
    payload = {
        "dataset_name": "Kanzi Documentation VDB Vector Chunks (Crawl4AI + Ollama Pipeline)",
        "total_chunks": len(all_chunks),
        "chunks": all_chunks
    }

    logger.info(f"Saving dataset to {output_json.name}...")
    json_str = json.dumps(payload, indent=2, ensure_ascii=False)
    output_json.write_text(json_str, encoding="utf-8")

    json_mb = output_json.stat().st_size / (1024 * 1024)
    logger.info(f"Dataset export complete! JSON: {json_mb:.2f} MB")
#endregion


#region Main CLI Execution
async def run_pipeline(start_url: str = "https://docs.kanzi.com/4.1.0/en/overview.html", model_provider: str = "ollama/qwen2.5:7b"):
    """
    Runs the full Crawl4AI + Ollama extraction pipeline.
    """
    from crawl4ai import AsyncWebCrawler

    logger.info("========================================================")
    logger.info(f">>> Starting Crawl4AI + Ollama RAG Preprocessing Pipeline")
    logger.info(f">>> Target URL: {start_url} | Model Provider: {model_provider}")
    logger.info("========================================================")

    async with AsyncWebCrawler(verbose=True) as crawler:
        sections = await extract_url_with_ollama(crawler, start_url, model_provider=model_provider)
        chunks = convert_sections_to_chunks(sections, start_url, "overview.md")
        if chunks:
            export_rag_chunks_dataset(chunks, OUTPUT_JSON)
        else:
            logger.warning("No chunks were extracted.")


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://docs.kanzi.com/4.1.0/en/overview.html"
    model = sys.argv[2] if len(sys.argv) > 2 else "ollama/qwen2.5:7b"
    asyncio.run(run_pipeline(url, model))
#endregion
