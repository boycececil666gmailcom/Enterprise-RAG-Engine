# Workspace Security Rules

- Treat `*.tfvars`, `*.tfstate`, and `.env` files with high security.
- Do NOT open, view, or inspect `*.tfvars`, `*.tfstate`, or `.env` files without explicit user consent.


# Regarding config.py

- In each Python module, put the acquireing of environment variables inside `config.py` and do not provide any default fallback values.
- Use `require_env(key: str)` to raise an error if the environment variable is not set in `.env`:
  ```python
  def require_env(key: str) -> str:
      val = os.getenv(key)
      if not val:
          raise ValueError(f"CRITICAL CONFIG ERROR: Environment variable '{key}' is required but not set.")
      return val
  ```
