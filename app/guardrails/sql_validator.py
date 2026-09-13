"""Day 18: AST allow-list validation for generated SQL.

Design decision: prompts are not a security boundary — validate the
generated SQL's AST before it ever runs, against a read-only role.
Trade-off accepted: some legitimate queries get rejected by the parser.
"""


def validate_sql(sql: str) -> bool:
    # TODO(day 18): parse with sqlglot, walk the AST, allow only
    # SELECT statements over allow-listed tables/functions.
    raise NotImplementedError("validate_sql: not implemented yet (day 18)")
