"""Day 17: refuse rather than generate from weak retrieval context.

Design decision: some over-refusal accepted, tuned against negative cases,
because a silent wrong answer is worse than a structured refusal.
"""

from app.config import settings


def passes_score_gate(candidates: list[dict]) -> bool:
    # TODO(day 17): compare top retrieval score(s) against
    # settings.retrieval_score_gate, tuned against the negative-case set.
    raise NotImplementedError("passes_score_gate: not implemented yet (day 17)")
