from fastapi import APIRouter

from app.models.schemas import ExplainRequest, ExplainResponse

router = APIRouter()


@router.post("/v1/explain", response_model=ExplainResponse)
async def explain(request: ExplainRequest) -> ExplainResponse:
    # TODO(day 18): retrieve similar past incidents, ground diagnosis in them.
    raise NotImplementedError("explain: not implemented yet (day 18)")
