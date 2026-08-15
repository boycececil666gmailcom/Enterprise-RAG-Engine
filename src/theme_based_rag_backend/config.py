#region Config
import os
from dotenv import load_dotenv

load_dotenv()

def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set.")
    return val

# Gemini Settings
GEMINI_API_KEY = require_env("GEMINI_API_KEY")
GEMINI_MODEL = require_env("GEMINI_MODEL")
_raw_embed = require_env("GEMINI_EMBED_MODEL").removeprefix("models/")
GEMINI_EMBED_MODEL = "gemini-embedding-001" if _raw_embed == "text-embedding-004" else _raw_embed
GEMINI_TEMPERATURE = float(require_env("GEMINI_TEMPERATURE"))

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
#endregion
