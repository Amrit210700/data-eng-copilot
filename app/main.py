from fastapi import FastAPI

from app.api import ask, explain, feedback, health, metrics, sql

app = FastAPI(title="Data Engineering Copilot")

app.include_router(health.router)
app.include_router(ask.router)
app.include_router(sql.router)
app.include_router(explain.router)
app.include_router(feedback.router)
app.include_router(metrics.router)
