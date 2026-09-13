from fastapi import APIRouter

from app.models.schemas import AskRequest, AskResponse

router = APIRouter()


@router.post("/v1/ask", response_model=AskResponse)
async def ask(request: AskRequest) -> AskResponse:
    # TODO(day 15): naive baseline — retrieve, generate, log failures.
    # TODO(day 16): hybrid BM25 + RRF retrieval, cross-encoder rerank.
    # TODO(day 17): retrieval score gate -> structured refusal path.
    raise NotImplementedError("ask: not implemented yet (day 15)")
