import os
import random
import shutil

from braincode_loop import simulation
from braincode_loop.budget import BudgetTracker
from braincode_loop.simulation import SimItem
from braincode_loop.state import LanguageState

BASE_DIR = os.path.join(os.path.dirname(__file__), "..")
SEED_TASKS = os.path.join(BASE_DIR, "braincode_loop", "seed_tasks.json")


def _pool():
    return {
        "seed_tasks": [SimItem(id=f"s{i}", nl=f"seed {i}", source="seed_tasks") for i in range(5)],
        "mind2web": [SimItem(id=f"m{i}", nl=f"web {i}", source="mind2web") for i in range(5)],
        "alfred": [SimItem(id=f"a{i}", nl=f"home {i}", source="alfred") for i in range(2)],
    }


def test_sampling_is_deterministic_and_stratified():
    kwargs = dict(closed_sources=["seed_tasks", "mind2web"], open_sources=["alfred"], per_closed=2, per_open=2)
    a = simulation.sample_items(_pool(), rng=random.Random(1), **kwargs)
    b = simulation.sample_items(_pool(), rng=random.Random(1), **kwargs)
    assert [i.id for i in a] == [i.id for i in b]
    assert sum(i.source == "seed_tasks" for i in a) == 2
    assert sum(i.source == "mind2web" for i in a) == 2
    assert sum(i.source == "alfred" for i in a) == 2
    assert len(a) == 6


def test_sampling_caps_at_available_items_without_crashing():
    """Requesting more items than a source has caps at what's available, no crash — e.g.
    alfred's fixture pool only has 2 items."""
    picked = simulation.sample_items(
        _pool(), closed_sources=["seed_tasks"], open_sources=["alfred"],
        per_closed=3, per_open=10, rng=random.Random(0),
    )
    assert sum(i.source == "alfred" for i in picked) == 2
    assert sum(i.source == "seed_tasks" for i in picked) == 3


def test_load_pool_falls_back_to_seed_samples(tmp_path):
    # Isolated fake project dir: only the .seed.jsonl fallbacks exist here, no fetched .jsonl —
    # exercises the fallback regardless of whether the real repo has since run the fetch script.
    samples_dir = tmp_path / "datasets" / "samples"
    samples_dir.mkdir(parents=True)
    for name in ("mind2web", "alfred", "swebench"):
        shutil.copyfile(
            os.path.join(BASE_DIR, "datasets", "samples", f"{name}.seed.jsonl"),
            samples_dir / f"{name}.seed.jsonl",
        )
    state = LanguageState(str(tmp_path), SEED_TASKS)
    pool = simulation.load_pool(str(tmp_path), ["seed_tasks", "mind2web", "alfred", "swebench", "nonexistent"], state)
    assert set(pool) == {"seed_tasks", "mind2web", "alfred", "swebench"}
    assert all(i.source.startswith("illustrative") for i in pool["mind2web"])
    assert all(i.source.startswith("illustrative") for i in pool["swebench"])
    assert pool["alfred"][0].steps
    assert pool["swebench"][0].steps


def test_load_pool_prefers_real_samples_over_seed(tmp_path):
    samples_dir = tmp_path / "datasets" / "samples"
    samples_dir.mkdir(parents=True)
    (samples_dir / "mind2web.jsonl").write_text(
        '{"id": "real-1", "nl": "a real sampled task", "source": "Mind2Web (real)"}\n', encoding="utf-8",
    )
    state = LanguageState(str(tmp_path), SEED_TASKS)
    pool = simulation.load_pool(str(tmp_path), ["mind2web"], state)
    assert [i.id for i in pool["mind2web"]] == ["real-1"]


def test_should_cross_check_auto_rules():
    budget = BudgetTracker(max_budget_usd=20.0, max_iterations=5)
    base = dict(spec_construct_count=3, budget=budget, n_items=4, n_providers=2)
    adds = [{"op": "add", "change_type": "MINOR"}, {"op": "add", "change_type": "MINOR"}]
    assert simulation.should_cross_check(mode="auto", changes=adds, **base)[0]
    assert not simulation.should_cross_check(mode="never", changes=adds, **base)[0]
    assert simulation.should_cross_check(mode="always", changes=[{"op": "add", "change_type": "PATCH"}], **base)[0]
    ok, why = simulation.should_cross_check(mode="auto", changes=[{"op": "revise", "change_type": "PATCH"}], **base)
    assert not ok and "PATCH" in why
    ok, why = simulation.should_cross_check(mode="auto", changes=adds[:1], **{**base, "spec_construct_count": 0})
    assert not ok and "no constructs" in why
    assert not simulation.should_cross_check(mode="auto", changes=adds, **{**base, "n_providers": 1})[0]
    poor = BudgetTracker(max_budget_usd=0.1, max_iterations=5)
    assert not simulation.should_cross_check(mode="auto", changes=adds, **{**base, "budget": poor})[0]


def test_cross_translate_dry_run_returns_both_providers():
    budget = BudgetTracker(max_budget_usd=20.0, max_iterations=5)
    items = [SimItem(id="x", nl="do x", source="seed_tasks")]
    out = simulation.cross_translate(
        items=items, spec_text="", proposal={"changes": []}, providers=["anthropic", "gemini"],
        models_map={"anthropic": "m1", "gemini": "m2"}, sprint=1, budget=budget,
        pricing_table={"_default": {"input": 1, "output": 1}}, dry_run=True,
    )
    assert set(out["x"]) == {"anthropic", "gemini"}
    assert budget.calls and all(c.role == "cross_check_translator" for c in budget.calls)


def test_cross_translate_drops_items_with_one_provider():
    budget = BudgetTracker(max_budget_usd=20.0, max_iterations=5)
    out = simulation.cross_translate(
        items=[SimItem(id="x", nl="do x", source="s")], spec_text="", proposal={}, providers=["anthropic", "gemini"],
        models_map={"anthropic": "m1"}, sprint=1, budget=budget,
        pricing_table={"_default": {"input": 1, "output": 1}}, dry_run=True,
    )
    assert out == {}


def test_pick_cross_check_items_spans_sources_and_caps():
    from braincode_loop.simulation import SimItem, pick_cross_check_items

    items = [SimItem(id=f"{s}-{i}", source=s, domain="d", nl="x") for s in ("a", "b", "c") for i in range(3)]
    picked = pick_cross_check_items(items, 4)
    assert [i.id for i in picked] == ["a-0", "b-0", "c-0", "a-1"]
    assert pick_cross_check_items(items, None) == items and pick_cross_check_items(items, 50) == items
