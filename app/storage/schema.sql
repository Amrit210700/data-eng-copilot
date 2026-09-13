-- Day 18: Postgres schema for query logging and feedback.

CREATE TABLE IF NOT EXISTS queries (
    query_id        UUID PRIMARY KEY,
    endpoint        TEXT NOT NULL,
    question        TEXT NOT NULL,
    status          TEXT NOT NULL,          -- answered | refused | generated | needs_clarification
    response        JSONB NOT NULL,
    cache_hit       BOOLEAN NOT NULL DEFAULT FALSE,
    cost_usd        NUMERIC(10, 6),
    latency_ms      NUMERIC(10, 2),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS feedback (
    id              BIGSERIAL PRIMARY KEY,
    query_id        UUID NOT NULL REFERENCES queries(query_id),
    helpful         BOOLEAN NOT NULL,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_queries_created_at ON queries (created_at);
CREATE INDEX IF NOT EXISTS idx_feedback_query_id ON feedback (query_id);
