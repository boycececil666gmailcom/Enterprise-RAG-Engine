#region Imports & Configuration
import os
import sys
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set.")
    return val
#endregion

#region Gemini Settings
GEMINI_API_KEY = require_env("GEMINI_API_KEY")
GEMINI_MODEL = require_env("GEMINI_MODEL")
GEMINI_EMBED_MODEL = require_env("GEMINI_EMBED_MODEL")
GEMINI_TEMPERATURE = float(require_env("GEMINI_TEMPERATURE"))
#endregion

#region FastAPI Server Settings
BACKEND_PORT = int(require_env("BACKEND_PORT"))
BACKEND_HOST = require_env("BACKEND_HOST")
#endregion

#region Qdrant Database Settings
QDRANT_URL = require_env("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
#endregion

#region Neo4j Database Settings
NEO4J_URI = require_env("NEO4J_URI")
NEO4J_USERNAME = require_env("NEO4J_USERNAME")
NEO4J_PASSWORD = require_env("NEO4J_PASSWORD")
#endregion

#region Chatbot Theme Settings
CHATBOT_THEME = require_env("CHATBOT_THEME")
#endregion

#region LangSmith Settings
LANGSMITH_TRACING = require_env("LANGSMITH_TRACING").lower() == "true"
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
LANGSMITH_PROJECT = require_env("LANGSMITH_PROJECT")
#endregion
