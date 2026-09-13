"""Day 16: hybrid BM25 + dense retrieval, combined with Reciprocal Rank Fusion."""


def hybrid_search(query: str, k: int = 8) -> list[dict]:
    # TODO(day 16): run BM25 and semantic_search in parallel, fuse rankings
    # with RRF. Exists because exact identifiers/error codes fail dense-only
    # retrieval (see README design decisions).
    raise NotImplementedError("hybrid_search: not implemented yet (day 16)")
