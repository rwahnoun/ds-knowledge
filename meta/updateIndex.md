This task updates a global index of the vaults to optimize claude knowledge access. the index is stored at the root of the vault. 
It's the curated navigation hub — every section, subdirectory, and note has a one-line description and wikilink.


  Create or update `index.md` at the vault root (D:\obsidian\index.md).

  This file is the primary navigation hub Claude uses to locate notes. Every directory and note gets a one-line description and a
  wikilink. Keep descriptions terse and content-focused — written for fast lookup, not for humans skimming.

  ## Structure

  Use H2 for top-level sections, H3 for subdirectories, then a flat list of notes:

  ## SECTION — one-line description of what this section covers

  ### Subsection — one-line description
  - [[Note Title]] — what this note covers

  ## Process
  1. Walk the full vault tree using directory listing tools.
  2. For each note, read the first heading or file to inform the description — don't rely on filename alone.
  3. Write the complete index to `index.md`, overwriting any previous version.
  ## Exclusions
  Skip entirely:
  - Directories: `templates`, `media`, `.obsidian`, `.claude`, `.ipynb_checkpoints`, `meta`, 
  - Any file named `Misc.md` (anywhere in the tree)
  - The index file itself
  - Files with no substantive content (empty, checkpoint copies under `.ipynb_checkpoints`)
