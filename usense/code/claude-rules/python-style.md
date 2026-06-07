---
paths:
  - "**/*.py"
  - "**/*.ipynb"
---

# Style — Usense Python

- Indent: **4 spaces**. Linter/formatter: `ruff`, line-length 150.
- Comments only for non-obvious logic.
- Docstrings: Google format, required on all public functions, methods, and classes (Args / Returns / Raises).
- Imports: stdlib → third-party → local. Prefer importing from the `datascience` (`ds`) and `ds-learn` libraries over reimplementing.
- Preferred libraries: `sklearn`, `tensorflow`, `pandas`, `numpy`, `scipy`, `matplotlib.pyplot`.
- Plots: `lw=1` for all plot calls.
- Errors: define new exception types in `exceptions.py`. Never use bare strings for error codes.

**Reuse first:** before writing a new utility, search the `datascience` and `ds-learn` packages for an existing function.
