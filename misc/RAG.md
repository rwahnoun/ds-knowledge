# subject
hardware: rtx5090 with 32gb vram, high end computer
context:
i want to have a rag system for two use cases: 
- my python code, with several repositories
- my obsidian vault with markdown notes on different subjets.
They can be pretty big.

goals:
- i want the code use case to be so claude can find anything in the code, review it easily, be able to code using my different repos etc.
- i need the obsidian use case to be able to retrieve information accurately in the vault and be able to write new ones.
- one metric on a method is how fast, accurately we can retrieve information
- another is the number of tokens used to get information. the idea is to help claude minimize tokens.

questions:
- what are my best options? skills ? tools? external rag? 

do a deep research and write below the top 10 free options for my use cases. search latest and best information on the web.
What do people advise the most today?
write outputs below the answers section
# answers

> Curated for: RTX 5090 (32 GB VRAM) workstation, Python multi-repo code RAG + Obsidian markdown vault, optimizing for retrieval quality and minimal Claude token usage. MCP-first ranking. Researched 2026-05-16.

## Why MCP matters here

Claude Code's killer integration point is **MCP (Model Context Protocol)**. An MCP-based retrieval layer plugs directly into Claude's tool loop — Claude calls `search_code(query)` and gets back exactly the chunks it needs instead of `Read`-ing whole files. Combined with Claude Code's Tool Search behavior (only loads schemas on demand, cutting context ~95% vs. dumping all tools), MCP RAG is the most token-efficient pattern available. Standalone frameworks (LlamaIndex, RAGFlow) are powerful but require you to glue them to Claude yourself, which usually means more tokens, not fewer.

The community 2026 consensus, repeated across nearly every "best Claude Code MCP" roundup: **install Context7 first, Serena second, and one project-specific RAG server third.** Three to six MCP servers is the sweet spot — beyond that you fight context bloat.

---

## Top 10 Ranked

### 1. Serena — Symbol-level code intelligence via LSP
- **Best for:** Code (multi-repo Python)
- **Type:** MCP server (open-source, MIT)
- **Why recommended:** Universally cited as the #2 must-have MCP for any Claude Code user with non-trivial codebases. ManoMano's published benchmark on a 36 K-line Java repo concluded Serena is "mandatory" for any deep code modification: cross-file renames and reference lookups that would take Claude 8–12 fragile steps collapse into a single semantic call. Uses Language Server Protocol — not embeddings — so there is no indexing job, no stale vectors, and it understands your code the same way PyCharm does.
- **Pros:**
  - LSP-based: find_symbol, find_referencing_symbols, go_to_definition, insert_after_symbol — true semantic operations, not text search
  - 40+ languages including Python, TS, Go, Rust, C++, Java
  - Zero indexing setup, no API keys, completely local
  - Free, MIT licensed
- **Cons:**
  - Adds latency and tokens for *quick* lookups — ManoMano found it 4× more expensive than vanilla Claude for trivial "find this rule" queries
  - Doesn't help with markdown / docs / Obsidian
  - LSP can be flaky for some languages on Windows
- **Hardware fit:** No GPU needed. CPU + LSP only.
- **Token efficiency for Claude:** Excellent for edits/refactors — one `find_referencing_symbols` call replaces dozens of `Read` + `Grep` rounds. Worse for small queries (overhead).
- **Link:** https://github.com/oraios/serena

### 2. Claude Context (Zilliz) — Hybrid semantic + BM25 code search
- **Best for:** Code (very large repos), some doc support
- **Type:** MCP server (open-source, MIT)
- **Why recommended:** The Zilliz/Milvus team built this specifically for Claude Code. Hybrid dense-vector + BM25 keyword search across millions of lines, optimized to return only the relevant snippets — explicitly designed to avoid Claude loading whole directories. Supports a **fully local deployment** with self-hosted Milvus + **Ollama embeddings**, so on your RTX 5090 you can run it 100 % offline.
- **Pros:**
  - Hybrid retrieval (BM25 + dense) — best-of-both for code, where exact identifiers matter as much as semantics
  - Local mode supported: self-hosted Milvus + Ollama (nomic-embed-text, qwen3-embedding, voyage-code-3 if you want cloud)
  - Scales to millions of lines without choking
  - Tree-sitter aware chunking
- **Cons:**
  - Initial Milvus setup is more involved than Serena (Docker compose)
  - Embeddings go stale — needs an incremental re-index pipeline
  - Pure code focus, not ideal for prose
- **Hardware fit:** GPU-accelerated if you embed with Ollama on the 5090. Milvus runs CPU+RAM.
- **Token efficiency for Claude:** Very high — returns ranked snippets with line numbers, not files. Claude reads ~kilobytes instead of megabytes.
- **Link:** https://github.com/zilliztech/claude-context

### 3. Context7 — Up-to-date third-party library docs
- **Best for:** Code (any language, any framework you depend on)
- **Type:** MCP server (open-source, free hosted by Upstash)
- **Why recommended:** Cited in every 2026 roundup as *the single highest-leverage MCP server* — "if you install only one, install this one." It solves a different problem than the others: when Claude writes code against React 19, scikit-learn 1.6, FastAPI 0.115, etc., its training data lags. Context7 fetches current, version-pinned docs at query time and injects them into the prompt. Eliminates hallucinated APIs.
- **Pros:**
  - Zero setup (`npx @upstash/context7-mcp`)
  - Free hosted version, no API key needed for basic use
  - Massive library coverage, kept current
  - Reduces Claude's token waste on wrong-API retries
- **Cons:**
  - Not for *your* code or *your* vault — only public library docs
  - Quality varies by library
- **Hardware fit:** Cloud-hosted, no local resources.
- **Token efficiency for Claude:** Excellent — surgical doc injection vs. Claude flailing with stale API memory.
- **Link:** https://github.com/upstash/context7

### 4. Basic Memory — Markdown knowledge graph that *is* your Obsidian vault
- **Best for:** Obsidian vault (perfect fit)
- **Type:** MCP server (open-source)
- **Why recommended:** Purpose-built for exactly the "Claude + Obsidian markdown vault" use case. Stores everything as plain Markdown with `[[wiki links]]` — meaning Basic Memory *is your Obsidian vault* and Obsidian renders it natively. Hybrid search (semantic + text) over your notes, plus Claude can *write* new notes back into the vault that Obsidian sees immediately. Two-way sync between human edits and AI edits.
- **Pros:**
  - Native Obsidian compatibility — no separate index to maintain
  - Hybrid vector + keyword search ("finds 'error handling' when you wrote 'exception management'")
  - Claude can both read and create notes — directly supports the "help write new notes" goal
  - One-click connect from web app to Claude Code/Desktop/Cursor
  - Local-first, your files never leave your machine
- **Cons:**
  - Younger project than Smart Connections
  - You're trusting it with vault writes; review its conventions
- **Hardware fit:** Runs locally, optional local embeddings.
- **Token efficiency for Claude:** Very high — returns specific note snippets with backlinks, not whole notes.
- **Link:** https://github.com/basicmachines-co/basic-memory

### 5. Probe — AST-aware code search with ripgrep speed
- **Best for:** Code (any size repo)
- **Type:** MCP server / CLI (open-source)
- **Why recommended:** A third path between dumb grep and slow embeddings — ripgrep-fast SIMD scanning combined with tree-sitter AST parsing and BM25/TF-IDF ranking, with a built-in **`--max-tokens` budget** which is exactly what you want for token-efficient Claude integration. Zero setup, no index to maintain (it scans on demand). Run as MCP: `npx @probelabs/probe agent --mcp`.
- **Pros:**
  - No persistent index → never stale, instant on freshly cloned repos
  - Token-budget-aware output natively
  - Tree-sitter for 14+ languages including Python
  - Tiny operational burden vs. Milvus/Qdrant stacks
- **Cons:**
  - Pure lexical+AST — no true semantic ("similar concept") retrieval
  - Less battle-tested than Serena
- **Hardware fit:** CPU only, very lightweight.
- **Token efficiency for Claude:** Best-in-class for "give me at most N tokens of relevant code" queries.
- **Link:** https://github.com/probelabs/probe

### 6. Smart Connections (Obsidian plugin) — Local-first vault embeddings
- **Best for:** Obsidian vault
- **Type:** Obsidian plugin (open-source, freemium)
- **Why recommended:** The incumbent Obsidian RAG plugin, 100k+ users. Zero-setup local embeddings via on-device transformers — no API key, no cloud, fully private. Best inside Obsidian itself (Smart Chat, Smart Connections sidebar). Pair it with Basic Memory or an MCP bridge if you want Claude Code to query the same index.
- **Pros:**
  - True zero-setup local embeddings
  - Works inside Obsidian, immediate UX value even without Claude
  - Active development, large community
- **Cons:**
  - No native MCP server — you'd need a bridge to expose to Claude Code
  - Best for in-Obsidian Q&A, weaker as a Claude Code retrieval backend
- **Hardware fit:** Local, optionally accelerated; CPU is fine for typical vaults.
- **Token efficiency for Claude:** Indirect — strong for the human, requires extra wiring for Claude.
- **Link:** https://github.com/brianpetro/obsidian-smart-connections

### 7. LightRAG — Graph + vector hybrid RAG (cost-effective GraphRAG)
- **Best for:** Vault (especially big, interconnected vaults), can also do code
- **Type:** Python library / standalone (open-source)
- **Why recommended:** Microsoft GraphRAG produces beautiful multi-hop reasoning but indexing 1 GB of docs has been benchmarked at ~$33 K in token costs. LightRAG keeps the entity-relationship graph but unions new docs incrementally (~50% faster updates) and merges neighboring subgraphs for multi-hop without GraphRAG's price tag. Reddit/Medium 2026 practitioner guides repeatedly recommend it as the best Graph-RAG for individuals. Pair with an Ollama model and a local embedding model and it's genuinely free.
- **Pros:**
  - Multi-hop reasoning over your vault — "what did I say about X that connects to Y?"
  - Incremental updates (vs. GraphRAG's full re-build)
  - Works with local Ollama LLM + local embeddings
  - ~20–30 ms faster retrieval than GraphRAG
- **Cons:**
  - Python library, no first-class MCP server (community wrappers exist) — you'd self-host the MCP shim
  - More setup than a one-line npx
  - Graph extraction still costs LLM tokens (use a local model on the 5090)
- **Hardware fit:** Ideal for your rig — runs the extraction LLM on the 5090.
- **Token efficiency for Claude:** Very high once built — returns curated subgraphs, not raw chunks.
- **Link:** https://github.com/HKUDS/LightRAG

### 8. Continue.dev — Local codebase indexer for VS Code (companion to Claude Code)
- **Best for:** Code, as a companion not a replacement
- **Type:** VS Code/JetBrains extension (open-source, Apache-2.0)
- **Why recommended:** Continue indexes your repos into a local vector DB at `~/.continue/index` using transformers.js (so embeddings stay on your machine), and offers `@codebase` retrieval. Several 2026 setups pair Continue (for indexing + autocomplete) with Claude Code (for agentic tasks) — Continue does the heavy retrieval, Claude does the reasoning. Recommended local embedder: `nomic-embed-text` via Ollama.
- **Pros:**
  - Fully local indexing, no API
  - Battle-tested at scale
  - Good defaults for Python repos
  - Free, Apache-2.0
- **Cons:**
  - Lives in the IDE, not as MCP server — slight friction to call from Claude Code (some community MCP wrappers exist)
  - Has had reliability bugs reported on Windows for indexing
- **Hardware fit:** Local embeddings benefit from your GPU.
- **Token efficiency for Claude:** Medium — best when you use Continue's chat directly; indirect via Claude Code.
- **Link:** https://github.com/continuedev/continue

### 9. Cognee — Persistent knowledge-graph memory for agents
- **Best for:** Both (cross-cutting AI memory across code + notes)
- **Type:** MCP server + Python library (open-source)
- **Why recommended:** Cognee builds a unified knowledge graph from any text/code/conversation source and exposes it over MCP. It's how you'd give Claude *persistent memory* across sessions — every interaction is `cognify`'d into the graph, every future query can `search` it. Running in 70+ companies (Bayer, U. of Wyoming). Useful when you want one memory layer behind both code and vault.
- **Pros:**
  - Single backend for code + notes + conversations
  - MCP-native, works with Claude Code / Desktop / Cursor
  - Captures tool-call hooks → builds memory automatically
  - Pluggable graph DB (NetworkX/Neo4j/etc.)
- **Cons:**
  - More opinionated and heavier than a pure code RAG
  - Quality depends on the cognify LLM (run locally for free)
  - Newer; expect rough edges
- **Hardware fit:** Local extraction LLM ideal on 5090.
- **Token efficiency for Claude:** High — graph queries return curated subgraphs.
- **Link:** https://github.com/topoteretes/cognee

### 10. RAGFlow — Heavy-duty document RAG with deep parsing
- **Best for:** Vault (only if your notes include PDFs, scans, tables)
- **Type:** Self-hosted server + UI (open-source, Apache-2.0)
- **Why recommended:** If your Obsidian vault contains attached PDFs, papers, screenshots of figures, etc., RAGFlow has the best "deep document understanding" pipeline of any open-source tool — intelligent layout-aware chunking, table extraction, built-in knowledge graph. Overkill for plain markdown, but the right tool if your vault is heterogenous (markdown + research PDFs + scanned notes).
- **Pros:**
  - Best-in-class document parsing (tables, multi-column, scans)
  - Built-in graph construction
  - Visual UI for tuning chunkers
  - Free, Apache-2.0
- **Cons:**
  - Heavy Docker stack to operate
  - No native MCP server (you'd query via its HTTP API from a wrapper)
  - Overkill for pure markdown
- **Hardware fit:** GPU helps for parsing models; CPU+RAM heavy.
- **Token efficiency for Claude:** Medium-high once wired in.
- **Link:** https://github.com/infiniflow/ragflow

---

## Honorable mentions (didn't make top 10)

- **mcp-local-rag** — zero-setup local-first RAG MCP server (semantic + keyword, npx one-liner). Good lightweight default if you don't want Milvus. https://github.com/shinpr/mcp-local-rag
- **AnythingLLM** — desktop RAG app with Ollama integration; great for browsing your vault as a human, not ideal as a Claude backend.
- **Open WebUI** — similar story, now has native MCP support; consider for the chat-with-your-vault human side.
- **Microsoft GraphRAG / nano-graphrag** — quality is great, cost is brutal unless you run extraction locally; LightRAG eats their lunch in 2026.
- **Aider** — its own agent with embedded repo-map; competes with Claude Code rather than augmenting it.
- **LlamaIndex / LangChain** — frameworks, not products. Use as glue if you build something custom.
- **Sourcegraph Cody / Zoekt** — Zoekt alone is a fantastic free trigram code search engine you could expose via a tiny MCP shim if you want grep-on-steroids over many repos.

---

## Vector store / embedding picks (if you roll your own)

- **Vector DB:** Qdrant (local Docker, fast, hybrid search) or LanceDB (embedded, zero-ops, perfect for personal use). pgvectorscale wins on raw QPS but is overkill for a single user.
- **Code embeddings (local on 5090):** `voyage-code-3` if you accept a paid API; otherwise `Qwen3-Embedding-4B` or `nomic-embed-text-v2-moe` via Ollama — both fit comfortably in 32 GB VRAM and score near the top of MTEB for code.
- **Text embeddings (vault):** `Qwen3-Embedding-4B` is the all-rounder right now; `Jina Embeddings v4` if you have images in notes.

---

## Overall recommendation for your two use cases

Given the RTX 5090, 32 GB VRAM and the Claude Code integration angle, here's the stack to actually deploy:

**Tier 1 — install today, all free, all MCP, ~30 minutes setup:**
1. **Context7** — always-on, kills hallucinated library APIs across every Python project.
2. **Serena** — symbol-level navigation across all repos. Disable it for trivial sessions where only quick reads are needed (its overhead isn't worth it), enable for refactors and review.
3. **Basic Memory** — point it at the Obsidian vault. Claude Code can now read, search, and write notes that Obsidian sees natively. Cleanest match for the "retrieve + help write new notes" goal.

**Tier 2 — add when you outgrow Tier 1 (a week or two later):**

4. **Claude Context** with self-hosted Milvus + Ollama `Qwen3-Embedding-4B` for **dense semantic search over the multi-repo codebase**. This is where the 5090 finally earns its keep — local embeddings, no API costs, hybrid retrieval beats Serena alone for "find code about concept X across all repos."
5. **Probe** as a no-index fallback for sessions on repos that aren't indexed yet — keeps Claude productive on a freshly cloned repo before Milvus catches up.

**Tier 3 — experiment if you love your vault:**

6. **LightRAG** layered on top of the vault for multi-hop reasoning ("what notes connect biomarker X to ML approach Y?"). Run extraction with a local Qwen3 model on the 5090. This is where the GPU really shines.

**What to skip:** Full Microsoft GraphRAG (too expensive), RAGFlow (overkill unless lots of PDFs), AnythingLLM/Open WebUI (great human UIs but redundant when Claude Code is the driver), LangChain/LlamaIndex (only if building custom).

**Token-efficiency principle to internalize:** Every tool in Tier 1 returns *snippets with locations*, not files. That's the whole game for minimizing Claude's context. The moment a tool wants Claude to read entire files to "see context," you've lost — switch to a tool that does the chunking + ranking on its side.

---

## Sources

- [Best Claude Code MCP Servers in 2026 (Nimbalyst)](https://nimbalyst.com/blog/best-claude-code-mcp-servers/)
- [Best MCP Servers for Claude Code 2026 (Toolradar)](https://toolradar.com/blog/best-mcp-servers-claude-code)
- [Best MCP Servers 2026 (Totalum)](https://www.totalum.app/blog/best-mcp-servers-2026)
- [15 Best Open-Source RAG Frameworks 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-open-source-rag-frameworks)
- [Vector Database Benchmarks 2026 (CallSphere)](https://callsphere.ai/blog/vector-database-benchmarks-2026-pgvector-qdrant-weaviate-milvus-lancedb)
- [Best Vector Databases 2026 (MarkTechPost)](https://www.marktechpost.com/2026/05/10/best-vector-databases-in-2026-pricing-scale-limits-and-architecture-tradeoffs-across-nine-leading-systems/)
- [Embedding Models Benchmark 2026 (Milvus blog)](https://milvus.io/blog/choose-embedding-model-rag-2026.md)
- [Best Open-Source Embedding Models 2026 (BentoML)](https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models)
- [Claude Context GitHub (Zilliz)](https://github.com/zilliztech/claude-context)
- [Serena GitHub (oraios)](https://github.com/oraios/serena)
- [Context7 GitHub (Upstash)](https://github.com/upstash/context7)
- [Basic Memory GitHub](https://github.com/basicmachines-co/basic-memory)
- [Probe GitHub (probelabs)](https://github.com/probelabs/probe)
- [Cognee GitHub](https://github.com/topoteretes/cognee)
- [LightRAG GitHub (HKUDS)](https://github.com/HKUDS/LightRAG)
- [RAGFlow GitHub (infiniflow)](https://github.com/infiniflow/ragflow)
- [Continue Codebase Retrieval docs](https://docs.continue.dev/walkthroughs/codebase-embeddings)
- [Why Cline Doesn't Index (Cline blog)](https://cline.bot/blog/why-cline-doesnt-index-your-codebase-and-why-thats-a-good-thing)
- [Benchmarking Claude Code vs Serena on 36k LOC Java (ManoMano)](https://medium.com/manomano-tech/project-aegis-benchmarking-ai-agents-and-why-serena-is-our-new-must-have-311673db35dd)
- [Context7 vs Serena MCP comparison (bbang)](https://medium.com/@bbangjoa/context7-vs-serena-mcp-strengths-weaknesses-and-which-one-id-recommend-f3142424435d)
- [GraphRAG vs LightRAG (Maarga)](https://www.maargasystems.com/2025/05/12/understanding-graphrag-vs-lightrag-a-comparative-analysis-for-enhanced-knowledge-retrieval/)
- [Graph RAG in 2026 — Practitioner's Guide (Medium)](https://medium.com/graph-praxis/graph-rag-in-2026-a-practitioners-guide-to-what-actually-works-dca4962e7517)
- [cAST: AST-Based Chunking (arXiv)](https://arxiv.org/html/2506.15655v1)
- [Building RAG on Codebases (LanceDB)](https://www.lancedb.com/blog/building-rag-on-codebases-part-1)
- [RAG for 10k Code Repos (Qodo)](https://www.qodo.ai/blog/rag-for-large-scale-code-repos/)
- [AI Coding Assistants for Large Codebases (Kilo)](https://blog.kilo.ai/p/ai-coding-assistants-for-large-codebases)
- [Smart Connections Obsidian plugin](https://community.obsidian.md/plugins/smart-connections)
- [Local AI + Obsidian Second Brain (Local AI Master)](https://localaimaster.com/blog/local-ai-obsidian-integration)
- [Best Local LLMs for Private RAG 2026 (LMSA)](https://blog.lmsa.app/the-best-local-llms-for-private-rag-in-2026-a-complete-guide)
- [Obsidian + Claude Code Integration Guide (Starmorph)](https://blog.starmorph.com/blog/obsidian-claude-code-integration-guide)
- [Open WebUI vs AnythingLLM (wz-it)](https://wz-it.com/en/blog/open-webui-vs-anythingllm-comparison/)