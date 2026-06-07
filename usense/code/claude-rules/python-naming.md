---
paths:
  - "**/*.py"
  - "**/*.ipynb"
---

# Naming — Usense Python

**Strict — no underscores in variables, functions, or methods.**

| Element | Convention | Example |
|---------|------------|---------|
| Variables, functions, methods | `camelCase` | `xTest`, `trainModel()` |
| Classes | `PascalCase` | `FleetPDS`, `SignalProcessor` |
| Constants | `UPPER_CASE` | `MAX_ITERATIONS` |

Standard abbreviations: `src` (source), `tgt` (target), `ds` (dataset), `sid` (sampleId), `rec` (record), `slc` (slice/component), `cfg` (config), `val` (value), `res` (result), `idx` (index), `df` (DataFrame).

Train/test splits — suffix form only:

- ✅ `xTr` `xTe` `xVal` / `yTr` `yTe` `yVal` / `idxTr` `idxTe` `idxVal`
- ❌ `X_train` `X_test` `X_val` / `y_train` `y_test` `y_val` / `idx_train` `idx_test` `idx_val`

Class members: default **all public**. No leading underscores unless explicitly requested.
