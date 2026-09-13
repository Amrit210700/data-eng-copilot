from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    llm_provider: str = "gemini"
    gemini_api_key: str = ""
    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""

    chroma_persist_dir: str = "./data/chroma_db"
    postgres_dsn: str = "postgresql://localhost:5432/copilot"

    retrieval_score_gate: float = 0.55
    semantic_cache_threshold: float = 0.95

    class Config:
        env_file = ".env"


settings = Settings()
