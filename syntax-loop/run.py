#!/usr/bin/env python3
"""CLI entrypoint for the BrainCode syntax-creation loop.

Examples:
    python run.py --dry-run
    python run.py --max-budget 5 --max-iterations 10
    python run.py --reset              # restore docs/ + runs/ to seed state, then exit
    python run.py --reset --dry-run    # reset, then run
    python run.py --from               # start from run.baseline_dir's latest vN/ product instead of Sprint 0, then exit
    python run.py --from ../syntax-loop-favourite-products/v1 --max-budget 5   # a specific version, then run
"""
from __future__ import annotations

import argparse
import datetime
import logging
import os
import sys

import yaml
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from braincode_loop.orchestrator import Orchestrator  # noqa: E402
from braincode_loop.reset import import_baseline, reset_workspace  # noqa: E402
from braincode_loop.run_lock import RunAlreadyActive  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run the BrainCode syntax-creation agentic loop.")
    p.add_argument("--config", default=os.path.join(BASE_DIR, "config", "config.yaml"))
    p.add_argument("--dry-run", action="store_true", help="Force dry-run mode (no API calls, $0 cost), overriding config.yaml.")
    p.add_argument("--max-budget", type=float, default=None, help="Override budget.max_budget_usd.")
    p.add_argument("--max-iterations", type=int, default=None, help="Override budget.max_iterations.")
    p.add_argument("--reset", action="store_true", help="Restore docs/ and runs/ to seed state. Exits afterwards unless another run flag is also given.")
    p.add_argument("--from", dest="from_dir", nargs="?", const="", default=None, metavar="DIR",
                   help="Reset, then import DIR's language-spec.md + glossary.md (or those of DIR's highest vN/ "
                        "subfolder) as the starting point — copied, never modified. Skips Sprint 0; sprint numbering "
                        "continues. DIR defaults to config.yaml -> run.baseline_dir. Exits afterwards unless another "
                        "run flag is also given.")
    p.add_argument("--verbose", action="store_true")
    p.add_argument("--no-log-file", action="store_true", help="Skip writing runs/logs/*.log for this invocation (console output only).")
    return p.parse_args()


def _configure_logging(verbose: bool, write_file: bool) -> str | None:
    """Returns the run's log FOLDER path (or None if --no-log-file), containing
    orchestration.log (this function's own console/orchestration log) and, once
    Orchestrator constructs it, transcript.log (see braincode_loop/transcript.py)."""
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    handlers: list[logging.Handler] = [logging.StreamHandler()]

    run_log_dir = None
    if write_file:
        logs_root = os.path.join(BASE_DIR, "runs", "logs")
        run_log_dir = os.path.join(logs_root, f"run_{datetime.datetime.now():%Y%m%d_%H%M%S}")
        os.makedirs(run_log_dir, exist_ok=True)
        handlers.append(logging.FileHandler(os.path.join(run_log_dir, "orchestration.log"), encoding="utf-8"))

    logging.basicConfig(level=level, format=fmt, handlers=handlers, force=True)
    # --verbose should only make OUR OWN log lines more detailed, never the HTTP/SDK libraries'
    # (their DEBUG output is raw TCP/TLS handshake noise plus, for anthropic, a single-line dump
    # of the entire request body including the full prompt) — cap them regardless of `level`.
    for noisy in ("httpx", "httpcore", "anthropic", "openai", "google_genai", "google.genai", "urllib3"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    return run_log_dir


def main() -> None:
    args = parse_args()
    run_log_dir = _configure_logging(verbose=args.verbose, write_file=not args.no_log_file)
    if run_log_dir:
        logging.getLogger("braincode_loop").info(
            "Logging this run to %s%s (orchestration.log + transcript.log)", run_log_dir, os.sep,
        )

    load_dotenv(os.path.join(BASE_DIR, ".env"))

    with open(args.config, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    importing = args.from_dir is not None
    if args.reset and importing:
        raise SystemExit("--reset and --from are mutually exclusive (--from already resets first).")
    if args.reset or importing:
        run_cfg = config["run"]
        paths = dict(docs_dir=run_cfg["docs_dir"], runs_dir=run_cfg["runs_dir"],
                     sources_path=run_cfg.get("sources_path", "sources/previous_work.md"))
        if importing:
            src = args.from_dir or run_cfg.get("baseline_dir")
            if not src:
                raise SystemExit("--from needs a DIR, or config.yaml -> run.baseline_dir.")
            import_baseline(BASE_DIR, os.path.join(BASE_DIR, src) if not os.path.isabs(src) else src, **paths)
        else:
            reset_workspace(BASE_DIR, **paths)
        if not (args.dry_run or args.max_budget is not None or args.max_iterations is not None):
            logging.getLogger("braincode_loop").info(
                "%s complete. Run `python run.py` to start the run.", "Import" if importing else "Reset",
            )
            return

    if args.dry_run:
        config["run"]["dry_run"] = True
    if args.max_budget is not None:
        config["budget"]["max_budget_usd"] = args.max_budget
    if args.max_iterations is not None:
        config["budget"]["max_iterations"] = args.max_iterations

    orchestrator = Orchestrator(config, base_dir=BASE_DIR, log_dir=run_log_dir)
    try:
        orchestrator.run()
    except RunAlreadyActive as exc:
        logging.getLogger("braincode_loop").error(str(exc))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
