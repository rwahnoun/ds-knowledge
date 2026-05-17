# Researcher RAG — Code + Science Corpus

> Pattern for a data scientist + scientist who needs retrieval across both a multi-repo Python codebase and a scientific knowledge corpus (papers, lab notes, methods, Obsidian vault). Researched 2026-05-17.

## Verdict up front

**Active frontier with strong duct-tape elements.** No single tool today owns "code + Obsidian + papers + lab notes" end-to-end. The realistic 2026 best-practice is a **Claude Code + MCP + maintained-wiki spine** — not yet-another vector DB.

The single highest-leverage move is the **Karpathy LLM-wiki pattern**: stop chunking, start compiling. Have the agent pre-synthesize raw sources into a maintained markdown wiki, then retrieve from the wiki. Maps directly onto a `ds-knowledge`-style vault with an `index.md` seed.

---

## A. Tools purpose-built for this

1. **[PaperQA2](https://github.com/Future-House/paper-qa)** (FutureHouse / Andrew White). High-accuracy RAG over PDFs + source code with agentic query expansion, re-ranking, and contextual summarization; SOTA on RAG-QA Arena science. Best-in-class for the **papers half** of a researcher stack and explicitly supports source-code files. Heavy LLM-call cost, but quality is the benchmark to beat.
2. **[Khoj](https://github.com/khoj-ai/khoj)** (YC W24, AGPL, 34k+ stars). Self-hostable semantic search + chat across Obsidian, PDFs, markdown, images, Notion, the web; first-class Obsidian plugin; Ollama backend. Closest off-the-shelf fit for "Obsidian vault + cloud/local LLM" — but weaker on code-aware retrieval than a Claude-Code-native flow.
3. **[Reor](https://github.com/reorproject/reor)** — Electron app, fully local (Ollama + Transformers.js + LanceDB), auto-links related markdown notes via vector similarity. Pure PKM — would *replace* Obsidian, so it's a side option rather than a fit unless you abandon the Obsidian editor.
4. **[Open Notebook](https://github.com/lfnovo/open-notebook)** (MIT, Python/FastAPI/SurrealDB). Self-hosted NotebookLM clone, 18+ LLM providers, multimodal, citations with source attribution. Useful as a per-project "research notebook" layer on top of curated source bundles; not a vault-spanning brain.
5. **[research-hub](https://github.com/WenyuChiou/research-hub)** (pip-installable, MCP server). Glues Zotero + Obsidian + NotebookLM with a dashboard and exposes everything via MCP for Claude Code. Very close shape to the canonical researcher setup if you adopt Zotero as the paper store.
6. **[Zotero-MCP](https://github.com/54yyyu/zotero-mcp)** + **[local-rag](https://github.com/Ricardo-Kaminski/local-rag)** (LightRAG + Ollama + MCP over Obsidian + Zotero + Claude Code). Almost exactly the target stack as a reference implementation.

---

## B. Documented strategies people actually use

1. **Router / agentic RAG with one tool per source** — separate indexes for code, papers, lab notes; let an agent decide which to hit and merge. Mainstream 2026 pattern. See [Agentic RAG survey, arXiv 2501.09136](https://arxiv.org/abs/2501.09136).
2. **Zotero-as-source-of-truth + Obsidian-as-synthesis + MCP for access** — Zotero owns PDFs/metadata, Obsidian owns notes/links, Claude/NotebookLM reads both via MCP. Codified in [research-hub](https://github.com/WenyuChiou/research-hub) and [Claude Scholar](https://github.com/Galaxy-Dawn/claude-scholar); see also [spektrl's thesis writeup](https://medium.com/@spektrl/my-thesis-writing-workflow-obsidian-zotero-and-claude-ai-2427737f531f).
3. **GraphRAG over the corpus** — Cognee-style triplet extraction so cross-document entities (biomarkers, instruments, methods) resolve globally instead of per-chunk. See [Cognee GraphRAG](https://www.cognee.ai/blog/deep-dives/cognee-graphrag-supercharging-search-with-knowledge-graphs-and-vector-magic).
4. **Karpathy's LLM-Wiki pattern (the hot 2026 take)** — drop classic RAG for personal use; have the agent *pre-synthesize* raw sources into a maintained markdown wiki (raw/ → wiki/ → CLAUDE.md schema), then retrieve from the wiki. Originally [Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f); Obsidian-flavored fork at [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki). Maps perfectly onto a `ds-knowledge`-style vault with `index.md`.
5. **Tag namespaces + index.md as router hint** — give the vault a curated top-level index file with tags/paths; the agent routes by tag/path before any embeddings get involved. Widely recommended in r/ObsidianMD setups. Already the shape of `ds-knowledge`.

---

## C. Notable individuals who've published their workflow

- **Andrej Karpathy — [llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (Apr 2026).** Takeaway: stop chunking, start compiling — let the agent maintain a structured wiki rather than retrieving raw chunks.
- **Simon Willison — [`llm` + `datasette`](https://github.com/simonw/llm).** Takeaway: SQLite-backed embeddings + CLI plugins are a perfectly viable DIY RAG substrate; he runs his entire 7k-link blog this way.
- **Eugene Yan — [Obsidian Copilot](https://eugeneyan.com/writing/llm-patterns/) and "LLM patterns" essay.** Takeaway: even minimal lookup-style RAG over personal notes pays off; build evals before you build a fancy retriever.

---

## D. Realistic best-practice today

1. **Claude Code with MCP servers as the agent layer.** Code repos already work natively; add an arXiv MCP, a Zotero MCP, and a thin Obsidian MCP (or just let the agent read the vault as files via the existing `index.md`).
2. **Keep code retrieval in-IDE.** Claude Code's grep/glob is already better than embedding-based code RAG for most queries at researcher scale — backed up by the agentic-RAG router pattern.
3. **PaperQA2 (or Open Notebook) for the paper-deep-dive half**, called as a sub-tool when actual literature synthesis is needed.
4. **Adopt the Karpathy LLM-wiki pattern incrementally** on top of the vault. The `index.md` already is the seed; let the agent maintain it. Highest-leverage move and the only one genuinely novel vs. 2024-era RAG.
5. **Skip pure vector-RAG over the vault for now.** For a hundreds-of-notes corpus with good tags and an index, agentic file-reading beats embeddings; revisit if the vault crosses ~10k notes or grows a raw PDF corpus.

Bottom line: the pieces exist, no one has shipped the unified product, and the smart play is a Claude Code + MCP + maintained-wiki spine — not yet-another vector DB.
