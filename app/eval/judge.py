"""Day 17: LLM-as-judge for faithfulness scoring.

Design decision: human labelling doesn't scale to CI. Calibrated on
30 hand labels; treat scores as a relative signal, not an absolute one.
"""


def score_faithfulness(question: str, answer: str, citations: list[dict]) -> float:
    # TODO(day 17): prompt a judge model to score whether the answer is
    # faithful to the retrieved citations. Return a 0-1 score.
    raise NotImplementedError("score_faithfulness: not implemented yet (day 17)")
