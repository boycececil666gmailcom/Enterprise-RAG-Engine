#region Imports
import json
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
#endregion

#region Configuration
_CURRENT_DIR = Path(__file__).resolve().parent
INPUT_JSON_PATH = _CURRENT_DIR / "1.scrape.json"
OUTPUT_JSON_PATH = _CURRENT_DIR / "2.raptor_chunks.json"
_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
#endregion

#region Models
class RaptorNode:
    """Represents a node in the 3-tier RAPTOR tree (0: Root, 1: Section, 2: Leaf)."""
    def __init__(
        self,
        node_id: str,
        title: str,
        layer: int,
        content: str,
        url: str = "",
        markdown: str = "",
        keywords: Optional[List[str]] = None,
        parent_id: Optional[str] = None,
        breadcrumb: str = ""
    ):
        self.node_id = node_id
        self.title = title
        self.layer = layer
        self.content = content
        self.url = url
        self.markdown = markdown
        self.keywords = keywords or []
        self.parent_id = parent_id
        self.breadcrumb = breadcrumb

    def to_dict(self) -> Dict[str, Any]:
        """Converts RaptorNode to JSON format with [title], [summary], and [keyword] tags in small."""
        parts = []
        if self.title:
            parts.append(f"[title] {self.title}")
        if self.content:
            parts.append(f"[summary] {self.content}")
        if self.keywords:
            parts.append(f"[keyword] {', '.join(self.keywords)}")

        return {
            "id": self.node_id,
            "small": "\n".join(parts) if parts else self.content,
            "metadata": {
                "parent_id": self.parent_id or "",
                "title": self.title,
                "url": self.url,
                "raptor_layer": self.layer,
                "breadcrumb": self.breadcrumb,
                "keywords": self.keywords,
                "big": self.markdown,
            }
        }
#endregion

#region Tree Builder
class RaptorTreeBuilder:
    """Builds 3-layer RAPTOR structured dataset (0: Root, 1: Section, 2: Leaf)."""
    def __init__(self, raw_json_path: Path):
        self.raw_json_path = raw_json_path
        self.nodes: List[RaptorNode] = []
        self.md_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[("#", "H1"), ("##", "H2"), ("###", "H3")],
            strip_headers=False
        )
        self.char_splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=120)

    def _uuid(self, seed: str) -> str:
        return str(uuid.uuid5(_NAMESPACE, seed))

    def build(self) -> List[RaptorNode]:
        with open(self.raw_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for root in data:
            self._process_root(root)
        return self.nodes

    def _process_root(self, item: Dict[str, Any]):
        title = item.get("title", "Root Document")
        url = item.get("url", "")
        root_id = self._uuid(f"root_{url}_{title}")

        self.nodes.append(RaptorNode(
            node_id=root_id,
            title=title,
            layer=0,
            content=item.get("summary", ""),
            url=url,
            markdown=item.get("markdown_content", ""),
            keywords=item.get("keywords", []),
            breadcrumb=title
        ))

        for sec in item.get("sub_documents", []):
            self._process_section(sec, parent_id=root_id, breadcrumb=title)

    def _process_section(self, item: Dict[str, Any], parent_id: str, breadcrumb: str):
        title = item.get("title", "Section Document")
        url = item.get("url", "")
        sec_id = self._uuid(f"sec_{url}_{title}")
        sec_bc = f"{breadcrumb} > {title}"

        self.nodes.append(RaptorNode(
            node_id=sec_id,
            title=title,
            layer=1,
            content=item.get("summary", ""),
            url=url,
            markdown=item.get("markdown_content", ""),
            keywords=item.get("keywords", []),
            parent_id=parent_id,
            breadcrumb=sec_bc
        ))

        sub_docs = item.get("sub_documents", [])
        if sub_docs:
            for leaf in sub_docs:
                leaf_title = leaf.get("title", "Leaf Document")
                self._chunk_leaf(leaf, parent_id=sec_id, breadcrumb=f"{sec_bc} > {leaf_title}")
        else:
            self._chunk_leaf(item, parent_id=sec_id, breadcrumb=sec_bc)

    def _chunk_leaf(self, doc: Dict[str, Any], parent_id: str, breadcrumb: str):
        markdown = doc.get("markdown_content", "").strip()
        if not markdown:
            return

        splits = self.char_splitter.split_documents(self.md_splitter.split_text(markdown))
        url = doc.get("url", "")
        title = doc.get("title", "Detail Chunk")
        summary = doc.get("summary", "")
        keywords = doc.get("keywords", [])

        for idx, split in enumerate(splits):
            leaf_id = self._uuid(f"leaf_{url}_{title}_{idx}")
            self.nodes.append(RaptorNode(
                node_id=leaf_id,
                title=title,
                layer=2,
                content=summary or split.page_content,
                url=url,
                markdown=split.page_content,
                keywords=keywords,
                parent_id=parent_id,
                breadcrumb=breadcrumb
            ))
#endregion

#region Pipeline Execution
def run_formatting_pipeline():
    """Builds RAPTOR chunks and formats them into standard JSON."""
    if not INPUT_JSON_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_JSON_PATH}")

    print(f"[RAPTOR] Building tree from: {INPUT_JSON_PATH.name}...")
    builder = RaptorTreeBuilder(INPUT_JSON_PATH)
    nodes = builder.build()
    formatted = [n.to_dict() for n in nodes]

    counts = {i: sum(1 for n in formatted if n["metadata"]["raptor_layer"] == i) for i in range(3)}
    print(f"[RAPTOR] Formatted {len(formatted)} chunks: Layer 0={counts[0]}, Layer 1={counts[1]}, Layer 2={counts[2]}")

    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(formatted, f, ensure_ascii=False, indent=2)

    print(f"[RAPTOR] Saved dataset to: {OUTPUT_JSON_PATH.name}")


if __name__ == "__main__":
    run_formatting_pipeline()
#endregion
