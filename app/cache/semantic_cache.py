"""Day 18: semantic cache for repeated/near-duplicate questions.

Design decision: threshold set at settings.semantic_cache_threshold (0.95).
Trade-off accepted: lower hit rate than a loose threshold, because a false
hit is a silent wrong answer.
"""

from app.config import settings


def get_cached(query: str) -> dict | None:
    # TODO(day 18): embed query, search cache store for a neighbor above
    # settings.semantic_cache_threshold, return its stored response if hit.
    raise NotImplementedError("get_cached: not implemented yet (day 18)")


def set_cached(query: str, response: dict) -> None:
    # TODO(day 18): store query embedding + response for future lookups.
    raise NotImplementedError("set_cached: not implemented yet (day 18)")
