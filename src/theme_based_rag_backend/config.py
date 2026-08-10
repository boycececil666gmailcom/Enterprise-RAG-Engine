import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

import sys

#region Gemini Settings
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY and "pytest" in sys.modules:
    GEMINI_API_KEY = "dummy_key_for_testing"

GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
_embed_model = os.getenv("GEMINI_EMBED_MODEL", "models/gemini-embedding-001")
if not _embed_model.startswith("models/") and not _embed_model.startswith("tunedModels/"):
    _embed_model = f"models/{_embed_model}"
GEMINI_EMBED_MODEL = _embed_model
GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", "0.0"))
#endregion

# FastAPI server settings
PORT = int(os.getenv("PORT", "8000"))
HOST = os.getenv("HOST", "0.0.0.0")

# Qdrant settings
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# Neo4j settings
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password123")

# Chatbot Theme setting
CHATBOT_THEME = os.getenv("CHATBOT_THEME", "Fintech SaaS platform")

# LangSmith Observability settings
LANGSMITH_TRACING = (os.getenv("LANGSMITH_TRACING") or os.getenv("LANGCHAIN_TRACING_V2") or "false").lower() == "true"
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT") or "pr-virtual-cork-53"
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT") or os.getenv("LANGCHAIN_ENDPOINT") or "https://api.smith.langchain.com"

if LANGSMITH_TRACING:
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    if LANGSMITH_API_KEY:
        os.environ["LANGSMITH_API_KEY"] = LANGSMITH_API_KEY
        os.environ["LANGCHAIN_API_KEY"] = LANGSMITH_API_KEY
    if LANGSMITH_PROJECT:
        os.environ["LANGSMITH_PROJECT"] = LANGSMITH_PROJECT
        os.environ["LANGCHAIN_PROJECT"] = LANGSMITH_PROJECT
    if LANGSMITH_ENDPOINT:
        os.environ["LANGSMITH_ENDPOINT"] = LANGSMITH_ENDPOINT
        os.environ["LANGCHAIN_ENDPOINT"] = LANGSMITH_ENDPOINT
    print(f"\033[1;92m[LangSmith Tracing] Enabled for project: '{LANGSMITH_PROJECT}'\033[0m")





