"""Cost estimation from token counts, using the table in config.yaml."""
from __future__ import annotations


def estimate_cost_usd(pricing_table: dict, model: str, input_tokens: int, output_tokens: int) -> float:
    rates = pricing_table.get(model, pricing_table.get("_default", {"input": 3.0, "output": 15.0}))
    cost = (input_tokens / 1_000_000) * rates["input"] + (output_tokens / 1_000_000) * rates["output"]
    return round(cost, 6)
