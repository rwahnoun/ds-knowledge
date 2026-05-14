# RAG Methods — Operations Reference

How to use, update, maintain, and visualize each method in the comparison.
See [[compare]] for the full plan and benchmark structure.

---

## A — Repomix

### Use
Run repomix to pack a repo or vault into a single file, then paste that file into Claude's context alongside your question.

```powershell
# Pack a code repo
repomix --output D:\code\meta\datascience-packed.xml D:\code\datascience

# Pack the Obsidian vault
repomix --output D:\code\meta\vault-packed.xml D:\code\ds-knowledge
```

The output XML file goes directly into Claude's context window at query time.

### Update
Re-run the same command. Repomix always does a full re-pack — no incremental update. Add it to a script or run manually before benchmarking.

### Maintain
Nothing to maintain. No index, no database. The packed file is disposable — regenerate whenever the source changes.

### UI
No dedicated UI. The output is plain XML/text — open in VS Code or any editor to inspect what was packed. Use `repomix --help` for filtering options (e.g. exclude `node_modules`, `.git`).

---

## B — code-review-graph MCP

### Use
Already wired into Claude Code. Use MCP tools directly in conversation:

| Tool | Purpose |
|---|---|
| `semantic_search_nodes` | Find functions/classes by keyword |
| `query_graph` | Trace callers, callees, imports, tests |
| `get_architecture_overview` | High-level structure |
| `get_impact_radius` | Blast radius of a change |
| `get_review_context` | Source snippets for review |
| `list_communities` | Cluster overview |
| `generate_wiki_tool` | Structured docs from graph |

### Update
The graph auto-updates via file-watch hooks when you edit files. To force a full rebuild:

```
Use build_or_update_graph_tool in Claude Code
```

### Maintain
- Graph lives in the MCP server's local storage (check MCP config for path)
- If graph seems stale: `detect_changes` first, then `build_or_update_graph_tool`
- No manual indexing needed for day-to-day use

### UI
No dedicated visual graph browser. Use these tools for structured views:
- `list_communities_tool` — shows code clusters
- `generate_wiki_tool` — renders a navigable wiki from the graph
- `get_architecture_overview` — text summary of modules and relationships

---

## C — ChromaDB-MCP

### Use
After setup, ChromaDB is available as an MCP tool in Claude Code. It retrieves the most relevant chunks for your query using hybrid BM25 + vector search.

At query time Claude automatically calls the chroma MCP tool — no manual steps needed.

To query directly from Python:

```python
import chromadb
client = chromadb.PersistentClient(path="D:/code/meta/chroma_db")
collection = client.get_collection("datascience")
results = collection.query(query_texts=["signal processing pipeline"], n_results=5)
```

### Update
Re-run the indexing script when files change:

```powershell
cd D:\code\venvs\py312\Scripts; .\activate
python D:\code\ds-knowledge\meta\setup\index_chroma.py --repo datascience
python D:\code\ds-knowledge\meta\setup\index_chroma.py --vault
```

The script uses upsert so unchanged chunks are skipped — incremental update is fast.

### Maintain
- DB lives at `D:\code\meta\chroma_db\` (persistent on disk)
- If you rename or delete files: run with `--clean` flag to remove stale chunks
- Check collection stats: `client.get_collection("datascience").count()`
- No server to restart — ChromaDB runs in-process via `PersistentClient`

### UI
Install and run Chroma UI:

```powershell
# Option 1: pip
pip install chroma-ui
chroma-ui --db D:\code\meta\chroma_db

# Option 2: Docker
docker run -p 3000:3000 -v D:\code\meta\chroma_db:/data chromadb/chroma-ui
```

Open `http://localhost:3000` — browse collections, inspect individual chunks, view embedding metadata, run test queries. Useful for checking that chunking and indexing look sane before benchmarking.

For 3D embedding visualization (optional):
- Export vectors from ChromaDB to JSON
- Load into [TensorFlow Embedding Projector](https://projector.tensorflow.org/) — shows semantic clusters visually

---

## D — Kuzu (embedded graph DB)

### Use
After setup, Kuzu is available via MCP. Claude queries it with Cypher-style graph traversal.

To query directly from Python:

```python
import kuzu
db = kuzu.Database("D:/code/meta/kuzu_db")
conn = kuzu.Connection(db)

# Example: find all callers of a function
result = conn.execute("""
    MATCH (caller:Function)-[:CALLS]->(callee:Function {name: 'Record'})
    RETURN caller.name, caller.module
""")
```

### Update
Re-run the graph builder when code or vault changes:

```powershell
python D:\code\ds-knowledge\meta\setup\build_kuzu.py --repo datascience
python D:\code\ds-knowledge\meta\setup\build_kuzu.py --vault
```

Builder uses Tree-sitter for code (functions, classes, imports, calls) and markdown parsing for vault (notes as nodes, wikilinks as edges). Drops and rebuilds affected nodes on update.

### Maintain
- DB lives at `D:\code\meta\kuzu_db\` (embedded, no server)
- No daemon to manage — opens and closes with each script run
- If schema changes (e.g. adding edge types): delete `kuzu_db/` and rebuild from scratch
- Check node/edge counts via Python or Kuzu Explorer

### UI
Install and launch Kuzu Explorer:

```powershell
pip install kuzu-explorer
kuzu-explorer D:\code\meta\kuzu_db
```

Opens at `http://localhost:8000`. Features:
- Interactive graph visualization — click nodes to expand neighbors
- Cypher query console — run queries and see results as graph or table
- Schema browser — see all node/edge types and their properties

This is the richest UI of all the methods. Use it to:
- Verify the code graph looks correct (functions → calls → modules)
- Explore the vault graph (notes → wikilinks → notes)
- Debug missing nodes or wrong edge directions

---

## E — Vault-MCP

### Use
After setup, Vault-MCP is available as an MCP tool. Claude calls it automatically when answering vault questions. It returns semantically relevant note chunks.

To test a query directly:

```powershell
vault-mcp query --vault D:\code\ds-knowledge --q "Jimini device"
```

### Update
Vault-MCP watches the vault directory and re-indexes on file changes automatically. To force a full re-index:

```powershell
vault-mcp reindex --vault D:\code\ds-knowledge
```

### Maintain
- Index stored locally (check Vault-MCP config for path, typically `~/.vault-mcp/`)
- No server to manage — runs as an MCP subprocess
- If note quality is poor: tune chunking strategy in Vault-MCP config (quality-based chunking is its default — it scores chunks and discards low-signal ones)
- Use Obsidian's broken-links panel to keep wikilinks healthy (broken links = missing graph edges)

### UI
Two options, both already available:

**Obsidian Graph View** (built-in, free)
- Open Obsidian → `Ctrl+G` or click the graph icon
- Shows all notes as nodes, wikilinks as edges
- Filter by tag, folder, or connection depth
- Use to verify vault structure before indexing

**Obsidian Dataview plugin** (install from Community Plugins)
- Query notes like a database using DQL (SQL-like syntax)
- Example: list all notes tagged `type/index` with their backlink counts
- Renders results as table, list, or calendar inline in notes
- Useful for spotting gaps in vault coverage before benchmarking

```dataview
TABLE file.inlinks AS "Backlinks", file.tags AS "Tags"
FROM "usense"
SORT file.inlinks DESC
```

---

## Quick Reference

| Method | Update command | UI URL | DB path |
|---|---|---|---|
| A Repomix | `repomix --output ...` | — (file) | `D:\code\meta\*-packed.xml` |
| B code-review-graph | `build_or_update_graph_tool` | — (MCP tools) | MCP internal |
| C ChromaDB | `python index_chroma.py` | `http://localhost:3000` | `D:\code\meta\chroma_db\` |
| D Kuzu | `python build_kuzu.py` | `http://localhost:8000` | `D:\code\meta\kuzu_db\` |
| E Vault-MCP | `vault-mcp reindex` | Obsidian Graph View | `~/.vault-mcp/` |
