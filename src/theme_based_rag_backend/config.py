#region Config
import os
from dotenv import load_dotenv

load_dotenv()

def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set.")
    return val

# OpenRouter Settings
OPENROUTER_API_KEY = require_env("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "deepseek/deepseek-v4-flash-0731")
OPENROUTER_PROVIDER = os.getenv("OPENROUTER_PROVIDER", "baidu")
OPENROUTER_EMBED_MODEL = os.getenv("OPENROUTER_EMBED_MODEL", "nvidia/nemotron-3-embed-1b:free")
OPENROUTER_TEMPERATURE = float(os.getenv("OPENROUTER_TEMPERATURE", "0.2"))

# Server Settings
BACKEND_HOST = require_env("BACKEND_HOST")
BACKEND_PORT = int(require_env("BACKEND_PORT"))

# Qdrant Database Settings
QDRANT_URL = require_env("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Neo4j Database Settings
NEO4J_URI = require_env("NEO4J_URI")
NEO4J_USERNAME = require_env("NEO4J_USERNAME")
NEO4J_PASSWORD = require_env("NEO4J_PASSWORD")

# Chatbot Theme Settings
CHATBOT_THEME = require_env("CHATBOT_THEME")

# LangSmith Settings
LANGSMITH_TRACING = require_env("LANGSMITH_TRACING").lower() == "true"
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
LANGSMITH_PROJECT = require_env("LANGSMITH_PROJECT")

# LLMLingua-2 Context Compression Settings
LLMLINGUA_MODEL = os.getenv("LLMLINGUA_MODEL", "microsoft/llmlingua-2-bert-base-multilingual-cased-meetingbank")
LLMLINGUA_RATE = float(os.getenv("LLMLINGUA_RATE", "0.6"))
LLMLINGUA_DEVICE = os.getenv("LLMLINGUA_DEVICE", "cpu")
#endregion
