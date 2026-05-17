# RAG Method Comparison Plan

**Goal:** Find the best token-efficient way to give Claude access to the Usense codebases and Obsidian vault. Compare quality, token cost, and speed across five retrieval methods, then adopt the winner as the permanent MCP setup.

**Repos under test:** `datascience`, `ds-scripts`, `ds-learn`, `ds-knowledge` (Obsidian vault)
**Report output:** `D:\code\ds-knowledge\meta\compareReport\`
**Operations reference:** [[compareReadme]]
**Estimated effort:** 2–3 days setup · half a day benchmarking

---

## Methods

| # | Method | Covers | Status |
|---|---|---|---|
| A | **Repomix** | code + vault | to set up |
| B | **code-review-graph MCP** | code only | already installed |
| C | **ChromaDB-MCP** (vector search) | code + vault | to set up |
| D | **Kuzu** (embedded graph DB) | code + vault | to set up |
| E | **Vault-MCP** | vault only | to set up |
| F | **graphify** (AST + semantic graph) | code only (free) · vault (token cost) | installed · datascience built · ds-knowledge building |

> **Note on hybrid BM25+vector for ChromaDB:** ChromaDB does not support hybrid search natively. True hybrid (BM25 + vector with reciprocal rank fusion) requires a separate `rank_bm25` index and manual fusion logic. For this benchmark, Method C uses pure vector search. Hybrid can be added as a follow-up if C shows promise.

> **Note on Smart Connections MCP:** evaluated during planning, excluded because Vault-MCP (E) is more actively maintained and purpose-built for local-first use without the Smart Connections plugin dependency.

> **Note on graphify vault cost:** graphify uses Claude subagents to extract entities from markdown files. Running it on `ds-knowledge` will cost tokens at build time (similar to the GraphRAG we excluded). It caches aggressively — only changed files are re-processed on `--update`. Method F is therefore included for code repos (free, AST-only) and listed as optional/flagged for the vault.

---

## Method × Question Coverage

Methods B and E do not cover all domains. Questions they cannot answer get **N/A** in the report — not a score of zero.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Code questions (Q01–Q06) | — ¹ | ✓ | ✓ | ✓ | — | ✓ |
| Vault questions (Q07–Q10) | ✓ | — | ✓ | ✓ | ✓ | optional* |
| Cross-domain (Q11) | — ¹ | — | ✓ | ✓ | — | optional* |

¹ Repomix code repos are 1M–14M tokens — too large even for the 1M context model. Vault (316k) fits.
*graphify can index the vault but costs Claude tokens at build time — run vault queries with F only if you want to compare despite the build cost.

---

## Test Questions

Designed to stress-test different retrieval strengths: structural/relational (graph wins), semantic/fuzzy (vector wins), broad synthesis (Repomix may hit token limits), specific fact lookup (all compete on efficiency).

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

### Cross-domain

| # | Question | Expected winner |
|---|---|---|
| Q11 | How does the `Dataset` class in code relate to its description in the knowledge vault — are they consistent? | coverage (A, C, D) |

---

## Quality Scoring Rubric

All questions scored 1–5 by Remy after reading each response:

| Score | Meaning |
|---|---|
| 1 | Wrong, hallucinated, or completely off-topic |
| 2 | Partially relevant but missing key facts or confused |
| 3 | Correct but incomplete — covers the main point, misses nuance |
| 4 | Correct and reasonably complete |
| 5 | Complete, accurate, concise, nothing to add |

---

## Setup Plan

### Pre-flight: Repomix token size check — COMPLETE

Results (repomix o200k_base token counts):

| Repo | Tokens | Verdict |
|---|---|---|
| datascience | 9,438,994 | disqualified — exceeds 1M context |
| ds-scripts | 1,238,692 | disqualified — exceeds 1M context |
| ds-learn | 14,693,433 | disqualified — exceeds 1M context |
| ds-knowledge (vault) | 316,473 | **viable** — fits in 1M context model |

**Method A (Repomix) scope: vault only (Q07–Q11).** Code repos are too large even for the 1M context window. The vault at 316k tokens is a reasonable full-context load — no filtering needed for now.

### Indexing exclusions

Apply these exclusions when building indexes for all methods (ChromaDB, Kuzu, Vault-MCP):

**Code repos — exclude:**
- `__pycache__/`, `*.pyc`
- `.git/`
- `venvs/`, `env/`, `.venv/`
- `*.egg-info/`
- test fixtures / large binary files

**Vault — exclude:**
- `meta/` (the comparison files themselves)
- `.obsidian/`
- `*.canvas` (not prose)

### A — Repomix

1. Install: `npm install -g repomix`
2. Run pre-flight token size check (above)
3. Pack each repo and vault with exclusions:
   ```powershell
   repomix --ignore "__pycache__,*.pyc,.git,venvs" --output D:\code\meta\datascience-packed.xml D:\code\datascience
   repomix --ignore ".obsidian,meta" --output D:\code\meta\vault-packed.xml D:\code\ds-knowledge
   ```
4. At query time: full packed file is passed as context to Claude
5. **UI:** none — plain XML file, open in any editor

### B — code-review-graph MCP *(already installed)*

1. Verify graph is built: use `get_architecture_overview` tool
2. Rebuild if needed: `build_or_update_graph_tool`
3. At query time: use MCP tools (`semantic_search_nodes`, `query_graph`, etc.)
4. Does **not** cover vault — Q07–Q11 are N/A
5. **UI:** no dedicated visual viewer; use `generate_wiki_tool` or `list_communities_tool`

### C — ChromaDB-MCP (vector search)

**Pinned versions:** `chromadb==0.5.x`, `sentence-transformers==3.x`

1. Install:
   ```powershell
   pip install "chromadb==0.5.*" "sentence-transformers==3.*" chroma-mcp
   ```
2. Write indexing script `meta/setup/index_chroma.py`:
   - Chunk files: 500 tokens, 50-token overlap (code); note-level chunks for vault (one chunk per note, preserving whole notes rather than splitting)
   - Embed with `all-MiniLM-L6-v2` (local, free, ~80MB)
   - Apply exclusions listed above
3. Run indexer:
   ```powershell
   python meta/setup/index_chroma.py --repo D:\code\datascience
   python meta/setup/index_chroma.py --repo D:\code\ds-scripts
   python meta/setup/index_chroma.py --repo D:\code\ds-learn
   python meta/setup/index_chroma.py --vault D:\code\ds-knowledge
   ```
4. Add to Claude Code MCP config: `claude mcp add chroma`
5. At query time: MCP tool retrieves top-k chunks by vector similarity
6. **UI:** `chroma-ui` — see [[compareReadme]] for launch instructions

### D — Kuzu (embedded graph DB)

**Pinned versions:** `kuzu==0.7.x`, `tree-sitter==0.23.x`

1. Install:
   ```powershell
   pip install "kuzu==0.7.*" "tree-sitter==0.23.*" tree-sitter-python kuzu-mcp
   ```
2. Write graph builder `meta/setup/build_kuzu.py`:
   - Code: Tree-sitter parses functions, classes, modules → nodes; calls, imports, inherits → edges
   - Vault: notes → nodes; wikilinks → edges; tags → node properties
   - Apply exclusions listed above
3. Run builder:
   ```powershell
   python meta/setup/build_kuzu.py --repo D:\code\datascience
   python meta/setup/build_kuzu.py --repo D:\code\ds-scripts
   python meta/setup/build_kuzu.py --repo D:\code\ds-learn
   python meta/setup/build_kuzu.py --vault D:\code\ds-knowledge
   ```
4. Add Kuzu MCP to Claude Code: `claude mcp add kuzu-mcp`
5. At query time: Cypher-style query returns relevant subgraph only
6. **UI:** Kuzu Explorer — see [[compareReadme]] for launch instructions

### E — Vault-MCP

**Pinned versions:** install from GitHub until stable PyPI release confirmed

1. Install:
   ```powershell
   pip install "git+https://github.com/robbiemu/vault-mcp"
   ```
2. Configure to point at vault root and apply exclusions (`.obsidian`, `meta/`)
3. Add to Claude Code MCP config: `claude mcp add vault`
4. At query time: semantic search returns relevant note chunks (quality-based chunking — low-signal chunks are discarded automatically)
5. Does **not** cover code repos — Q01–Q06 are N/A
6. **UI:** Obsidian Graph View + Dataview plugin — see [[compareReadme]]

> **Vault chunking note:** Vault-MCP uses quality-based chunking (scores and discards low-signal chunks) rather than fixed-size chunking. Method C uses fixed 500-token chunks for vault. This means vault retrieval quality is not directly apples-to-apples between C and E — note this when scoring Q07–Q10.

---

## Token Measurement

The Anthropic Python SDK returns exact `usage.input_tokens` and `usage.output_tokens` per response. Run all queries through the SDK — not through Claude Code UI — for comparable counts.

**Important:** MCP-based methods (B, C, D, E) cannot be invoked via the SDK directly. The benchmark harness calls each method's **underlying storage client** (ChromaDB Python client, Kuzu Python client, etc.) to retrieve context, then passes that context to the SDK. This means the benchmark measures retrieval quality as seen by Claude, independent of MCP overhead.

Write `meta/setup/run_benchmark.py`:

```python
# Pseudo-structure — real implementation in the script
import anthropic, time, json

client = anthropic.Anthropic()
results = []

for q in QUESTIONS:
    for method in applicable_methods(q):
        context = method.retrieve(q.text)   # calls DB client directly
        t0 = time.time()
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            messages=[{"role": "user", "content": context + "\n\n" + q.text}]
        )
        latency = time.time() - t0
        results.append({
            "question": q.id,
            "method": method.id,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
            "latency_s": round(latency, 2),
            "response": response.content[0].text,
        })

json.dump(results, open("meta/compareReport/raw_results.json", "w"), indent=2)
```

**Metrics recorded per query per method:**
- `input_tokens` — context sent to Claude
- `output_tokens` — Claude's answer length
- `total_tokens` = input + output
- `latency_s` — wall-clock seconds from query to full response
- `quality_score` — your 1–5 rating added manually after reading

---

## Report Format

```
compareReport/
  raw_results.json    ← machine output from run_benchmark.py
  q01.md … q11.md    ← one file per question, all methods side by side
  summary.md          ← final comparison table
```

Each `qNN.md` structure:
```
# Q01 — <question text>

## Method A — Repomix
**Tokens:** input=X output=Y total=Z | **Latency:** Xs
<response>
**Quality score:** /5 — <notes>

## Method B — code-review-graph
...
```

`summary.md` table:

| Q | A tokens | B tokens | C tokens | D tokens | E tokens | F tokens | Latency winner | Quality winner |
|---|---|---|---|---|---|---|---|---|
| Q01 | N/A | | | | N/A | | | |
| Q02 | N/A | | | | N/A | | | |
| Q03 | N/A | | | | N/A | | | |
| Q04 | N/A | | | | N/A | | | |
| Q05 | N/A | | | | N/A | | | |
| Q06 | N/A | | | | N/A | | | |
| Q07 | | N/A | | | | opt | | |
| Q08 | | N/A | | | | opt | | |
| Q09 | | N/A | | | | opt | | |
| Q10 | | N/A | | | | opt | | |
| Q11 | N/A | N/A | | | N/A | opt | | |
| **Total** | | | | | | | | |

---

## Order of Execution

1. Run pre-flight Repomix token size check — disqualify if over 150k tokens per repo
2. Set up and verify each method one at a time (test with a single question before full run)
3. Run `run_benchmark.py` — all 11 questions × applicable methods
4. Read responses, add quality scores manually to each `qNN.md`
5. Fill in `summary.md`
6. Draw conclusions — pick the winner or the best hybrid combination
7. **Adopt winner as permanent MCP setup** — update Claude Code MCP config and remove others

---

### F — graphify (AST + semantic graph)

**Pinned versions:** `graphifyy` (note double-y — that's the PyPI package name)

1. Install:
   ```powershell
   pip install graphifyy
   ```
2. Run on code repos (free — AST only, no Claude tokens):
   ```powershell
   cd D:\code\datascience
   graphify . --no-viz          # builds graph, skips HTML for speed
   ```
   Repeat for `ds-scripts` and `ds-learn`.
3. Start the MCP server to expose the graph to Claude Code:
   ```powershell
   graphify . --mcp             # starts stdio MCP server
   ```
   Or add to Claude Code MCP config so it starts automatically.
4. **Optional — vault indexing (costs tokens):** only run if you want to compare F on vault questions:
   ```powershell
   cd D:\code\ds-knowledge
   graphify . --ignore ".obsidian,meta" --no-viz
   ```
5. For incremental updates after code changes:
   ```powershell
   graphify . --update          # re-extracts only changed files
   ```
6. At query time: use `/graphify query "<question>"` or MCP tools (`query_graph`, `get_node`, `shortest_path`, etc.)
7. **UI:** graphify generates `graphify-out/graph.html` — open in any browser. Interactive graph with community coloring, no server needed. Also exports to GraphML for Gephi/yEd.

---

## Open Questions Before Starting

- [ ] Confirm `kuzu-mcp` is the correct package name on PyPI
- [ ] Confirm `vault-mcp` PyPI status vs GitHub install
- [ ] Decide whether to run graphify on the vault (token cost) or code-only
- [ ] Decide whether to pursue hybrid BM25+vector for ChromaDB as a follow-up (Method C+)
- [ ] Chunk size for code in ChromaDB: start at 500 tokens, adjust after first test run
