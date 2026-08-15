#region Vector Stores
from functools import lru_cache

from langchain_core.documents import Document
from langchain_qdrant import FastEmbedSparse, QdrantVectorStore, RetrievalMode
from qdrant_client.http import models as qmodels

from .config import QDRANT_API_KEY, QDRANT_URL
from .llm_client import embeddings


@lru_cache(maxsize=1)
def get_sparse_embeddings() -> FastEmbedSparse | None:
    try:
        return FastEmbedSparse(model_name="Qdrant/bm25")
    except Exception:
        return None


@lru_cache(maxsize=3)
def get_layer_store(layer: int = 2) -> QdrantVectorStore:
    return QdrantVectorStore.from_existing_collection(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=f"raptor_layer_{layer}",
        content_payload_key="small",
        embedding=embeddings,
        sparse_embedding=get_sparse_embeddings(),
        retrieval_mode=RetrievalMode.HYBRID,
    )
#endregion

#region Tree Traversal
def _build_parent_filter(docs: list[Document]) -> qmodels.Filter | None:
    """Builds a Qdrant parent_id filter from document IDs or metadata."""
    ids = [d.id or d.metadata.get("id") for d in docs if d.id or d.metadata.get("id")]
    if not ids:
        return None
    match = qmodels.MatchValue(value=ids[0]) if len(ids) == 1 else qmodels.MatchAny(any=ids)
    return qmodels.Filter(must=[qmodels.FieldCondition(key="metadata.parent_id", match=match)])


def retrieve_layer(
    layer: int,
    query: str,
    top_k: int = 5,
    filter_obj: qmodels.Filter | None = None,
) -> list[Document]:
    return get_layer_store(layer).similarity_search(query=query, k=top_k, filter=filter_obj)


def retrieve_tree_traversal(
    query: str,
    top_k_layer0: int = 2,
    top_k_layer1: int = 3,
    top_k_layer2: int = 5,
) -> list[Document]:
    """Executes top-down hierarchical tree traversal across RAPTOR layers (Root -> Section -> Leaf)."""
    root_docs = retrieve_layer(0, query, top_k_layer0)
    sec_docs = retrieve_layer(1, query, top_k_layer1, _build_parent_filter(root_docs))
    leaf_docs = retrieve_layer(2, query, top_k_layer2, _build_parent_filter(sec_docs))
    return leaf_docs or retrieve_layer(2, query, top_k_layer2)
#endregion
