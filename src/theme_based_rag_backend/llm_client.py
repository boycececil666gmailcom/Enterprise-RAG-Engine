#region LLM Clients
from flashrank import Ranker
from langchain_community.document_compressors.flashrank_rerank import FlashrankRerank
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from .config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
    OPENROUTER_EMBED_MODEL,
    OPENROUTER_MODEL,
    OPENROUTER_PROVIDER,
    OPENROUTER_TEMPERATURE,
)

_extra_body = {"provider": {"order": [OPENROUTER_PROVIDER], "allow_fallbacks": True}} if OPENROUTER_PROVIDER else None

# Primary LLM instance for standard generation (DeepSeek via OpenRouter)
llm = ChatOpenAI(
    model=OPENROUTER_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    temperature=OPENROUTER_TEMPERATURE,
    extra_body=_extra_body,
)

# LLM instance configured with lower temperature for HyDE passage generation
hyde_llm = ChatOpenAI(
    model=OPENROUTER_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    temperature=0.0,
    extra_body=_extra_body,
)

# Shared embeddings client for vector store and theme similarity
embeddings = OpenAIEmbeddings(
    model=OPENROUTER_EMBED_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    check_embedding_ctx_length=False,
    model_kwargs={"encoding_format": "float"},
)

# Shared Cross-Encoder reranker instance
reranker = FlashrankRerank(client=Ranker(), top_n=5)
#endregion
