# Claude Code — ds-knowledge Knowledge Base

## Vault Contents
**Read [`index.md`](index.md) first** to find what's in this vault. It's the curated navigation hub — every section, subdirectory, and note has a one-line description and wikilink. Use it to locate relevant notes before starting a task instead of grepping blindly. Regenerate it via [`updateIndex.md`](updateIndex.md) when the vault structure changes.

## Markdown File Template
**Always follow `meta/tplMarkdown.md`** when writing or editing generic markdown files in this vault.
**Always follow `meta/tplModule.md`** when writing or editing markdown files for a code module.

Key requirements:
- YAML frontmatter with `title`, `aliases`, `tags`, `date`, `status`, `type`, `author`
- Tag namespaces: `topic/`, `type/`, `status/`, `device/`
- `##` for top-level sections, `###` for subsections
- 2–3 line context block after H1
- End every file with `## Sources` table and `## Gaps` section
- Wikilinks: `[[note-name]]` or `[[note-name|display text]]`
- Callout boxes: `> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`
