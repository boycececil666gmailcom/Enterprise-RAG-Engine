#region Imports
import os
from typing import Any, Dict, List, Optional
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode

from .config import GEMINI_API_KEY, GEMINI_EMBED_MODEL, QDRANT_API_KEY, QDRANT_URL
#endregion

#region Raptor Retriever
class RaptorRetriever:
    """
    RAPTOR 3-Tier Multi-Layer Retriever supporting Tree Traversal across 3 dedicated collections:
    - Layer 0: 'raptor_layer_0' (Root Global Summaries)
    - Layer 1: 'raptor_layer_1' (Section Topic Summaries)
    - Layer 2: 'raptor_layer_2' (Leaf Detail Chunks)
    """
    def __init__(self):
        self.dense_embeddings = GoogleGenerativeAIEmbeddings(
            model=GEMINI_EMBED_MODEL,
            google_api_key=GEMINI_API_KEY
        )
        self.sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

        # Initialize vector stores for each dedicated layer collection
        self.layer_stores: Dict[int, QdrantVectorStore] = {
            layer: QdrantVectorStore.from_existing_collection(
                url=QDRANT_URL,
                api_key=QDRANT_API_KEY,
                collection_name=f"raptor_layer_{layer}",
                content_payload_key="small",
                embedding=self.dense_embeddings,
                sparse_embedding=self.sparse_embeddings,
                retrieval_mode=RetrievalMode.HYBRID
            )
            for layer in (0, 1, 2)
        }

    def retrieve_layer(
        self,
        layer: int,
        query: str,
        top_k: int = 5,
        filter_dict: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Searches a specific RAPTOR layer collection."""
        store = self.layer_stores.get(layer)
        if not store:
            raise ValueError(f"Invalid RAPTOR layer: {layer}. Must be 0, 1, or 2.")

        raw_docs = store.similarity_search(query=query, k=top_k, filter=filter_dict)
        return [self._format_doc(doc, layer) for doc in raw_docs]

    def retrieve_tree_traversal(
        self,
        query: str,
        top_k_layer0: int = 1,
        top_k_layer1: int = 2,
        top_k_layer2: int = 3
    ) -> Dict[str, Any]:
        """
        Executes hierarchical top-down tree traversal:
        1. Find best matching Root (Layer 0)
        2. Drill down to child Sections (Layer 1) belonging to the Root
        3. Drill down to child Leaves (Layer 2) belonging to the Sections
        """
        # Step 1: Query Layer 0
        layer_0_results = self.retrieve_layer(layer=0, query=query, top_k=top_k_layer0)

        # Step 2: Query Layer 1 (Optionally filtered by matched Layer 0 IDs)
        layer_1_results: List[Dict[str, Any]] = []
        for root in layer_0_results:
            root_id = root.get("id", "")
            filter_l1 = {"parent_id": root_id} if root_id else None
            l1_docs = self.retrieve_layer(layer=1, query=query, top_k=top_k_layer1, filter_dict=filter_l1)
            layer_1_results.extend(l1_docs)

        # If no l1 found with filter, fallback to unconstrained l1 search
        if not layer_1_results:
            layer_1_results = self.retrieve_layer(layer=1, query=query, top_k=top_k_layer1)

        # Step 3: Query Layer 2
        layer_2_results: List[Dict[str, Any]] = []
        for sec in layer_1_results:
            sec_id = sec.get("id", "")
            filter_l2 = {"parent_id": sec_id} if sec_id else None
            l2_docs = self.retrieve_layer(layer=2, query=query, top_k=top_k_layer2, filter_dict=filter_l2)
            layer_2_results.extend(l2_docs)

        if not layer_2_results:
            layer_2_results = self.retrieve_layer(layer=2, query=query, top_k=top_k_layer2)

        return {
            "root_overview": layer_0_results,
            "section_summaries": layer_1_results,
            "leaf_chunks": layer_2_results,
        }

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        target_layer: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves relevant documents. If target_layer is None, searches all layers and returns top_k.
        """
        if target_layer is not None:
            return self.retrieve_layer(layer=target_layer, query=query, top_k=top_k)

        # Multi-layer simultaneous retrieval
        all_results = []
        for layer in (0, 1, 2):
            all_results.extend(self.retrieve_layer(layer=layer, query=query, top_k=top_k))

        return all_results[:top_k]

    def _format_doc(self, doc: Document, default_layer: int) -> Dict[str, Any]:
        meta = doc.metadata
        layer = meta.get("raptor_layer", default_layer)
        return {
            "title": meta.get("title", ""),
            "layer": layer,
            "layer_name": "Root Overview" if layer == 0 else ("Section Summary" if layer == 1 else "Detail Leaf"),
            "breadcrumb": meta.get("breadcrumb", ""),
            "url": meta.get("url", ""),
            "parent_id": meta.get("parent_id", ""),
            "small": doc.page_content,
            "big": meta.get("big", meta.get("markdown", doc.page_content)),
        }
#endregion
