#region Imports
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
#endregion

#region Env Loading
_CURRENT_DIR = Path(__file__).resolve().parent
_ROOT_DIR = _CURRENT_DIR.parent
load_dotenv(dotenv_path=_ROOT_DIR / ".env")
load_dotenv(dotenv_path=_CURRENT_DIR / ".env", override=True)

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
) if OPENROUTER_API_KEY else None
#endregion
