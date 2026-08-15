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
def _build_parent_filter(parent_ids: list[str]) -> qmodels.Filter | None:
    ids = [pid for pid in parent_ids if pid]
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
    store = get_layer_store(layer)
    try:
        return store.similarity_search(query=query, k=top_k, filter=filter_obj)
    except Exception:
        return store.similarity_search(query=query, k=top_k)


def retrieve_tree_traversal(
    query: str,
    top_k_layer0: int = 2,
    top_k_layer1: int = 3,
    top_k_layer2: int = 5,
) -> list[Document]:
    """Executes top-down hierarchical tree traversal across RAPTOR layers (Root -> Section -> Leaf)."""
    # 1. Root search
    root_docs = retrieve_layer(0, query, top_k_layer0)
    root_ids = [d.metadata.get("id", "") for d in root_docs]

    # 2. Section search under matched Roots
    sec_docs = retrieve_layer(1, query, top_k_layer1, _build_parent_filter(root_ids))
    sec_ids = [d.metadata.get("id", "") for d in sec_docs]

    # 3. Leaf detail search under matched Sections (fallback to global search if empty)
    leaf_docs = retrieve_layer(2, query, top_k_layer2, _build_parent_filter(sec_ids))
    return leaf_docs or retrieve_layer(2, query, top_k_layer2)
#endregion
