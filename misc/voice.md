# Voice Cloning — Local & Fast (2026 Field Guide)

> Researched 2026-05-17. Target hardware: RTX 5090 / 32 GB VRAM, Windows. All picks run fully local, no cloud calls, no API keys. **Filtered to real-time / low-latency models only** — Claude generates the sentence text, the `/speak` skill TTSes it live at runtime. Models that take more than ~real-time to generate (F5-TTS, IndexTTS-2, StyleTTS 2 fine-tunes, Tortoise, MARS) are out of scope.

## Table of contents

1. [TL;DR — three picks for three goals](#1-tldr--three-picks-for-three-goals)
2. [Top models ranked](#2-top-models-ranked)
3. [Top 5 comparison matrix](#3-top-5-comparison-matrix)
4. [Generation time for a real phrase](#4-generation-time-for-a-real-phrase)
5. [Frontends / UIs worth using](#5-frontends--uis-worth-using)
6. [Fine-tuning notes & dataset prep](#6-fine-tuning-notes--dataset-prep)
7. [Cloning real people — audio sources](#7-cloning-real-people--audio-sources)
   - 7.1 [Richard Feynman](#71-richard-feynman)
   - 7.2 [John Malkovich](#72-john-malkovich)
8. [Giving Claude a voice — practical wiring](#8-giving-claude-a-voice--practical-wiring)
9. [Ethics & legal](#9-ethics--legal)
10. [References](#10-references)

---

## 1. TL;DR — three picks for three goals

| Goal | Pick | Why |
|---|---|---|
| **"Clone my own voice today, minimal fuss, live generation"** | **Chatterbox Turbo** by Resemble AI | MIT license, 5-second zero-shot clone, sub-200 ms first-audio on a 5090, beats ElevenLabs in blind tests. Runs as a persistent HTTP server (`devnen/Chatterbox-TTS-Server`) that the `/speak` skill calls directly. |
| **"Best Feynman/Malkovich from real recordings, real-time"** | **GPT-SoVITS v4**, fine-tuned | v4 vocoder outputs native 48 kHz. Fine-tune in <2 h on a 5090, sub-second inference for short phrases. The only fine-tunable cloner that's also fast enough for live `/speak` calls. |
| **"Zero GPU footprint at runtime"** | **Piper** (fine-tuned, or libritts base) | <100 ms per sentence on CPU. Lower quality than GPT-SoVITS for distinctive voices but fast enough that you stop noticing. Best fallback when the GPU is busy with ComfyUI / training. |

**Why F5-TTS is no longer the pick:** it takes 2-4 s to generate a 3-second phrase on a 5090. Quality is excellent but latency makes it unusable for live `/speak` calls where Claude already paused for ~5 s composing the sentence.

---

## 2. Top models ranked

Ranking weights: real-time inference, clone quality, ecosystem maturity, license cleanliness, Windows-friendliness on a 5090. All shipped models below generate faster than real-time for short phrases.

### 2.1 Chatterbox / Chatterbox Multilingual / Chatterbox Turbo — *the new default*
- **Tagline:** State-of-the-art open zero-shot TTS, with emotion exaggeration knob.
- **Type:** Zero-shot (5 s reference). Optional fine-tune.
- **License:** MIT (model + code).
- **Quality:** Excellent — repeatedly preferred over ElevenLabs in independent A/B tests.
- **Speed:** Sub-200 ms first-audio on Turbo. Total generation ~400-800 ms for a typical short phrase.
- **Setup:** Easy. `pip install chatterbox-tts`, or use the Chatterbox-TTS-Server (CUDA/ROCm/CPU, OpenAI-compatible API, voice cloning, audiobook chunking).
- **Windows:** Confirmed working; the devnen server has explicit Windows path support.
- **Pros:** MIT license, paralinguistic tags ("[laughs]", "[sighs]"), built-in PerTh watermarking, 23+ languages in Multilingual variant, mature community, persistent-server pattern is exactly what `/speak` needs.
- **Cons:** Watermarking baked in (fine for personal use); base model is English-first.
- **Repo:** https://github.com/resemble-ai/chatterbox · server: https://github.com/devnen/Chatterbox-TTS-Server

### 2.2 GPT-SoVITS v4 — *the cloner you can fine-tune AND run live*
- **Tagline:** "1 minute of voice data" voice cloning with a polished training WebUI; sub-second inference after fine-tune.
- **Type:** Few-shot zero-shot (5 s) + fine-tune from 1-60 min of data.
- **License:** MIT.
- **Quality:** Very high after fine-tuning. v4 outputs native 48 kHz, fixed v3's metallic artifacts. Tone leans toward the *reference audio* rather than averaged training set — good for impersonation.
- **Speed:** Sub-second on 5090 for short phrases (0.5-1.5 s for ~3-4 s of audio).
- **Setup:** Medium. Official one-click Windows installer; download `s2v4.pth` + `vocoder.pth` into `GPT_SoVITS/pretrained_models`.
- **Windows:** First-class. Most tutorials are Windows-first.
- **Pros:** Best-in-class for *trainable* voice cloning with tiny data, integrated dataset prep + ASR + segmentation tools, very active community, fast enough for live use.
- **Cons:** v3/v4 picky about training data quality — feed it noisy audio and it degrades (use v1/v2 if rough). Prosody capture is good-but-not-F5-tier — distinctive cadences (Malkovich) lose a bit. Mostly Chinese + English + Japanese.
- **Repo:** https://github.com/RVC-Boss/GPT-SoVITS

### 2.3 XTTS-v2 (Coqui, idiap fork) — *the streaming workhorse*
- **Tagline:** The default multilingual cloner since 2023; community-maintained after Coqui's 2024 shutdown.
- **Type:** Zero-shot (6 s) + fine-tune.
- **License:** Coqui Public Model License (CPML) — non-commercial, personal use OK. Code (idiap fork) MPL 2.0.
- **Quality:** Good. Beaten on raw fidelity by Chatterbox but unmatched in *multilingual* coverage and *ecosystem*.
- **Speed:** 200 ms time-to-first-chunk with streaming, ~1-2 s total for a short phrase.
- **Setup:** Easy via `pip install coqui-tts` (maintained fork) or via AllTalk v2 (which exposes a JSON API perfect for `/speak`).
- **Windows:** First-class — most XTTS tutorials are Windows.
- **Pros:** 17 languages, streaming, mature, deeply integrated with AllTalk and SillyTavern, huge fine-tuning community, AllTalk's API is drop-in for `/speak`.
- **Cons:** Original org dead; weights are CPML so technically non-commercial; quality now mid-pack.
- **Repo:** https://github.com/idiap/coqui-ai-TTS · PyPI: `coqui-tts`

### 2.4 Piper — *the CPU baseline, fine-tunable*
- **Tagline:** VITS-based TTS optimized for <100 ms CPU inference. Currently powers your `/speak` skill with `libritts_r-medium`.
- **Type:** Fine-tune from base checkpoint; not really a zero-shot cloner.
- **License:** GPL (active fork `OHF-Voice/piper1-gpl`); MIT (archived `rhasspy/piper`).
- **Quality:** ~3.6-3.8 MOS. Captures timbre, loses prosody/idiosyncrasy. Fine for short generic phrases; weak on distinctive voices like Malkovich on long sentences.
- **Speed:** **80-150 ms on CPU** for a 3-4 s phrase. 25-50× realtime. Zero GPU footprint at inference.
- **Setup:** Easy for inference (already installed). Training needs WSL2 on Windows for sm_120 (see Section 6.3).
- **Windows:** First-class for inference; WSL2 for training.
- **Pros:** Fastest option, zero GPU usage at runtime, integrates with existing `/speak` already, can fine-tune on Feynman/Malkovich data.
- **Cons:** Fine-tune quality won't match GPT-SoVITS/Chatterbox for distinctive voices; needs WSL2 for training on a 5090; 22050 Hz output (no 48 kHz).
- **Repo:** https://github.com/OHF-Voice/piper1-gpl

### 2.5 CosyVoice 2 (FunAudioLLM / Alibaba)
- **Tagline:** Ultra-low-latency multilingual TTS with streaming.
- **Type:** Zero-shot.
- **License:** Apache 2.0 — clean for any use.
- **Quality:** Very good (MOS 5.53), 9 languages + 18 Chinese dialects.
- **Speed:** **150 ms streaming latency** — second only to Piper.
- **Setup:** Medium. Heavier deps; Linux preferred but Windows works via WSL or pure pip with patience.
- **Pros:** Apache 2.0, fine emotion/dialect control, real-time, lowest streaming latency of any GPU model here.
- **Cons:** Chinese-first repo, uneven English instructions; Windows native is fiddly. Zero-shot only — can't fine-tune cleanly for a target voice.
- **Repo:** https://github.com/FunAudioLLM/CosyVoice

### 2.6 Sesame CSM-1B — *built for assistants*
- **Tagline:** *Conversational* speech model — built for back-and-forth dialogue.
- **Type:** Zero-shot voice cloning with conversational context.
- **License:** Apache 2.0.
- **Quality:** Particularly natural in dialogue / interactive use; emotionally intelligent.
- **Speed:** Real-time on consumer GPUs.
- **Pros:** Apache 2.0, Llama-based architecture (easy to reason about), built for assistants specifically — exactly your use case.
- **Cons:** Smaller community vs Chatterbox; tooling less mature; no fine-tune workflow yet.
- **Repo:** https://github.com/SesameAILabs/csm · clone fork: https://github.com/isaiahbjork/csm-voice-cloning

### 2.7 Kokoro-82M — *the speed demon*
- **Tagline:** 82M-param model optimized for blazing-fast inference on CPU or modest GPU.
- **Type:** Fixed-speaker embeddings + voice *blending*; not a true cloner. KVoiceWalk / KokoClone add approximate zero-shot.
- **License:** Apache 2.0.
- **Quality:** Surprisingly good for its size, but you can't truly clone Feynman/Malkovich — only approximate via blending.
- **Speed:** ~100-300 ms on CPU; faster on GPU. Comparable to Piper.
- **Pros:** Apache 2.0, tiny, fast, multilingual, great as a generic-voice fallback.
- **Cons:** Not a real cloner. Skip if specific-voice impersonation is the goal.
- **Repo:** https://huggingface.co/hexgrad/Kokoro-82M · clone hack: https://github.com/RobViren/kvoicewalk

**Skipped (too slow for live `/speak`, or otherwise out of scope):**
- **F5-TTS** — 2-4 s for a short phrase on 5090. Top-tier quality after fine-tune, especially for prosody capture (Malkovich), but unusable live. Mentioned only in passing.
- **IndexTTS-2** — few seconds per utterance. Skip for live use.
- **StyleTTS 2** — variable, training-heavy, brittle install. Skip.
- **MARS5/6** — AGPL-3.0 + not particularly fast. Skip.
- **Tortoise TTS** — 3.5× slower than ElevenLabs. Hard skip.
- **Fish Speech 1.5** — non-commercial weights, no compelling speed advantage. Skip.
- **MetaVoice / VALL-E** — abandoned / never released.

---

## 3. Top 5 comparison matrix

| # | Model | Latency (5090) | Training data type | CPU? | GPU? |
|---|---|---|---|---|---|
| 1 | **Chatterbox / Turbo** | ~200 ms first-audio (Turbo); ~400-800 ms total | **Zero-shot:** 5 s reference clip. **Optional fine-tune:** ~10-30 min single-speaker WAV + transcripts. | Yes (slow, ~3-5× realtime) | Yes (recommended; CUDA + ROCm) |
| 2 | **GPT-SoVITS v4** | 0.5-1.5 s for short phrases | **Few-shot:** 5 s reference. **Fine-tune:** 1-60 min single-speaker WAV; integrated WebUI handles slicing + ASR + transcription. | Possible but slow | **Required in practice** (CUDA) |
| 3 | **XTTS-v2 (idiap fork)** | ~200 ms first-chunk streaming; ~1-2 s total | **Zero-shot:** 6 s reference. **Fine-tune:** ~5-30 min single-speaker WAV + transcript (AllTalk wizard handles it). | Yes (slow but viable for short text) | Yes (recommended; CUDA) |
| 4 | **Piper** | **80-150 ms on CPU** | **Fine-tune from base ckpt:** ~30 min - 5 h single-speaker WAV @ 22050 Hz + transcripts (pipe-delimited CSV). No zero-shot. | **Required path** (CPU is the point) | Optional (training only) |
| 5 | **CosyVoice 2** | **~150 ms streaming** | **Zero-shot only:** 3-10 s reference clip. No fine-tune workflow. | Limited | **Required** (CUDA) |

---

## 4. Generation time for a real phrase

Concrete: how long does each model take to generate **"deployment to production done, all tasks cleared"** (~8 words, ~3-4 s of spoken audio) on the 5090?

| Model | Generation time | Real-time factor |
|---|---|---|
| **Piper** (CPU) | ~80-150 ms | ~25-50× realtime |
| **CosyVoice 2** (GPU, streaming) | ~150 ms first-chunk | ~20× realtime |
| **Chatterbox Turbo** (GPU) | ~400-800 ms (first audio at ~200 ms) | ~5-10× realtime |
| **GPT-SoVITS v4** (GPU) | ~0.5-1.5 s | ~3-8× realtime |
| **XTTS-v2** (GPU streaming) | ~1-2 s (first chunk at 200 ms) | ~2-4× realtime |
| **Kokoro-82M** (CPU) | ~100-300 ms | ~10-30× realtime |

All five top picks generate the phrase faster than the phrase plays. For a `/speak` skill called by Claude, this means audio starts within ~200 ms of the call — imperceptible.

---

## 5. Frontends / UIs worth using

| Frontend | Best for | Notes |
|---|---|---|
| **Chatterbox-TTS-Server** (devnen) | **Primary recommendation for `/speak`** | OpenAI-compatible HTTP API. Run it once at boot, `/speak` posts text and plays the returned WAV. Web UI for testing, audiobook chunking, CUDA/ROCm/CPU. https://github.com/devnen/Chatterbox-TTS-Server |
| **AllTalk TTS v2** (erew123) | XTTS-v2 power-users | Windows-friendly installer (`atsetup.bat`), DeepSpeed, low-VRAM mode, **built-in XTTS fine-tuning wizard**, JSON API (drop-in for `/speak`). https://github.com/erew123/alltalk_tts |
| **GPT-SoVITS API mode** | GPT-SoVITS persistent server | The included WebUI has an API tab. Start it once with `api.py`, point `/speak` at it. |
| **TTS-WebUI** (rsxdalv) | Trying lots of models from one UI | Gradio + React. Most models in one app. https://github.com/rsxdalv/TTS-WebUI |
| **Applio** | RVC voice *conversion* (live calls) | Best Windows RVC frontend, **realtime tab** for live calls. Maintenance mode now. https://github.com/IAHispano/Applio |

**RVC vs TTS:** RVC (Retrieval-based Voice Conversion) is *voice-to-voice* — record yourself, it re-renders in a target voice. Useful for live-mic interactions or to post-process a TTS that has the wrong timbre. *Not* a substitute for TTS.

---

## 6. Fine-tuning notes & dataset prep

### 6.1 GPT-SoVITS v4 fine-tuning on a 5090
- **Data needed:** 1 min minimum for usable clone; 5-30 min for high quality; 1-2 h = near-zero-shot from training distribution. v4 fussy about audio quality — clean, single-speaker, consistent mic, **16-22 kHz minimum source** ideally bumped to 48 kHz.
- **Pipeline:** Included one-click triple-action button handles slicing → ASR → transcription correction. Use the integrated WebUI; don't roll your own dataset scripts.
- **Training time on 5090:** SoVITS stage ~30 min for small datasets; GPT stage ~30-60 min. Complete fine-tune on 30 min of audio finishes in well under 2 h. 32 GB VRAM means aggressive batch sizes.
- **Gotcha:** If source has noise/reverb, train v1/v2/v2Pro instead — v3/v4 overfit on artifacts.
- **Why this is the primary fine-tune pick:** post-training inference is sub-second on a 5090, fitting the live-TTS pattern.

### 6.2 Piper fine-tuning on a 5090 (CPU-inference path)
Piper is the right choice when you need a cloned-ish voice with <100 ms CPU latency at runtime. Lower quality than GPT-SoVITS, but no GPU footprint at inference. Use the **active fork: `OHF-Voice/piper1-gpl`** — the original `rhasspy/piper` was archived 2025-10-06.

- **Data needed:** ~1,300 utterances is the community sweet spot; ~13,000 for from-scratch (don't). 30 min minimum for a usable fine-tune from a base checkpoint.
- **Dataset format:** Pipe-delimited CSV `utt.wav|text` (3 cols if multi-speaker). Mono 22050 Hz WAV, ≤ 15 s clips, loudness-normalized ~-23 LUFS. **espeak-ng must be installed** for phonemization. Expand numbers/abbreviations in text before training.
- **Training time on 5090 (fine-tune from base checkpoint):**

  | Dataset | Time | Epochs |
  |---|---|---|
  | 30 min - 1 h | 4-12 h | ~500-1000 |
  | 3-5 h | 12-24 h | ~1000 |
  | 10+ h | 1-2 days | 1000-2000 |

  Quality plateaus often by ~400-700 epochs — pull early checkpoints. Watch `loss_disc_all` flattening.
- **VRAM / batch:** `batch_size=32, max_phoneme_ids=400` fits in 24 GB; 5090's 32 GB lets you push bs=48-64.
- **Command:** `python -m piper.train fit --ckpt_path <base>.ckpt --data.csv_path ... --data.audio_dir ... --model.sample_rate 22050 --data.batch_size 32`. Export to ONNX with `piper.train.export_onnx` after.
- **Windows + sm_120 gotcha:** Native Windows builds with sm_120 are **not** a supported path. Use **WSL2 + Ubuntu 22.04** with PyTorch 2.7+ CUDA 12.8 wheels for training. *Inference* runs natively on Windows — the daily-use path stays Windows-native.
- **Quality reality:** ~3.6-3.8 MOS vs GPT-SoVITS ≈ 4.0+. Captures **timbre** but **loses prosody** — drawl, pacing, idiosyncrasy. Fine for short generic phrases ("task complete"); weak on capturing distinctive Malkovich cadence on a long sentence.

### 6.3 Chatterbox fine-tuning (optional, not necessary)
Chatterbox zero-shot is good enough that fine-tuning is rarely worth it. If you want it:
- Data needed: ~10-30 min single-speaker WAV + transcripts.
- Training time on 5090: ~few hours.
- Use cases: nailing a very distinctive voice that zero-shot misses, or building a permanent default voice.
- For your case: zero-shot from a 10-second reference clip is the right answer.

### 6.4 Dataset prep pipeline (regardless of model)
1. **Source audio** → mono WAV, 44.1 or 48 kHz (22050 Hz for Piper).
2. **Denoise:** rnnoise (CLI) or Resemble's **resemble-enhance** for restoration on old tapes. Avoid aggressive removal — it leaves artifacts the model learns.
3. **Diarize + segment:** WhisperX gives word-level timestamps + speaker labels in one pass on a 5090 (~70× realtime with `large-v3`). Keep only segments where the target is the sole speaker.
4. **Slice** into 4-12 s clips (≤15 s for Piper).
5. **Transcribe** with Whisper large-v3 / faster-whisper, then **hand-correct** the top 20% — bad transcripts wreck training more than noise does.
6. **VAD trim** silence; loudness-normalize to -23 LUFS.
7. **Spot-check 10 random clips** by ear before committing to a multi-hour training run.

---

## 7. Cloning real people — audio sources

### 7.1 Richard Feynman

#### Sources

| Source | Format / Quality | Hours | Notes |
|---|---|---|---|
| [Caltech Intro Physics Lectures](https://www.feynmanlectures.caltech.edu/recordings.html) | 48 kHz Opus stream (96/24 WAV masters in Caltech Archives) | ~60 h across vols I-III (1961-64) | Definitive source. Mono, ~8 kHz effective bandwidth, room reverb, chalkboard noise. Rip with `yt-dlp` or browser DevTools. |
| [Messenger Lectures (Cornell, 1964)](https://archive.org/details/academictorrents_c5af268ec55cf2d3b439e7311ad43101ba8322eb) | Internet Archive WAV/MP3 + video | ~7 h | Different mic and room than Caltech; cleaner. Topic: *The Character of Physical Law*. |
| [feynman-lectures (Internet Archive)](https://archive.org/details/feynman-lectures) | Mixed MP3/WAV | ~50 h | Mirror/re-uploads of Caltech material. Quality varies. |
| Esalen Institute lectures (1984) | Cassette rips, YouTube and IA | ~10 h | Older Feynman, philosophical — different vocal energy. |
| PBS *The Pleasure of Finding Things Out* (1981) | Documentary audio | ~50 min | Studio-mic'd interview. Among the cleanest Feynman audio anywhere. |
| BBC *Horizon: The Quest for Tannu Tuva* | Documentary audio | ~50 min | Late-life Feynman, conversational. |
| [Caltech Archives accession 2669](https://collections.archives.caltech.edu/repositories/2/accessions/2669) | Original 1/4″ reel-to-reel masters | varies | In-person consultation only. |

#### Quality realities
- 1961-64 tapes are **mono, ~8 kHz effective bandwidth**, with room reverb, tape hiss, chalkboard transients.
- **One lecture** has clipping damage; Caltech provides both original and reconstruction.
- Expect to discard 30-50% of raw audio (Feynman moving off-mic, student interjections, blackboard noise).

#### Data prep tips (Feynman-specific)
- **Don't over-denoise.** Aggressive removal will make him sound underwater. Light spectral gating + resemble-enhance gives best results.
- **Diarize hard.** Students ask questions, TAs interject. WhisperX with pyannote will pick this up; verify by sampling.
- **Up-sample carefully.** Source is effectively narrowband; modern TTS will *extrapolate* high frequencies — GPT-SoVITS v4's native 48 kHz vocoder is the sweet spot.
- **Vocabulary matters.** Feynman pronounces a *lot* of physics jargon. Include "Hamiltonian", "renormalization" etc. in training transcripts so the model learns his cadence on them.
- **Curate clips by energy level.** Quiet explanatory Feynman and excited gesticulating Feynman are almost different speakers. Either mix or split.

#### Recommended path
1. Download Caltech lectures (`yt-dlp` from feynmanlectures.caltech.edu, or IA WAV bundle).
2. WhisperX diarize+transcribe.
3. Keep only Feynman-only segments, 4-12 s, hand-corrected transcripts.
4. Aim for **2-5 h of clean curated audio**.
5. Fine-tune **GPT-SoVITS v4**. SoVITS ~20 epochs, GPT ~15. Listen, iterate.

### 7.2 John Malkovich

Malkovich's source quality is far better than Feynman's, but his prosody is the whole point and live-TTS models capture it imperfectly. Best real-time option is **GPT-SoVITS v4 fine-tune** — acknowledge the cadence won't be 100% (F5-TTS would do better but is too slow for live use).

#### Sources

| Source | Format / Quality | Hours | Notes |
|---|---|---|---|
| *Heart of Darkness* — Audible, 2010 | Studio audiobook, 44.1 kHz | ~3 h | **Best single training source.** Single speaker, studio mic, no music. Audible / library Libby. |
| *Animal Farm* — Audible | Studio audiobook | ~3 h | Same quality bar; different cadence (storytelling vs narration). Mixes well with HoD. |
| [Eames: The Architect and the Painter (2011)](https://www.imdb.com/title/tt1880565/) | Documentary narration | ~1.3 h | Studio voiceover, conversational tone. |
| Joe Rogan Experience #1657 (2021) | Podcast | ~2 h | Decent mic, conversational. Less clean but adds spontaneous prosody. |
| Marc Maron *WTF* #859 (2017) | Podcast | ~1.5 h | Similar to Rogan. |
| Charlie Rose interviews | Studio TV audio | several h | YouTube. Clean studio mic. |
| *Empire of the Sun* / *Dangerous Liaisons* / *In the Line of Fire* | Film dialogue | hours | Use sparingly — music + other actors require diarization and SFX removal. |

#### Recommended path
1. Acquire *Heart of Darkness* audiobook (Audible/Libby). 3 h of pristine single-speaker audio.
2. Add *Animal Farm* + *Eames* narration for cadence variety.
3. WhisperX transcribe (no diarization needed — single speaker), hand-correct.
4. Fine-tune **GPT-SoVITS v4** for live inference. SoVITS ~20 epochs, GPT ~15.
5. Tradeoff: cadence won't be 100% Malkovich (F5-TTS would do better but is too slow for live `/speak`).

**Acquisition note:** Audible files are DRM'd; library Libby/OverDrive copies sync as DRM-free MP3 on some platforms. AAX → MP3 conversion (`OpenAudible`, `AAXtoMP3`) is broadly defensible for personal-use training; redistribution of a model trained on copyrighted commercial recordings is a separate question — keep it local.

---

## 8. Giving Claude a voice — practical wiring

Use case: Claude generates a sentence at end of turn ("deployment to production done, all tasks cleared"), then calls the `/speak` skill which TTSes it live. Goal: simple, no persistent processes, no idle VRAM.

### 8.1 The pattern: CLI invocation per call (skip the server)

Forget persistent servers. Every model has a CLI; `/speak` invokes it, waits for the WAV, plays it, exits. Cold-start cost matters because it dominates wall-clock time for one-shot calls.

### 8.2 Cold-start + generation totals (3-4 s phrase on 5090)

| Model | Cold start | Generation | Total wall-clock |
|---|---|---|---|
| **Piper** (CPU, ONNX) | ~50-200 ms | ~80-150 ms | **~250-400 ms** ✅ |
| **Kokoro-82M** (CPU/GPU) | ~500-1000 ms | ~100-300 ms | ~700 ms-1.3 s ✅ |
| **Chatterbox CLI** (GPU) | ~3-5 s | ~400-800 ms | ~4-6 s ⚠️ |
| **GPT-SoVITS CLI** (GPU) | ~3-5 s | ~0.5-1.5 s | ~4-6 s ⚠️ |
| **XTTS-v2 `tts` CLI** (GPU) | ~3-5 s | ~1-2 s | ~4-7 s ⚠️ |
| **CosyVoice CLI** (GPU) | ~3-5 s | ~150 ms-1 s | ~4-6 s ⚠️ |

Piper is the only model that's CLI-snappy. The others spend most of their time loading weights into VRAM — fine for occasional end-of-task calls, painful for snappy interactive use.

### 8.3 CLI commands

```powershell
# Piper (current /speak path)
echo "deployment to production done" | piper -m feynman.onnx -f out.wav

# Chatterbox
python -m chatterbox.cli --text "..." --voice ref.wav --out out.wav

# GPT-SoVITS (after fine-tune)
python GPT_SoVITS/inference_cli.py --gpt feynman.ckpt --sovits feynman.pth --ref ref.wav --text "..." --out out.wav

# XTTS via coqui-tts
tts --text "..." --model_name tts_models/multilingual/multi-dataset/xtts_v2 --speaker_wav feynman.wav --language_en --out_path out.wav

# Kokoro
python -m kokoro_onnx --text "..." --voice af_heart --out out.wav
```

### 8.4 Recommendation: fine-tuned Piper as the primary, Chatterbox CLI optional

**Stick with CLI, use fine-tuned Piper.** Two reasons:

1. **No server to manage.** Claude calls `/speak`, Piper runs, audio plays, process exits. Zero idle resources, zero startup-script complexity, zero "is the server alive?" edge cases.
2. **The quality gap matters less than it sounds.** For end-of-task announcements (short phrases, cloned voice approximation), fine-tuned Piper gets you 85% of the way there at 25× less latency. The remaining 15% only matters for long expressive sentences, which `/speak` rarely says.

**When CLI cold-start is fine:** if `/speak` only fires a few times an hour, a 4-second Chatterbox cold-start is invisible — the phrase plays right when you'd expect it anyway. So **Chatterbox CLI is a viable upgrade** if you want zero-shot any-voice and you're OK waiting ~4 s for end-of-task audio.

### 8.5 Voice choice
- **Your own voice:** Best for "this is *my* agent talking back to me." Slightly uncanny first week, you stop noticing.
- **Feynman:** Joyful, curious, mid-frequency-rich. Great for "build passed" / "interesting result, take a look."
- **Malkovich:** Deliberate, theatrical. Excellent for "deployment to production successful." Wears out faster than Feynman in casual back-and-forth.
- **Daily recommendation:** Feynman, with Malkovich on rotation for production deploys.

### 8.6 Implementation sketch

1. **One-time:** Fine-tune Piper on Feynman (2-5 h curated audio, WSL2 training, see Section 6.2). Export to ONNX. Drop the `.onnx` into your Piper voices directory.
2. **Update `/speak` skill:** Point it at `feynman.onnx` instead of `libritts_r-medium`. One config line change.
3. **Optional upgrade path:** Install `chatterbox-tts` Python package. Add a `--high-quality` flag to `/speak` that uses Chatterbox CLI with a reference WAV. Use for special phrases (prod deploys) where the 4-second cold-start is acceptable.
4. **Auto-trigger via `Stop` hook** in `~/.claude/settings.json` so Claude announces *automatically* at end of turn:
   ```jsonc
   "hooks": {
     "Stop": [{
       "hooks": [{ "type": "command",
                   "command": "powershell -NoProfile -File C:/Users/rwa/.claude/scripts/speak-stop.ps1" }]
     }]
   }
   ```
   Script reads the last sentence from Claude's transcript and calls `/speak`.

### 8.7 Why CLI beats the server pattern for this use case
- **No persistent VRAM.** GPU stays fully available for ComfyUI / training / Claude.
- **No autostart complexity.** No Task Scheduler entry, no Windows service, no "did the server die" checks.
- **Crash-safe.** A `/speak` invocation can fail without affecting anything else.
- **Cost:** higher per-call latency for non-Piper models. For end-of-task announcements, you don't care.

---

## 9. Ethics & legal

### Feynman (deceased 1988)
Personal, private use sits in a real grey area but is broadly tolerated. Right-of-publicity rights generally lapse at death in most US states, though some (CA, TN with 2024 ELVIS Act, NY) have post-mortem protections extending decades. Feynman's estate is administered by his family and Caltech; no known aggressive action against fan use, but they *could*.

### Malkovich (living)
- US right-of-publicity rights are **fully active** for living people. CA (where he's based) has very strong protections.
- The federal **NO FAKES Act** (2024, advancing through 2025-26) specifically targets unauthorized AI voice clones of identifiable living people.
- Malkovich has been vocal about AI/likeness issues. He could pursue if it became public.
- **Personal use, kept private:** still legally low-risk, same as Feynman. **Anything published:** much higher risk than a 35-years-dead physicist.

### The line moves sharply when you
- **Publish or distribute** clones — publicity-rights question; Caltech also holds copyright on the digitized Feynman files.
- **Put words in their mouth** they never said on topics they had no view on, especially endorsements.
- **Train on copyrighted source recordings** — personal use *probably* defensible as fair use; redistribution is not.

### For your use case (personal AI assistant, just for you)
Ethically a private homage. Legally low risk. Don't publish clips, don't have it endorse anything. Cloning your *own* voice has none of these issues — just don't use it for fraud, and consider that any audio your assistant emits in your voice could be misused if it leaks.

Modern open-source cloners increasingly ship **watermarks** (Chatterbox's PerTh, Resemble Detect). For personal use this is fine; if you want clean unwatermarked output you'll need to fine-tune GPT-SoVITS or Piper yourself — neither watermarks by default.

---

## 10. References

**Comparison + roundup**
- [Best Open-Source TTS Models 2026 — BentoML](https://www.bentoml.com/blog/exploring-the-world-of-open-source-text-to-speech-models)
- [Ultimate Guide: Best Open Source Voice Cloning Models 2026 — SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-models-for-voice-cloning)
- [Best Open-Source Alternatives to ElevenLabs 2026 — bymar.co](https://blog.bymar.co/posts/open-source-voice-cloning-alternatives-elevenlabs-2026/)
- [XTTSv2 / F5-TTS / GPT-SoVITS-v2 side-by-side demos](https://tts.x86.st/)
- [Best ElevenLabs Alternatives 2026 — Nerdynav](https://nerdynav.com/open-source-ai-voice/)
- [Local TTS & Voice Cloning 2026 comparison — PromptQuorum](https://www.promptquorum.com/power-local-llm/local-tts-voice-cloning-piper-coqui-xtts)
- [awesome-ai-voice list](https://github.com/wildminder/awesome-ai-voice)

**Models**
- [Chatterbox — Resemble AI](https://www.resemble.ai/chatterbox/) · [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) · [devnen/Chatterbox-TTS-Server](https://github.com/devnen/Chatterbox-TTS-Server)
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) · [v3/v4 features wiki](https://github.com/RVC-Boss/GPT-SoVITS/wiki) · [Practical guide](https://medium.com/@akshit0405/gpt-sovits-a-practical-guide-to-voice-synthesis-using-python-cce78818c933)
- [XTTS-v2 HF (CPML)](https://huggingface.co/coqui/XTTS-v2) · [idiap/coqui-ai-TTS fork](https://github.com/idiap/coqui-ai-TTS) · [coqui-tts on PyPI](https://pypi.org/project/coqui-tts/)
- [piper1-gpl TRAINING.md (OHF-Voice)](https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/TRAINING.md) · [piper1-gpl docs](https://thedocs.io/piper1-gpl/usage/training/) · [ssamjh – Create Custom Piper TTS Voice](https://ssamjh.nz/create-custom-piper-tts-voice/)
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) · [CosyVoice2-0.5B HF](https://huggingface.co/FunAudioLLM/CosyVoice2-0.5B)
- [Sesame CSM](https://github.com/SesameAILabs/csm) · [CSM Voice Cloning fork](https://github.com/isaiahbjork/csm-voice-cloning)
- [Kokoro-82M HF](https://huggingface.co/hexgrad/Kokoro-82M) · [KVoiceWalk](https://github.com/RobViren/kvoicewalk)

**Frontends**
- [AllTalk TTS](https://github.com/erew123/alltalk_tts) · [QuickStart](https://github.com/erew123/alltalk_tts/wiki/AllTalk-V2-QuickStart-Guide)
- [TTS-WebUI](https://github.com/rsxdalv/TTS-WebUI)
- [Applio](https://github.com/IAHispano/Applio)

**Feynman audio**
- [Feynman Lectures Recordings (Caltech)](https://www.feynmanlectures.caltech.edu/recordings.html) · [Messenger Lectures on IA](https://archive.org/details/academictorrents_c5af268ec55cf2d3b439e7311ad43101ba8322eb) · [feynman-lectures on IA](https://archive.org/details/feynman-lectures)

**Data prep**
- [WhisperX](https://github.com/m-bain/whisperx) · [Whisper transcription + diarization tutorial](https://towardsdatascience.com/unlock-the-power-of-audio-data-advanced-transcription-and-diarization-with-whisper-whisperx-and-ed9424307281/)

**RTX 5090 / sm_120**
- [PyTorch sm_120 / WSL2 setup for 5090](https://medium.com/@getnetdemil/getting-pytorch-to-actually-use-your-rtx-5090-a-complete-wsl2-setup-guide-for-blackwell-sm-120-61f86f64abc4) · [PyTorch issue #159207 – CUDA sm_120 support](https://github.com/pytorch/pytorch/issues/159207)

**Ethics / legal**
- [Voice Cloning Legal & Ethical Guide 2026 — Audioscripter](https://www.audioscripter.com/blog/voice-cloning-legal-ethical-guide) · [Right of Publicity & Synthetic Voice Regs — Rocklaw](https://www.rock.law/voice-cloning-ai-audio-legal-issues-right-publicity-synthetic-regulations/) · [The Law Speaks Up — Duquesne Juris](https://sites.law.duq.edu/juris/2025/11/25/the-law-speaks-up-ai-voice-cloning-and-consent/)
