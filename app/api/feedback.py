from fastapi import APIRouter

from app.models.schemas import FeedbackRequest, FeedbackResponse

router = APIRouter()


@router.post("/v1/feedback", response_model=FeedbackResponse)
async def feedback(request: FeedbackRequest) -> FeedbackResponse:
    # TODO(day 18): write to Postgres, feed the golden set (day 17).
    raise NotImplementedError("feedback: not implemented yet (day 18)")
