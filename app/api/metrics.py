from fastapi import APIRouter

from app.models.schemas import MetricsResponse

router = APIRouter()


@router.get("/v1/metrics", response_model=MetricsResponse)
async def metrics() -> MetricsResponse:
    # TODO(day 18): pull cache hit rate, refusal rate, cost, latency
    # from Postgres logging over a rolling 30-day window.
    raise NotImplementedError("metrics: not implemented yet (day 18)")
