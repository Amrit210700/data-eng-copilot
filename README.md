# Data Engineering Copilot

A RAG service a data team would actually use: schema-grounded SQL generation,
Spark error explanation from past incidents, and metadata search — with
measured quality, not vibes.

Status: skeleton scaffolded, all components stubbed. Nothing is implemented
yet — see the `TODO(day N)` markers throughout `app/` for what goes where.

## Build order across the week

| Day | What you add | Why it comes here |
|---|---|---|
| 14 | Catalog indexed in Chroma, semantic search working | Retrieval substrate first — everything sits on it |
| 15 | `POST /v1/ask` end to end, plus a failure log | You need the naive baseline to prove the upgrades worked |
| 16 | Hybrid BM25 + RRF, cross-encoder rerank, ablation table | Fix the failures with measurements attached |
| 17 | Golden set, eval harness, guardrails, CI regression gate | Turns a demo into something defensible |
| 18 | SQL and explain endpoints, semantic cache, Postgres logging, deploy | Assembly and shipping |

## Endpoints

| Endpoint | Input | Returns |
|---|---|---|
| `POST /v1/ask` | Natural-language question | Grounded answer + verified citations, or structured refusal |
| `POST /v1/sql` | Question + optional layer filter | AST-validated Spark SQL, or a clarification question |
| `POST /v1/explain` | Spark stack trace | Diagnosis grounded in retrieved past incidents |
| `POST /v1/feedback` | `query_id` + helpful flag | Written to Postgres; feeds the golden set |
| `GET /v1/metrics` | — | Cache hit rate, refusal rate, cost, latency over 30 days |
| `GET /health` · `/ready` | — | Liveness; readiness including provider circuit-breaker state |

## Design decisions

| Decision | Why | Trade-off accepted |
|---|---|---|
| Hybrid + rerank over dense only | Exact identifiers and error codes failed dense retrieval | +200ms latency |
| Retrieval score gate | Refuse rather than generate from weak context | Some over-refusal; tuned against the negative cases |
| Semantic cache at 0.95 | A false hit is a silent wrong answer | Lower hit rate than a loose threshold |
| AST allow-list + read-only role | Prompts are not a security boundary | Some legitimate queries rejected by the parser |
| Provider adapter layer | Swap Gemini for Azure OpenAI in one file | Cannot use provider-specific niche features |
| LLM-as-judge for faithfulness | Human labelling does not scale to CI | Calibrated on 30 hand labels; relative signal only |

## Project layout

```
app/
  api/            # FastAPI routers, one per endpoint
  retrieval/       # catalog indexing, semantic/hybrid search, reranking
  llm/             # provider adapter, SQL generation, explanation
  guardrails/      # retrieval score gate, SQL AST validator
  cache/           # semantic cache
  storage/         # Postgres logging + schema.sql
  eval/            # golden set, eval harness, LLM-as-judge, ablation
  models/          # pydantic request/response schemas
  main.py          # FastAPI app, router wiring
scripts/
  index_catalog.py # day 14 entrypoint
  run_eval.py      # day 17 entrypoint, wire into CI
data/
  catalog/         # source docs to index (schemas, table/column metadata)
  golden_set/      # day 17 labeled examples
tests/
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Running tests

```bash
pytest
```
