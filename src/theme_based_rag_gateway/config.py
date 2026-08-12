#region Imports & Environment Setup
import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set.")
    return val
#endregion

#region Gateway Server Settings
GATEWAY_HOST = require_env("GATEWAY_HOST")
GATEWAY_PORT = int(require_env("GATEWAY_PORT"))
#endregion

#region Downstream Backend Settings
RAG_BACKEND_URL = require_env("RAG_BACKEND_URL")
#endregion

#region CORS Security Settings
ALLOWED_ORIGINS = require_env("ALLOWED_ORIGINS").split(",")
ALLOW_CREDENTIALS = False if "*" in ALLOWED_ORIGINS else True
#endregion
