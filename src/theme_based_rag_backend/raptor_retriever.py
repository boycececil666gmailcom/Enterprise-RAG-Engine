#region Retriever
from typing import Any

from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode

from .config import GEMINI_API_KEY, GEMINI_EMBED_MODEL, QDRANT_API_KEY, QDRANT_URL


class RaptorRetriever:
    """RAPTOR 3-Tier Multi-Layer Retriever for hierarchical tree traversal."""

    def __init__(self):
        self.dense_embeddings = GoogleGenerativeAIEmbeddings(
            model=GEMINI_EMBED_MODEL,
            google_api_key=GEMINI_API_KEY,
        )
        self.sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

        self.layer_stores: dict[int, QdrantVectorStore] = {
            layer: QdrantVectorStore.from_existing_collection(
                url=QDRANT_URL,
                api_key=QDRANT_API_KEY,
                collection_name=f"raptor_layer_{layer}",
                content_payload_key="small",
                embedding=self.dense_embeddings,
                sparse_embedding=self.sparse_embeddings,
                retrieval_mode=RetrievalMode.HYBRID,
            )
            for layer in (0, 1, 2)
        }

    def retrieve_layer(
        self,
        layer: int,
        query: str,
        top_k: int = 5,
        filter_dict: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
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
        top_k_layer2: int = 3,
    ) -> dict[str, Any]:
        """Executes top-down hierarchical tree traversal across RAPTOR layers."""
        layer_0 = self.retrieve_layer(0, query, top_k=top_k_layer0)

        layer_1: list[dict[str, Any]] = []
        for root in layer_0:
            root_id = root.get("id", "")
            f_l1 = {"parent_id": root_id} if root_id else None
            layer_1.extend(self.retrieve_layer(1, query, top_k=top_k_layer1, filter_dict=f_l1))

        if not layer_1:
            layer_1 = self.retrieve_layer(1, query, top_k=top_k_layer1)

        layer_2: list[dict[str, Any]] = []
        for sec in layer_1:
            sec_id = sec.get("id", "")
            f_l2 = {"parent_id": sec_id} if sec_id else None
            layer_2.extend(self.retrieve_layer(2, query, top_k=top_k_layer2, filter_dict=f_l2))

        if not layer_2:
            layer_2 = self.retrieve_layer(2, query, top_k=top_k_layer2)

        return {
            "root_overview": layer_0,
            "section_summaries": layer_1,
            "leaf_chunks": layer_2,
        }

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        target_layer: int | None = None,
    ) -> list[dict[str, Any]]:
        """Retrieves relevant documents from specific or all layers."""
        if target_layer is not None:
            return self.retrieve_layer(layer=target_layer, query=query, top_k=top_k)

        all_results = []
        for layer in (0, 1, 2):
            all_results.extend(self.retrieve_layer(layer=layer, query=query, top_k=top_k))
        return all_results[:top_k]

    def _format_doc(self, doc: Document, default_layer: int) -> dict[str, Any]:
        meta = doc.metadata
        layer = meta.get("raptor_layer", default_layer)
        layer_names = {0: "Root Overview", 1: "Section Summary", 2: "Detail Leaf"}
        return {
            "title": meta.get("title", ""),
            "layer": layer,
            "layer_name": layer_names.get(layer, "Detail Leaf"),
            "breadcrumb": meta.get("breadcrumb", ""),
            "url": meta.get("url", ""),
            "parent_id": meta.get("parent_id", ""),
            "small": doc.page_content,
            "big": meta.get("big", meta.get("markdown", doc.page_content)),
        }
#endregion
