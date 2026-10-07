#!/usr/bin/env python3
"""Assemble this folder for Google Colab (run locally, from the repository).

    python finetune-qwen/build_folder.py                    # training data + BrainCode kit
    python evaluations/proofwriter/pw.py package            # benchmark/ (after phase 2's translations)

Writes, next to this script:
  data/train.jsonl, data/val.jsonl   training examples (item -> BrainCode), validated against glossary g19
  data/translations/...              the full successful translation documents they come from
  data/manifest.json                 counts and what was filtered out, and why
  braincode_kit/                     the BrainCode reference (glossary g19, compact spec, standards)
                                     and the swarm's RAG + checker code, with the prebuilt index

The training data is exactly the Llama run's (finetune-llama/build_folder.py):
every successful translation that still passes the host check against g19,
identical BrainCode kept once, validation items disjoint from training items.
ProofWriter is not in it.
"""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("llama_build", HERE.parent / "finetune-llama" / "build_folder.py")
llama_build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(llama_build)
llama_build.KIT = HERE / "braincode_kit"
llama_build.DATA = HERE / "data"

if __name__ == "__main__":
    llama_build.build_kit()
    print(json.dumps(llama_build.build_data(), indent=1))
