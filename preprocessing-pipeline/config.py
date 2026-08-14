#region Imports
import os
from pathlib import Path
from dotenv import load_dotenv
#endregion

#region Env Loading
# Load .env file from the module folder or workspace root
_module_env = Path(__file__).resolve().parent / ".env"
_root_env = Path(__file__).resolve().parent.parent / ".env"

if _root_env.exists():
    _ = load_dotenv(dotenv_path=_root_env)
if _module_env.exists():
    _ = load_dotenv(dotenv_path=_module_env, override=True)
#endregion

#region Helpers
def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise ValueError(f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set.")
    return val
#endregion

#region Environment
OPENROUTER_API_KEY = require_env("OPENROUTER_API_KEY")
#endregion
