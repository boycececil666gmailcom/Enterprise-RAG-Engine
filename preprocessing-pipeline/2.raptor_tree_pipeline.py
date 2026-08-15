#region Imports
import json
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
#endregion

#region File Paths
_CURRENT_DIR = Path(__file__).resolve().parent
INPUT_JSON_PATH = _CURRENT_DIR / "1.scrape.json"
OUTPUT_JSON_PATH = _CURRENT_DIR / "2.raptor_chunks.json"
#endregion

#region UUID Helper
_RAPTOR_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

def generate_deterministic_id(seed_str: str) -> str:
    """Generates reproducible UUIDv5 from a string."""
    return str(uuid.uuid5(_RAPTOR_NAMESPACE, seed_str))
#endregion

#region Data Models
class RaptorNode:
    """Represents a node in the 3-tier hierarchical RAPTOR tree (0: Root, 1: Section, 2: Leaf)."""
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
        self.layer = layer  # 0: Root Global Summary, 1: Section Summary, 2: Leaf Detail Chunk
        self.content = content
        self.url = url
        self.markdown = markdown
        self.keywords = keywords or []
        self.parent_id = parent_id
        self.breadcrumb = breadcrumb

    def to_dict(self) -> Dict[str, Any]:
        """Converts RaptorNode to standardized JSON format with clean content and metadata."""
        return {
            "id": self.node_id,
            "small": self.content,
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

#region Text Splitters
def get_markdown_splitters() -> Tuple[MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter]:
    """Returns markdown header and recursive character splitters."""
    headers_to_split = [
        ("#", "Header_1"),
        ("##", "Header_2"),
        ("###", "Header_3"),
    ]
    md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split, strip_headers=False)
    char_splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=120)
    return md_splitter, char_splitter
#endregion

#region Tree Builder
class RaptorTreeBuilder:
    """Builds 3-layer RAPTOR structured dataset (0: Root, 1: Section, 2: Leaf)."""
    def __init__(self, raw_json_path: Path):
        self.raw_json_path = raw_json_path
        self.nodes: List[RaptorNode] = []
        self.md_splitter, self.char_splitter = get_markdown_splitters()

    def build(self) -> List[RaptorNode]:
        """Constructs Layer 0 (Root), Layer 1 (Section), and Layer 2 (Leaves)."""
        with open(self.raw_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for root_item in data:
            self._process_root(root_item)

        return self.nodes

    def _process_root(self, root_item: Dict[str, Any]):
        """Processes Root Level (Layer 0 in RAPTOR)."""
        title = root_item.get("title", "Root Document")
        url = root_item.get("url", "")
        root_id = generate_deterministic_id(f"root_{url}_{title}")
        breadcrumb = title
        summary = root_item.get("summary", "")
        markdown = root_item.get("markdown_content", "")

        # Layer 0: Root Global Summary
        root_node = RaptorNode(
            node_id=root_id,
            title=title,
            layer=0,
            content=summary or markdown[:1000],
            url=url,
            markdown=markdown,
            keywords=root_item.get("keywords", []),
            parent_id=None,
            breadcrumb=breadcrumb
        )
        self.nodes.append(root_node)

        for sec_item in root_item.get("sub_documents", []):
            self._process_section(sec_item, parent_id=root_id, parent_breadcrumb=breadcrumb)

    def _process_section(self, sec_item: Dict[str, Any], parent_id: str, parent_breadcrumb: str):
        """Processes Section Level (Layer 1 in RAPTOR)."""
        title = sec_item.get("title", "Section Document")
        url = sec_item.get("url", "")
        sec_id = generate_deterministic_id(f"sec_{url}_{title}")
        breadcrumb = f"{parent_breadcrumb} > {title}"
        summary = sec_item.get("summary", "")
        markdown = sec_item.get("markdown_content", "")

        # Layer 1: Section Intermediate Summary
        sec_node = RaptorNode(
            node_id=sec_id,
            title=title,
            layer=1,
            content=summary or markdown[:1000],
            url=url,
            markdown=markdown,
            keywords=sec_item.get("keywords", []),
            parent_id=parent_id,
            breadcrumb=breadcrumb
        )
        self.nodes.append(sec_node)

        sub_docs = sec_item.get("sub_documents", [])
        if sub_docs:
            for leaf_doc in sub_docs:
                self._process_leaf(leaf_doc, parent_id=sec_id, parent_breadcrumb=breadcrumb)
        else:
            self._chunk_leaf_content(sec_item, parent_id=sec_id, parent_breadcrumb=breadcrumb)

    def _process_leaf(self, leaf_item: Dict[str, Any], parent_id: str, parent_breadcrumb: str):
        """Processes detailed pages and splits them into Layer 2 leaves."""
        title = leaf_item.get("title", "Leaf Document")
        breadcrumb = f"{parent_breadcrumb} > {title}"
        self._chunk_leaf_content(leaf_item, parent_id=parent_id, parent_breadcrumb=breadcrumb)

    def _chunk_leaf_content(self, doc_item: Dict[str, Any], parent_id: str, parent_breadcrumb: str):
        """Splits markdown into Layer 2 semantic leaf chunks."""
        markdown_content = doc_item.get("markdown_content", "")
        if not markdown_content.strip():
            return

        header_splits = self.md_splitter.split_text(markdown_content)
        final_splits = self.char_splitter.split_documents(header_splits)
        
        doc_url = doc_item.get("url", "")
        doc_title = doc_item.get("title", "Detail Chunk")
        doc_keywords = doc_item.get("keywords", [])

        for idx, split in enumerate(final_splits):
            leaf_id = generate_deterministic_id(f"leaf_{doc_url}_{doc_title}_{idx}")
            leaf_node = RaptorNode(
                node_id=leaf_id,
                title=doc_title,
                layer=2,  # Layer 2: Detailed Leaf Chunk
                content=split.page_content,
                url=doc_url,
                markdown=split.page_content,
                keywords=doc_keywords,
                parent_id=parent_id,
                breadcrumb=parent_breadcrumb
            )
            self.nodes.append(leaf_node)
#endregion

#region Pipeline Execution
def run_formatting_pipeline():
    """Builds RAPTOR chunks and formats them into standard JSON with metadata wrapper."""
    if not INPUT_JSON_PATH.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_JSON_PATH}")

    print(f"[RAPTOR Pipeline] Reading input from: {INPUT_JSON_PATH.name}...")
    builder = RaptorTreeBuilder(INPUT_JSON_PATH)
    nodes = builder.build()

    formatted_data = [node.to_dict() for node in nodes]

    layer_0_cnt = sum(1 for n in formatted_data if n["metadata"]["raptor_layer"] == 0)
    layer_1_cnt = sum(1 for n in formatted_data if n["metadata"]["raptor_layer"] == 1)
    layer_2_cnt = sum(1 for n in formatted_data if n["metadata"]["raptor_layer"] == 2)

    print(f"[RAPTOR Pipeline] Formatted {len(formatted_data)} total chunks:")
    print(f"  - Layer 0 (Root Global Summaries): {layer_0_cnt}")
    print(f"  - Layer 1 (Section Summaries): {layer_1_cnt}")
    print(f"  - Layer 2 (Leaf Detail Chunks): {layer_2_cnt}")

    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, ensure_ascii=False, indent=2)

    print(f"[RAPTOR Pipeline] Successfully saved formatted dataset with metadata wrapper to: {OUTPUT_JSON_PATH.name}")

if __name__ == "__main__":
    run_formatting_pipeline()
#endregion
