from typing import Literal, Optional

from pydantic import BaseModel


class Citation(BaseModel):
    source: str
    snippet: str
    score: float


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    status: Literal["answered", "refused"]
    answer: Optional[str] = None
    citations: list[Citation] = []
    refusal_reason: Optional[str] = None


class SqlRequest(BaseModel):
    question: str
    layer: Optional[Literal["bronze", "silver", "gold"]] = None


class SqlResponse(BaseModel):
    status: Literal["generated", "needs_clarification"]
    sql: Optional[str] = None
    clarification_question: Optional[str] = None


class ExplainRequest(BaseModel):
    stack_trace: str


class ExplainResponse(BaseModel):
    diagnosis: str
    related_incidents: list[Citation] = []


class FeedbackRequest(BaseModel):
    query_id: str
    helpful: bool


class FeedbackResponse(BaseModel):
    status: Literal["recorded"]


class MetricsResponse(BaseModel):
    window_days: int
    cache_hit_rate: float
    refusal_rate: float
    total_cost_usd: float
    p50_latency_ms: float
    p95_latency_ms: float
