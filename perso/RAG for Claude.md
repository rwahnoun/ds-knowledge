# RAG for Claude — Code + Obsidian Vault (Local Setup Review)  
  
**Date:** 2026-04-20  
**Hardware:** 32GB VRAM GPU, high-perf PC — local-first is the right default  
**Goal:** Minimize token usage while keeping retrieval quality high  
  
---  
  
## TL;DR / Recommendations  
  
| Use case | Recommended stack | Why |  
|---|---|---|  
| **Code RAG** | `knowledge-rag` or `mcp-local-rag` (MCP) + Qwen3-Embedding-4B + BM25 + cross-encoder rerank | MCP means Claude calls a tool, so only the top-k chunks enter context — huge token savings vs. dumping files. Qwen3 leads MTEB-Code. |  
| **Obsidian RAG** | `obsidian-intelligence` or `engraph` (MCP) + Ollama `nomic-embed-text` or `qwen3-embedding` | Native markdown chunking, wikilink graph traversal, file-watcher auto-reindex, 100% local. |  
| **Shared principle** | Contextual Retrieval (Anthropic) + hybrid (vector + BM25) + reranker | Reduces retrieval failures by up to 67% (Anthropic benchmark). |  
  
**Token-minimizing key insight:** The whole point of a good RAG is that Claude asks the tool for 3–5 relevant chunks instead of loading a whole repo or vault. Reports of ~98% token reduction per query vs. dumping the vault are realistic.  
  
---  
  
## 1. Core Principles (apply to both use cases)  
  
### 1.1 Use MCP, not context dumps  
Model Context Protocol (MCP) lets Claude Desktop / Claude Code call your local RAG server as a tool. Claude decides when to search, receives only the top-k chunks, and you never have to paste content manually. Every RAG solution below uses MCP.  
  
### 1.2 Hybrid search beats vector-only  
Pure semantic search misses exact matches (function names, error codes, IDs, acronyms). Combine:  
- **Dense** (embeddings, semantic)  
- **Sparse** (BM25, keyword — essential for code identifiers like `useEffect`, gene symbols, variable names)  
- **Reranker** (cross-encoder like `ms-marco-MiniLM-L-6-v2` or BGE reranker) over the merged candidate set  
  
### 1.3 Contextual Retrieval (Anthropic, Sep 2024)  
Before embedding each chunk, prepend a short LLM-generated context summarizing where the chunk sits in the parent document. Benchmarks: 35% fewer failures with contextual embeddings alone, 49% with BM25, **67% with reranking**. With prompt caching, indexing a 1000-doc corpus drops from ~$94 to ~$12.  
- Blog: [https://www.anthropic.com/news/contextual-retrieval](https://www.anthropic.com/news/contextual-retrieval)  
- Cookbook: [https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)  
  
### 1.4 Under 200K tokens? Skip RAG  
Anthropic's own recommendation: if the knowledge base fits in one context window, just load it all with prompt caching. RAG is for the cases where you can't.  
  
---  
  
## 2. Embedding Models (local, 32GB VRAM)  
  
Based on the 2026 benchmark rounds (Milvus, Zhang, BentoML, PreMAI):  
  
| Model | Size | Context | Best for | License |  
|---|---|---|---|---|  
| **Qwen3-Embedding-8B** | 8B | 32K | **#1 MTEB multilingual + MTEB-Code** — best overall open for you | Apache 2.0 |  
| **Qwen3-Embedding-4B** | 4B | 32K | Great quality/speed balance on your GPU | Apache 2.0 |  
| **Qwen3-Embedding-0.6B** | 0.6B | 32K | Fast indexing, still strong | Apache 2.0 |  
| **Jina Embeddings v4** | 3B | 32K | MRL compression, multimodal | Open weights |  
| **BGE-M3** | 568M | 8K | Dense + sparse + multi-vector in one model | MIT |  
| **nomic-embed-text** | 137M | 8K | Lightweight default, runs via Ollama out-of-the-box | Apache 2.0 |  
| **jina-embeddings-v2-base-code** | — | 8K | Code-specific alternative | Open |  
  
**My pick for your box:**  
- **Code RAG:** `Qwen3-Embedding-4B` (leads MTEB-Code, understands programming syntax + NL queries; 4B fits comfortably on 32GB with headroom for reranker)  
- **Obsidian RAG:** `Qwen3-Embedding-4B` or `nomic-embed-text` if you want minimal footprint / fast iteration  
  
Use **Ollama** (`ollama pull qwen3-embedding` / `ollama pull nomic-embed-text`) — simplest local serving path and integrates with every tool below.  
  
---  
  
## 3. Use Case 1 — RAG over your Code  
  
### Option A: `knowledge-rag` by lyonzin ![⭐](https://fonts.gstatic.com/s/e/notoemoji/17.0/2b50/32.png) (recommended starting point)  
- Pure pip install, MCP-native, ONNX with optional CUDA for 5-10x indexing speedup  
- Hybrid search + cross-encoder reranking + markdown-aware chunking  
- 12 file formats, 12 MCP tools, presets including `developer.yaml`  
- Repo: [https://github.com/lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag)  
- Install: `pip install knowledge-rag[gpu]` → `claude mcp add knowledge-rag`  
  
### Option B: `mcp-local-rag` by shinpr  
- Semantic + keyword boost specifically designed for code (makes `useEffect`, class names rank higher than just semantically similar concepts)  
- Smart semantic chunking at topic boundaries, quality-first result filtering  
- Zero setup: `npx -y mcp-local-rag`  
- Can swap to `jinaai/jina-embeddings-v2-base-code` for code-only corpora  
- Repo: [https://github.com/shinpr/mcp-local-rag](https://github.com/shinpr/mcp-local-rag)  
  
### Option C: `rag-cli` by ItMeDiaTech  
- ChromaDB + sentence-transformers + cross-encoder reranking  
- Multi-Agent Framework orchestration, explicit "no token use" bridge design  
- More moving parts but very configurable  
- Repo: [https://github.com/ItMeDiaTech/rag-cli](https://github.com/ItMeDiaTech/rag-cli)  
  
### Option D: DIY from `awesome-llm-apps` + Ollama + ChromaDB  
- Full control: function-aware chunking that respects code boundaries (AST-level splits), content-addressed IDs, file-path metadata  
- Middleware injects retrieved context into `CLAUDE.md` before each task  
- Walkthrough: [https://www.sitepoint.com/local-rag-for-agents-integrating-private-knowledge-bases-with-awesomellmapps/](https://www.sitepoint.com/local-rag-for-agents-integrating-private-knowledge-bases-with-awesomellmapps/)  
  
### For ML/signal-processing/DL code specifically  
Add these to the index:  
- Your repos + inline docstrings  
- Papers you reference (PDFs) — use PyMuPDF for extraction  
- Library source code you pin to (e.g., specific PyTorch / scipy.signal / MNE / nilearn versions)  
- Jupyter notebooks — strip outputs, chunk by cell markdown headings  
  
Chunking strategy for Python: split by function/class (use `tree-sitter` or `ast`), keep docstrings attached to their function body in the same chunk, prepend file path + module docstring as "context."  
  
---  
  
## 4. Use Case 2 — RAG over your Obsidian Vaults  
  
### Option A: `obsidian-intelligence` by GuideThomas ![⭐](https://fonts.gstatic.com/s/e/notoemoji/17.0/2b50/32.png) (recommended)  
- Purpose-built for Obsidian: SQLite index storing FTS, embeddings, graph metadata  
- Fully air-gapped with Ollama, no telemetry, no phone-home  
- Built originally for a 6,000-note vault (similar scale to what you likely have)  
- Works with Claude Desktop, Claude Code, Cursor, Cline, Continue.dev  
- Glama listing: [https://glama.ai/mcp/servers/GuideThomas/obsidian-intelligence](https://glama.ai/mcp/servers/GuideThomas/obsidian-intelligence)  
- Install: `npm install -g obsidian-intelligence` → `vault-intelligence index --vault /path`  
  
### Option B: `engraph` by devwhodevs  
- Local knowledge **graph** — respects your wikilinks, tags, backlinks  
- 5-lane hybrid: semantic + BM25 + graph expansion + cross-encoder rerank + temporal scoring, fused via Reciprocal Rank Fusion  
- LLM-powered orchestrator that adapts lane weights per query intent  
- Temporal queries like "what did I write last week" work out of the box  
- 25 MCP tools, 26 REST endpoints, llama.cpp with CUDA  
- Repo: [https://github.com/devwhodevs/engraph](https://github.com/devwhodevs/engraph)  
  
### Option C: `obsidian-agentic-rag` by mthehang  
- Docker-based, 7 specialized MCP tools, hybrid search with reranking  
- File watcher auto-reindexes on changes  
- Qwen3 embeddings (4096d), ChromaDB, FastAPI  
- Implements Anthropic's Contextual Retrieval (prepends LLM-generated context per chunk)  
- Repo referenced via: [https://lobehub.com/mcp/mthehang-obsidian-agentic-rag](https://lobehub.com/mcp/mthehang-obsidian-agentic-rag)  
  
### Option D: `obsidian-notes-rag` by ernestkoe  
- Minimal, Python + uv, Ollama or OpenAI, ChromaDB  
- Good for a clean reference implementation you can fork  
- Repo: [https://github.com/ernestkoe/obsidian-notes-rag](https://github.com/ernestkoe/obsidian-notes-rag)  
  
### Option E: `nooscope` by dyerlab  
- Thoughtful write-up on the architecture — worth reading even if you pick another tool  
- Key distinction: read AND write path (can save new notes back to vault during conversation)  
- Blog: [https://www.rodneydyer.com/your-vault-your-vectors-building-a-local-first-mcp-server-for-obsidian/](https://www.rodneydyer.com/your-vault-your-vectors-building-a-local-first-mcp-server-for-obsidian/)  
  
### Obsidian-specific chunking tips  
- Chunk by heading (H1/H2/H3), not character count — preserves semantic boundaries  
- Keep frontmatter as metadata (tags, date, aliases), not in the embedded text  
- Index wikilinks as graph edges — major boost for notes that reference each other (biomedical workflow: `[[Parkinson-signal-processing]]` linking to `[[EMG-filtering]]` etc.)  
- Exclude `.trash/`, `templates/`, attachments by default  
  
---  
  
## 5. Token-Minimization Checklist  
  
1. **MCP tool interface** — Claude pulls only top-k chunks (not full docs)  
2. **Aggressive top-k** — start with k=20 retrieved, rerank to top 3–5 for Claude  
3. **Chunk size 400–800 tokens** — small enough to be relevant, large enough to carry context  
4. **Contextual Retrieval** — one-time indexing cost, permanent token savings per query  
5. **Cross-encoder rerank** — lets you retrieve broadly then hand Claude fewer, better chunks  
6. **Group-by-relevance-gaps** (a la `mcp-local-rag`) — trims the tail instead of arbitrary top-k cutoff  
7. **Prompt caching** — if you must include any static context (CLAUDE.md, system prompt), cache it  
8. **Section-level tools** — give Claude `read_chunk_neighbors` / `read_section` so it expands context on demand rather than receiving everything upfront  
  
---  
  
## 6. Concrete Starting Plan  
  
**Week 1 — Code RAG:**  
1. Install Ollama, pull `qwen3-embedding` and `qwen3-reranker`  
2. `pip install knowledge-rag[gpu]`  
3. Point it at your main repos, index  
4. Add as MCP server to Claude Code  
5. Test retrieval with 10 realistic queries from your workflow  
  
**Week 2 — Obsidian RAG:**  
6. `npm install -g obsidian-intelligence`  
7. Index your vault, use Ollama as embedding backend  
8. Add as MCP server to Claude Desktop  
9. Validate on a few notes you know well  
  
**Week 3 — Upgrade:**  
10. Layer in Contextual Retrieval (use a local Qwen or Claude Haiku for chunk context generation with prompt caching)  
11. Add cross-encoder reranking if not already on  
12. Measure retrieval failure rate on a hand-built eval set of ~30 queries — Anthropic's Pass@k metric is a simple place to start  
  
---  
  
## Key References  
  
- Anthropic Contextual Retrieval: [https://www.anthropic.com/news/contextual-retrieval](https://www.anthropic.com/news/contextual-retrieval)  
- Anthropic RAG Cookbook: [https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)  
- Claude Projects RAG (managed): [https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)  
- 2026 Embedding Benchmark (Milvus): [https://milvus.io/blog/choose-embedding-model-rag-2026.md](https://milvus.io/blog/choose-embedding-model-rag-2026.md)  
- 2026 Embedding Benchmark (Zhang, DEV): [https://dev.to/chen_zhang_bac430bc7f6b95/which-embedding-model-should-you-actually-use-in-2026-i-benchmarked-10-models-to-find-out-58bc](https://dev.to/chen_zhang_bac430bc7f6b95/which-embedding-model-should-you-actually-use-in-2026-i-benchmarked-10-models-to-find-out-58bc)  
- MTEB Leaderboard: [https://huggingface.co/spaces/mteb/leaderboard](https://huggingface.co/spaces/mteb/leaderboard)  
- knowledge-rag: [https://github.com/lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag)  
- mcp-local-rag: [https://github.com/shinpr/mcp-local-rag](https://github.com/shinpr/mcp-local-rag)  
- obsidian-intelligence: [https://glama.ai/mcp/servers/GuideThomas/obsidian-intelligence](https://glama.ai/mcp/servers/GuideThomas/obsidian-intelligence)  
- engraph: [https://github.com/devwhodevs/engraph](https://github.com/devwhodevs/engraph)  
- Agentic RAG w/ Claude Code (Medium): [https://medium.com/@souma.paul/building-an-agentic-rag-with-claude-code-65358a96ab09](https://medium.com/@souma.paul/building-an-agentic-rag-with-claude-code-65358a96ab09)