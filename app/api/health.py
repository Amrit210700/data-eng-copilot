from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health() -> dict:
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict:
    # TODO(day 18): include provider circuit-breaker state.
    return {"status": "ready", "circuit_breaker": "unknown"}
