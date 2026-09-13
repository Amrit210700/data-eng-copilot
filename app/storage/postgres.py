"""Day 18: Postgres logging for queries, feedback, and metrics."""


def log_query(query_id: str, question: str, response: dict, latency_ms: float) -> None:
    # TODO(day 18): insert into the queries table (see schema.sql).
    raise NotImplementedError("log_query: not implemented yet (day 18)")


def log_feedback(query_id: str, helpful: bool) -> None:
    # TODO(day 18): insert into the feedback table.
    raise NotImplementedError("log_feedback: not implemented yet (day 18)")


def get_metrics(window_days: int = 30) -> dict:
    # TODO(day 18): aggregate cache hit rate, refusal rate, cost, latency
    # over the given window from the queries table.
    raise NotImplementedError("get_metrics: not implemented yet (day 18)")
