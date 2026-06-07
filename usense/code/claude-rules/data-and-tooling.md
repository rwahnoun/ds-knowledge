---
paths:
  - "**/*.py"
  - "**/*.ipynb"
  - "**/pyproject.toml"
---

# Data, Models & Tooling — Usense

- Python 3.11+, packages via `uv`, build with `hatchling`, tests with `pytest`.
- Data models: Pydantic v2 (`BaseModel`) with `computed_field` and `PlainSerializer`.
- ML pipelines: sklearn `Pipeline` + custom transformers.
- Serialization: `joblib` (`.joblib` files).
- Model versioning: `name-Vx.y.z` — `x` signal/model, `y` bugfix, `z` data version.

Workflows:

```bash
ruff check src/ --fix && ruff format src/
python -m pytest src/tests/ -v
python -m pytest src/tests/ --cov=<package>
```
