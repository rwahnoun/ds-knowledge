# RAG Method Comparison Plan

**Goal:** Find the best token-efficient way to give Claude access to the Usense codebases and Obsidian vault. Compare quality, token cost, and speed across four retrieval methods.

**Repos under test:** `datascience`, `ds-scripts`, `ds-learn`, `ds-knowledge` (Obsidian vault)
**Report output:** `D:\code\ds-knowledge\meta\compareReport\`

---

## Methods

| # | Method | Covers | Status |
|---|---|---|---|
| A | **Repomix** | code + vault | to set up |
| B | **code-review-graph MCP** | code only | already installed |
| C | **ChromaDB-MCP** (hybrid BM25 + vector) | code + vault | to set up |
| D | **Kuzu** (embedded graph DB) | code + vault | to set up |
| E | **Vault-MCP** | vault only | to set up |

---

## Test Questions

Designed to stress-test different retrieval strengths: structural/relational (graph wins), semantic/fuzzy (ChromaDB wins), broad synthesis (repomix may hit token limits), specific fact lookup (all compete on efficiency).

### Code repos (datascience · ds-scripts · ds-learn)

| # | Question | Expected winner |
|---|---|---|
| Q01 | What functions or methods call `Record` across all three repos? | graph (B, D) |
| Q02 | How does the signal processing pipeline work from raw measurement to final output? | semantic (C) |
| Q03 | What public methods does the `Dataset` class expose, and what do they do? | structural (B, D) |
| Q04 | Which scripts in ds-scripts depend on the `ds` package, and what do they import from it? | graph (D) |
| Q05 | What file formats are supported for data loading across the repos? | semantic (C) |
| Q06 | What ML or statistical models are used or implemented across the three repos? | semantic (C) |

### Obsidian vault (ds-knowledge)

| # | Question | Expected winner |
|---|---|---|
| Q07 | What is the Jimini device and how does it work? | fact lookup (all) |
| Q08 | What biomarkers is Usense targeting, and what are the measurement principles for each? | semantic (C, E) |
| Q09 | What is the Dataset / Record / Component data model and how do the three relate? | fact lookup |
| Q10 | What are the key regulatory and QARA considerations for the Usense device? | semantic (C, E) |

---

## Setup Plan

### A — Repomix

1. Install: `npm install -g repomix`
2. For each repo: `repomix --output <repo>-packed.xml <repo-path>`
3. For vault: run repomix on `ds-knowledge/`
4. At query time: paste packed file into Claude context + question
5. **UI:** none — output is a plain text/XML file; open in any editor

### B — code-review-graph MCP *(already installed)*

1. Verify graph is built: use `get_architecture_overview` tool
2. Rebuild if needed: `build_or_update_graph_tool`
3. At query time: use MCP tools (`semantic_search_nodes`, `query_graph`, etc.)
4. **UI:** no dedicated graph viewer; use `generate_wiki_tool` for structured docs or `list_communities_tool` for cluster overview

### C — ChromaDB-MCP (hybrid BM25 + vector)

1. Install ChromaDB locally: `pip install chromadb`
2. Install sentence-transformers for local embeddings: `pip install sentence-transformers`
3. Install Chroma MCP server: `pip install chroma-mcp`
4. Index repos and vault: write indexing script (`meta/setup/index_chroma.py`)
   - Chunk files (500 tokens, 50 overlap)
   - Embed with `all-MiniLM-L6-v2` (local, free)
   - Store with BM25 metadata for hybrid search
5. Add to Claude Code MCP config: `claude mcp add chroma`
6. At query time: MCP tool retrieves top-k chunks hybrid-ranked
7. **UI:** install `chromadb-ui` via Docker or `pip install chroma-ui` — browse collections, inspect chunks, view embedding metadata at `http://localhost:3000`

### D — Kuzu (embedded graph DB)

1. Install: `pip install kuzu`
2. Parse repos with Tree-sitter: extract nodes (functions, classes, modules) and edges (calls, imports, inherits)
3. Parse vault: extract notes as nodes, wikilinks as edges
4. Write graph builder script (`meta/setup/build_kuzu.py`)
5. Install or build Kuzu MCP server
6. At query time: Cypher-style query returns relevant subgraph only
7. **UI:** install Kuzu Explorer — `pip install kuzu-explorer` then `kuzu-explorer <db-path>` — opens browser UI at `http://localhost:8000` with interactive graph view and Cypher query console

### E — Vault-MCP

1. Install Vault-MCP: `pip install vault-mcp` (or clone from GitHub)
2. Point at `ds-knowledge/` vault root
3. Add to Claude Code MCP config: `claude mcp add vault`
4. At query time: semantic search returns relevant note chunks
5. **UI:** use Obsidian's built-in **Graph View** (free, already available) — shows wikilink graph visually. For query-based views install the **Dataview** plugin in Obsidian

---

## Token Measurement

To get accurate per-query token counts, run each query via the **Anthropic Python SDK** directly (not through Claude Code UI), which returns `usage.input_tokens` and `usage.output_tokens` in the response.

Write a test harness: `meta/setup/run_benchmark.py`

```python
# pseudo-structure
for question in QUESTIONS:
    for method in METHODS:
        context = method.retrieve(question)
        response = anthropic.messages.create(
            model="claude-sonnet-4-6",
            messages=[{"role": "user", "content": context + "\n\n" + question}]
        )
        record(question, method, response.usage, response.content, elapsed_time)
```

**Metrics per query per method:**
- `input_tokens` — context sent to Claude
- `output_tokens` — Claude's answer
- `total_tokens` = input + output
- `latency_s` — wall-clock time from query to full response
- `quality_score` — your 1–5 subjective rating

---

## Report Format

One file per question in `compareReport/`:

```
compareReport/
  q01.md  …  q10.md      ← one file per question
  summary.md              ← final comparison table
```

Each `qNN.md` has sections: question → method A response + tokens → method B → … → your rating notes.

`summary.md` has:

| Q | Method A tokens | B tokens | C tokens | D tokens | E tokens | Winner (quality) | Winner (tokens) |
|---|---|---|---|---|---|---|---|
| Q01 | | | | | | | |
| … | | | | | | | |
| **Total** | | | | | | | |

---

## Order of Execution

1. Set up and verify each method (one at a time)
2. Run `run_benchmark.py` for all 10 questions × all applicable methods
3. Fill in quality scores manually
4. Write `summary.md`
5. Draw conclusions — pick the winner or the best hybrid setup

---

## Open Questions Before Starting

- [ ] Which Python venv to use for indexing scripts? (`py312` assumed)
- [ ] Confirm Kuzu MCP server availability (may need to build a thin wrapper)
- [ ] Decide chunk size for ChromaDB (start with 500 tokens, adjust if quality is poor)
