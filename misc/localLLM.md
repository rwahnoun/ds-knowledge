---
title: Local LLM setup
aliases:
  - localLLM
  - local llm
  - ollama setup
tags:
  - topic/ml
  - topic/tooling
  - type/pipeline
  - status/draft
date: 2026-05-20
status: draft
type: pipeline
author: rwa
---

# Local LLM setup

End-to-end setup for running a local coding LLM on the RTX 5090 (32 GB VRAM, Blackwell), exposed via an OpenAI-compatible API and consumable from both **OpenCode** and **Claude Code** (as a delegating agent). Target: zero-token coding offload from Claude, GPU shared with other workloads (ComfyUI, etc.).

## Why Ollama (not vLLM)

| Concern | vLLM / TRT-LLM | Ollama |
|---|---|---|
| Windows native | no (WSL2/Docker) | yes |
| Idle VRAM unload | no — locks 90% of VRAM 24/7 | yes — auto-unloads after `OLLAMA_KEEP_ALIVE` |
| Single-user throughput | excellent (overkill solo) | very good |
| NVFP4 / Blackwell-native FP4 | yes | no (GGUF only — Q4–Q8) |
| OpenAI-compatible endpoint | yes | yes (`/v1`) |
| Setup pain | high | trivial |

For a single-user dev box that also runs ComfyUI on the same GPU, **idle unload wins over peak throughput**. The note below uses Ollama; a vLLM appendix is at the bottom for when batched serving is actually needed.

> [!IMPORTANT]
> **NVFP4 in Ollama: not really a thing.** NVFP4 is NVIDIA's Blackwell-native 4-bit float format and currently lives in vLLM and TensorRT-LLM. Ollama uses llama.cpp under the hood with GGUF quants (Q4_K_M, Q6_K, Q8_0, plus MXFP4 for `gpt-oss`). For Qwen3-Coder there is no NVFP4 build — Q6_K is the practical quality/VRAM sweet spot on a 5090. If you ever genuinely need NVFP4 speed, you'd run vLLM in WSL2 and give up idle unload.

---

## 1. Install Ollama

Native Windows installer — no WSL2 needed.

```powershell
winget install Ollama.Ollama
```

Or download the installer from <https://ollama.com/download/windows>. Ollama installs as a background service that auto-starts on login, exposing the API on `http://127.0.0.1:11434`.

Verify:

```powershell
ollama --version
curl http://127.0.0.1:11434/api/version
```

---

## 2. Configure idle unload + performance

Ollama is configured via **user environment variables** (PowerShell — sets persistent user env vars, then restarts the service):

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_MODELS",           "D:\ollamaModels", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_KEEP_ALIVE",       "5m",              "User")
[Environment]::SetEnvironmentVariable("OLLAMA_FLASH_ATTENTION",  "1",               "User")
[Environment]::SetEnvironmentVariable("OLLAMA_KV_CACHE_TYPE",    "q8_0",            "User")
[Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL",     "2",               "User")
[Environment]::SetEnvironmentVariable("OLLAMA_MAX_LOADED_MODELS","1",               "User")

# restart the service so it picks up the new env
Get-Process ollama* -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Process "ollama" -ArgumentList "serve" -WindowStyle Hidden
```

| Variable | Effect |
|---|---|
| `OLLAMA_MODELS=D:\ollamaModels` | Store model blobs on `D:` instead of `C:\Users\rwa\.ollama\models\`. **Set this before the first `ollama pull`** |
| `OLLAMA_KEEP_ALIVE=5m` | Unload model from VRAM after 5 min of idle (5 m is already default — explicit for clarity) |
| `OLLAMA_FLASH_ATTENTION=1` | Enable FlashAttention — large speed + VRAM win on Blackwell |
| `OLLAMA_KV_CACHE_TYPE=q8_0` | Quantize KV cache to 8-bit — roughly halves context VRAM with no measurable quality loss |
| `OLLAMA_NUM_PARALLEL=2` | Allow 2 concurrent requests (OpenCode + Claude agent at the same time) |
| `OLLAMA_MAX_LOADED_MODELS=1` | Don't try to keep two models resident at once |

> [!TIP]
> Watch `nvidia-smi` after a request — VRAM should drop back to ~0 about 5 min after the last call. First request after unload re-loads in ~5–15 s for a 30 B MoE.

---

## 3. Pull the coding model

**Pick: `qwen3-coder:30b-a3b-q4_K_M`** — verified May 2026 as the strongest open coding model that fits **entirely on a single 32 GB 5090** with room for KV cache and a parallel ComfyUI workload. MoE architecture (~3 B active params), tuned for agentic / tool-use coding, native 256 K context. CloudRift's published 5090 benchmark uses this exact variant (AWQ 4-bit) and reaches ~1,157 tok/s aggregate at 16 concurrent requests.

Available official tags on Ollama (May 2026): only `q4_K_M` (19 GB), `q8_0` (32 GB), or `fp16` (61 GB). **No Q6_K shipped** — Q8 saturates the 5090 with no headroom, so Q4_K_M is the only practical choice.

### Why not the newer / bigger models?

| Model (May 2026) | Why not |
|---|---|
| Qwen3-Coder-Next (80B-A3B, Feb 2026) | Smallest Ollama quant is Q4_K_M = **52 GB** — needs CPU offload on a 5090, kills throughput |
| Kimi K2.6 (current SOTA on coding benchmarks) | MoE giant, only fits with aggressive quant + offload — not viable solo on a 5090 |
| Devstral Small 2 (24B dense) | Strong agentic alternative, ~19 GB at Q6, vision support. Dense → 24 B active vs Qwen's 3 B → slower per token. Worth pulling as a secondary model for vision / agent loops |
| DeepSeek V4 Pro | Enterprise scale — out of reach for 32 GB |

| Quant | File size | Notes |
|---|---|---|
| **Q4_K_M** | **19 GB** | **Recommended** — only quant that leaves real KV cache headroom on a 5090 |
| Q8_0 | 32 GB | Saturates the 5090; will OOM with any non-trivial context |
| fp16 | 61 GB | Needs CPU offload — not viable |

```powershell
ollama pull qwen3-coder:30b-a3b-q4_K_M
```

### Tuned Modelfile for coding

Create `D:\code\ds-knowledge\misc\Modelfile.qwen3coder`:

```dockerfile
FROM qwen3-coder:30b-a3b-q4_K_M

# context — 64 K is plenty for coding, ~10 GB KV cache at q8_0
PARAMETER num_ctx 65536

# determinism — coding wants low temp
PARAMETER temperature 0.2
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.05

# leave room for full GPU offload
PARAMETER num_gpu -1
```

Register it:

```powershell
ollama create qwen3-coder-tuned -f D:\code\ds-knowledge\misc\Modelfile.qwen3coder
ollama run qwen3-coder-tuned "write a python function that returns fibonacci(n)"
```

From now on, **use `qwen3-coder-tuned`** as the model name everywhere.

---

## 4. Wire OpenCode to Ollama

OpenCode is already installed at `C:\Users\rwa\.config\opencode\` (`@opencode-ai/plugin` 1.14.25). It supports custom providers via the AI SDK's `@ai-sdk/openai-compatible` package. Write `C:\Users\rwa\.config\opencode\opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      },
      "models": {
        "qwen3-coder-tuned": { "name": "Qwen3-Coder 30B (tuned)" }
      }
    }
  },
  "model": "ollama/qwen3-coder-tuned"
}
```

OpenCode auto-installs `@ai-sdk/openai-compatible` on first launch. The provider key (`ollama`) becomes the prefix in `provider/model` strings.

> [!TIP]
> If tool calls fail, raise `num_ctx` in the Modelfile (Ollama defaults to 8K which is too small for OpenCode's tool prompts). The Modelfile above sets 64K, which is plenty.

Test:

```powershell
opencode run -m "ollama/qwen3-coder-tuned" --dir "d:/code/datascience" "list the top-level modules under ds/"
```

### Update the existing `/qwen` skill

`C:\Users\rwa\.claude\skills\qwen\SKILL.md` still points at `lmstudio/qwen/qwen3-coder-30b` (LM Studio is gone). Change line 17 to:

```bash
opencode run -m "ollama/qwen3-coder-tuned" --dir "<directory>" "<prompt>"
```

---

## 5. Create the `local` agent in Claude Code (user level)

Drop the file below at `C:\Users\rwa\.claude\agents\local.md`. User-level agents are available in every project.

```markdown
---
name: local
description: Delegate a coding task (implementation, refactoring, analysis, code generation, mechanical rewrites) to the local Qwen3-Coder model via Ollama. Use proactively whenever the work is well-defined but token-heavy — file rewrites, repetitive transformations, scaffolding, "do X in every file" tasks. Returns the local model's output; uses zero Claude tokens for the actual work.
tools: Bash, Read, Glob, Grep
---

You are a thin delegation wrapper. Your job is to pass the user's task to the local LLM running on Ollama and return its output. Do NOT perform the coding work yourself.

## How to run

For tasks that need filesystem context (most coding tasks):

```bash
opencode run -m "ollama/qwen3-coder-tuned" --dir "<absolute-dir>" "<prompt>"
```

For stateless one-shot prompts (no repo context):

```bash
curl -s http://127.0.0.1:11434/api/chat -d '{
  "model": "qwen3-coder-tuned",
  "messages": [{"role":"user","content":"<prompt>"}],
  "stream": false,
  "options": {"temperature": 0.2}
}' | jq -r .message.content
```

## Workflow

1. Read the user's task as-is — don't paraphrase.
2. Pick the right working directory:
   - `d:/code/datascience` — core `ds` library
   - `d:/code/ds-scripts` — analysis scripts
   - `d:/code/ds-learn` — ML / training
   - Otherwise use the current project directory.
3. Build a clear, self-contained prompt. Include file paths, the user's intent, and code-style reminders (camelCase methods/vars, CamelCase classes, no underscores; spaces 4 for datascience, tabs for ds-scripts/ds-learn).
4. Run the command with a 180 s timeout.
5. Return the model's output verbatim plus a one-line summary of what was done.
6. On failure, retry once with a tightened prompt, then surface the error.

## Rules

- Never do the coding work yourself — always delegate.
- Keep your own commentary minimal (one line top, one line bottom).
- For large tasks, split into multiple delegated calls rather than one giant prompt.
- If the local model gets it wrong twice, hand control back to the user with the local model's last output attached.
```

Reload Claude Code (`/agents` should now list `local`). Invoke explicitly with `> use the local agent to ...` or let Claude pick it via the description.

---

## 6. Smoke test

```powershell
# 1. model loads
ollama run qwen3-coder-tuned "say hi in one word"

# 2. OpenCode talks to it
opencode run -m "ollama/qwen3-coder-tuned" "what is 2+2"

# 3. Claude delegates — open Claude Code in d:/code/datascience and type:
#    > use the local agent to list every public function in ds/loaders/

# 4. idle unload — wait 6 min, then:
nvidia-smi   # VRAM should be ~0 MB
```

---

## Appendix: when to actually use vLLM

Switch from Ollama to vLLM only if you hit one of these:

- You start serving multiple concurrent users / IDE instances (>3 in parallel) and need real batching.
- You want NVFP4 for measurably higher tokens/sec on Blackwell.
- You're benchmarking model quality and need the exact same engine as cloud deployments.

Setup sketch: WSL2 Ubuntu 24.04 → install CUDA 12.6+ → `uv pip install vllm` → `vllm serve <model> --quantization nvfp4 --gpu-memory-utilization 0.85`. Plan to keep the LLM and ComfyUI on separate GPU power-states or schedule them in different windows.

---

## Sources

| Source | Used for |
|---|---|
| <https://github.com/ollama/ollama/blob/main/docs/faq.md> | Env vars, KV cache quant, keep-alive |
| <https://ollama.com/library/qwen3-coder> | Model tags, default quants |
| <https://ollama.com/library/qwen3-coder-next> | Confirmed newer 80B-A3B is too big for 32 GB |
| <https://www.cloudrift.ai/blog/optimizing-qwen3-coder-rtx5090-pro6000> | RTX 5090 benchmark: 30B-A3B AWQ at ~1,157 tok/s |
| <https://whatllm.org/best-open-source-llm> | May 2026 leaderboard (Kimi K2.6, Qwen 3.6, DeepSeek V4) |
| <https://www.promptquorum.com/local-llms/best-local-llms-for-coding> | Hardware-matched model selection May 2026 |
| <https://docs.vllm.ai/en/latest/features/quantization/nvfp4.html> | NVFP4 support state |
| `C:\Users\rwa\.claude\skills\qwen\SKILL.md` | Existing delegation pattern (LM Studio version) |

## Gaps

- OpenCode 1.14.x config schema isn't fully documented — `providers` block above is best-guess; verify against `opencode config show`.
- Need to actually benchmark Q6_K vs Q8_0 on a representative coding task; current pick is based on VRAM headroom, not measured quality.
- Whether Ollama's MXFP4 path (used by `gpt-oss`) can be applied to a custom Qwen3-Coder build — would close most of the NVFP4 gap if so.
- `/qwen` skill at `C:\Users\rwa\.claude\skills\qwen\SKILL.md` still references LM Studio; update or retire once the `local` agent is proven.
