# region Imports
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# endregion

# region Env Loading
_ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=_ROOT_DIR / ".env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-v4-flash-0731")
OPENROUTER_VISION_MODEL = os.getenv("OPENROUTER_VISION_MODEL", "google/gemini-3.7-flash")
OPENROUTER_PROVIDER_SORT = os.getenv("OPENROUTER_PROVIDER_SORT", "throughput")
OPENROUTER_PROVIDER_IGNORE = os.getenv("OPENROUTER_PROVIDER_IGNORE", "wafer,AtlasCloud")
OPENROUTER_EMBED_MODEL = os.getenv("OPENROUTER_EMBED_MODEL", "nvidia/nemotron-3-embed-1b:free")
# endregion

# region LLM & Embedding Instances
_provider_config = {"allow_fallbacks": True}
if OPENROUTER_PROVIDER_SORT:
    _provider_config["sort"] = OPENROUTER_PROVIDER_SORT
if OPENROUTER_PROVIDER_IGNORE:
    _provider_config["ignore"] = [
        p.strip() for p in OPENROUTER_PROVIDER_IGNORE.split(",") if p.strip()
    ]

_extra_body = {"provider": _provider_config}

# 1. Primary Text LLM (DeepSeek: Cost-effective reasoning & RCA extraction)
llm = (
    ChatOpenAI(
        model=OPENROUTER_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        temperature=0,
        extra_body=_extra_body,
    )
    if OPENROUTER_API_KEY
    else None
)

# 2. Multimodal Vision LLM (Gemini Flash: Analyzing video recordings & screenshot attachments)
vision_llm = (
    ChatOpenAI(
        model=OPENROUTER_VISION_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        temperature=0,
        extra_body=_extra_body,
    )
    if OPENROUTER_API_KEY
    else None
)

# 3. Vector Embeddings
embeddings = (
    OpenAIEmbeddings(
        model=OPENROUTER_EMBED_MODEL,
        api_key=OPENROUTER_API_KEY,
        base_url=OPENROUTER_BASE_URL,
        check_embedding_ctx_length=False,
        model_kwargs={"encoding_format": "float"},
    )
    if OPENROUTER_API_KEY
    else None
)
# endregion

if __name__ == "__main__":
    print(f"[LLM Client] Text Model: {OPENROUTER_MODEL}")
    print(f"[LLM Client] Vision Model: {OPENROUTER_VISION_MODEL}")
    print(f"[LLM Client] Embed Model: {OPENROUTER_EMBED_MODEL}")
    if embeddings:
        vec = embeddings.embed_query("test embedding connection")
        print(f"[LLM Client] Embeddings test success! Vector dimension: {len(vec)}")
    if llm:
        res = llm.invoke("Say 'Text LLM OK'")
        print(f"[LLM Client] Text LLM Response: {res.content}")
    if vision_llm:
        res_v = vision_llm.invoke("Say 'Vision LLM OK'")
        print(f"[LLM Client] Vision LLM Response: {res_v.content}")
