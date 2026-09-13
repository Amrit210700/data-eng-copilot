from fastapi import APIRouter

from app.models.schemas import SqlRequest, SqlResponse

router = APIRouter()


@router.post("/v1/sql", response_model=SqlResponse)
async def generate_sql(request: SqlRequest) -> SqlResponse:
    # TODO(day 18): retrieve schema context, generate Spark SQL,
    # validate against AST allow-list before returning.
    raise NotImplementedError("sql: not implemented yet (day 18)")
