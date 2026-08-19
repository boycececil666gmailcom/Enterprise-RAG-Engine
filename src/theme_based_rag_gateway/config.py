# region Config
import os

from dotenv import load_dotenv

load_dotenv()


def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(
            f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set."
        )
    return val


# Gateway Server Settings
GATEWAY_HOST = require_env("GATEWAY_HOST")
GATEWAY_PORT = int(require_env("GATEWAY_PORT"))

# Downstream Backend Settings
RAG_BACKEND_URL = require_env("RAG_BACKEND_URL")

# CORS Security Settings
ALLOWED_ORIGINS = [
    origin.strip() for origin in require_env("ALLOWED_ORIGINS").split(",")
]
ALLOW_CREDENTIALS = "*" not in ALLOWED_ORIGINS
# endregion
