#region Imports
from __future__ import annotations
import os
import re
import json
from typing import Any
from urllib.parse import urlparse
from pydantic import BaseModel, Field
#endregion

#region Models
class DocumentNode(BaseModel):
    url: str
    title: str
    depth_level: int
    summary: str = ""
    keywords: list[str] = Field(default_factory=list)
    markdown_content: str = ""
    sub_documents: list[DocumentNode] = Field(default_factory=list)

class ConsolidatedChunk(BaseModel):
    chunk_id: str
    source_url: str
    depth_level: int
    hierarchy_path: str
    summary_keywords: list[str] = Field(default_factory=list)
    small_search_content: str
    big_parent_content: str
    char_count: int
#endregion

#region Markdown Sanitizer
def clean_markdown(raw_markdown: str) -> str:
    """Clean navigation noise, SVG links, and Sphinx anchor symbols."""
    text = raw_markdown
    text = re.sub(r"\[¶\]\([^)]+\)", "", text)
    text = re.sub(r"!\[.*?\]\(.*?\.svg\)", "", text)
    text = re.sub(r"Copy page\s+Copy this page as Markdown.*?(?=\n\n|\n[A-Z#])", "", text, flags=re.DOTALL)
    text = re.sub(r"Ask Claude.*?Download and run the Claude mcpb\.", "", text, flags=re.DOTALL)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text
#endregion

#region Tree Transformer & Chunker
class DocTreeTransformer:
    def __init__(self, target_child_size: int = 300):
        self.target_child_size = target_child_size
        self.heading_pattern = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)
        self.chunk_counter = 1

    def tree_to_master_markdown(self, nodes: list[DocumentNode]) -> str:
        """Recursively render the DocumentNode tree into a single beautifully indented Master Markdown file."""
        lines: list[str] = [
            "# Kanzi Documentation Master Knowledge Base\n\n"
            "> Consolidated hierarchical documentation generated from recursive nested web crawl.\n\n"
        ]

        def render_node(node: DocumentNode, current_h_level: int):
            prefix = "#" * min(current_h_level, 5)
            cleaned_body = clean_markdown(node.markdown_content)
            
            # Remove existing top H1 from body if it duplicates node title
            body_lines = cleaned_body.splitlines()
            if body_lines and body_lines[0].startswith("#"):
                body_lines = body_lines[1:]
            content_without_h1 = "\n".join(body_lines).strip()

            lines.append(f"\n<!-- NODE_START: {node.url} (Depth {node.depth_level}) -->")
            lines.append(f"<!-- SOURCE_URL: {node.url} -->")
            lines.append(f"{prefix} {node.title}\n")
            if node.summary:
                lines.append(f"> **Summary**: {node.summary}\n")
            if content_without_h1:
                lines.append(f"{content_without_h1}\n")
            
            # Recursively render nested child documents
            for child in node.sub_documents:
                render_node(child, current_h_level + 1)

            lines.append(f"<!-- NODE_END: {node.url} -->\n")

        for root in nodes:
            render_node(root, current_h_level=2)

        return "\n".join(lines)

    def extract_chunks_from_tree(self, nodes: list[DocumentNode]) -> list[ConsolidatedChunk]:
        """Extract Small-to-Big search chunks from the nested document tree."""
        all_chunks: list[ConsolidatedChunk] = []

        def process_node(node: DocumentNode, parent_path: str):
            current_path = f"{parent_path} > {node.title}" if parent_path else node.title
            cleaned_text = clean_markdown(node.markdown_content)

            if cleaned_text:
                # 1. Parent Content (Full section text + summary)
                big_parent = f"## {current_path}\n\n"
                if node.summary:
                    big_parent += f"**Overview**: {node.summary}\n\n"
                big_parent += cleaned_text

                # 2. Small Search Content (Breadcrumbs + summary/first paragraph for high precision match)
                first_para = cleaned_text.split("\n\n")[0].strip()
                summary_line = node.summary or first_para
                small_search = f"[Document Context: {current_path}]\n{summary_line}"

                all_chunks.append(
                    ConsolidatedChunk(
                        chunk_id=f"tree_chunk_{self.chunk_counter:04d}",
                        source_url=node.url,
                        depth_level=node.depth_level,
                        hierarchy_path=current_path,
                        summary_keywords=node.keywords,
                        small_search_content=small_search,
                        big_parent_content=big_parent,
                        char_count=len(big_parent)
                    )
                )
                self.chunk_counter += 1

            # Recursively process child documents
            for child in node.sub_documents:
                process_node(child, current_path)

        for root in nodes:
            process_node(root, parent_path="Kanzi Documentation")

        return all_chunks
#endregion

#region Pipeline Runner
def main():
    base_dir = os.path.dirname(__file__)
    scrape_path = os.path.join(base_dir, "scrape.json")
    master_md_path = os.path.join(base_dir, "kanzi_unified_master.md")
    output_chunks_path = os.path.join(base_dir, "kanzi_unified_chunks.json")

    print(f"[1/3] Reading nested document tree from {scrape_path}...")
    with open(scrape_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Convert to DocumentNode list
    doc_tree = [DocumentNode(**item) for item in raw_data]

    transformer = DocTreeTransformer()

    print("[2/3] Building hierarchical Master Markdown from Document Tree...")
    master_md = transformer.tree_to_master_markdown(doc_tree)
    with open(master_md_path, "w", encoding="utf-8") as f:
        f.write(master_md)
    print(f"      -> Master Markdown saved: {master_md_path} ({len(master_md)} chars)")

    print("[3/3] Generating Small-to-Big RAG Chunks from Document Tree...")
    chunks = transformer.extract_chunks_from_tree(doc_tree)
    chunks_dict = [c.model_dump() for c in chunks]
    with open(output_chunks_path, "w", encoding="utf-8") as f:
        json.dump(chunks_dict, f, ensure_ascii=False, indent=2)
    print(f"      -> Successfully saved {len(chunks)} tree-aligned chunks to: {output_chunks_path}")

if __name__ == "__main__":
    main()
#endregion
