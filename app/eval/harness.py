"""Day 17: evaluation harness — runs the golden set through the pipeline
and reports pass/fail suitable for a CI regression gate."""


def run_eval(golden_set: list[dict]) -> dict:
    # TODO(day 17): for each golden example, run /v1/ask (or /v1/sql),
    # score with judge.score_faithfulness, compare against citation
    # ground truth, and aggregate into a pass/fail report.
    raise NotImplementedError("run_eval: not implemented yet (day 17)")
