from fastapi import FastAPI
from app.core.config import settings
from app.core.logger import setup_logging
from app.api.main import router as api_router

setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

app.include_router(api_router)
