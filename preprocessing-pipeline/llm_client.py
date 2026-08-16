#region Imports
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
#endregion

#region Env Loading
_ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=_ROOT_DIR / ".env")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-v4-flash-0731")
OPENROUTER_PROVIDER = os.getenv("OPENROUTER_PROVIDER", "baidu")
OPENROUTER_EMBED_MODEL = os.getenv("OPENROUTER_EMBED_MODEL", "nvidia/nemotron-3-embed-1b:free")
#endregion

#region LLM & Embedding Instances
_extra_body = {}
if OPENROUTER_PROVIDER:
    _extra_body["provider"] = {"order": [OPENROUTER_PROVIDER], "allow_fallbacks": True}

llm = ChatOpenAI(
    model=OPENROUTER_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    temperature=0,
    extra_body=_extra_body if _extra_body else None,
) if OPENROUTER_API_KEY else None

embeddings = OpenAIEmbeddings(
    model=OPENROUTER_EMBED_MODEL,
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    check_embedding_ctx_length=False,
    model_kwargs={"encoding_format": "float"},
) if OPENROUTER_API_KEY else None
#endregion

if __name__ == "__main__":
    print(f"[LLM Client] Model: {OPENROUTER_MODEL}")
    print(f"[LLM Client] Embed Model: {OPENROUTER_EMBED_MODEL}")
    if embeddings:
        vec = embeddings.embed_query("test embedding connection")
        print(f"[LLM Client] Embeddings test success! Vector dimension: {len(vec)}")
    if llm:
        res = llm.invoke("Say 'OK'")
        print(f"[LLM Client] LLM test success! Response: {res.content}")
