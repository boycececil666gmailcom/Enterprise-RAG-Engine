#region Imports
import os
from typing import Any, Dict, List, Optional
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode

from .config import GEMINI_API_KEY, GEMINI_EMBED_MODEL, QDRANT_API_KEY, QDRANT_URL
#endregion

#region Configuration
QDRANT_COLLECTION = "raptor_documents"
#endregion

#region Raptor Retriever
class RaptorRetriever:
    """
    RAPTOR 3-Tier Multi-Layer Retriever (Vector DB Only).
    Layer Mapping:
    - Layer 0: Root Global Summaries (Top-level Macro Context)
    - Layer 1: Section Summaries (Category Meso Context)
    - Layer 2: Leaf Detail Chunks (Micro Procedure Context)
    """
    def __init__(self):
        self.dense_embeddings = GoogleGenerativeAIEmbeddings(
            model=GEMINI_EMBED_MODEL,
            google_api_key=GEMINI_API_KEY
        )
        self.sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")
        self.vector_store = QdrantVectorStore.from_existing_collection(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name=QDRANT_COLLECTION,
            content_payload_key="small",
            embedding=self.dense_embeddings,
            sparse_embedding=self.sparse_embeddings,
            retrieval_mode=RetrievalMode.HYBRID
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        target_layer: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieves most relevant chunks from RAPTOR tree.
        - If target_layer is None: Collapsed Tree Search (Searches Layer 0, 1, and 2 simultaneously).
        - If target_layer is set (0, 1, or 2): Filters search to that specific layer.
        """
        filter_dict = None
        if target_layer is not None:
            filter_dict = {"raptor_layer": target_layer}

        raw_docs = self.vector_store.similarity_search(
            query=query,
            k=top_k,
            filter=filter_dict
        )

        results: List[Dict[str, Any]] = []
        for doc in raw_docs:
            meta = doc.metadata
            layer = meta.get("raptor_layer", 2)
            results.append({
                "title": meta.get("title", ""),
                "layer": layer,
                "layer_name": "Root Overview" if layer == 0 else ("Section Summary" if layer == 1 else "Detail Leaf"),
                "breadcrumb": meta.get("breadcrumb", ""),
                "url": meta.get("url", ""),
                "small": doc.page_content,
                "markdown": meta.get("markdown", doc.page_content),
            })

        return results
#endregion
