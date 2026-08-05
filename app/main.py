from fastapi import FastAPI
from sqlalchemy.orm import configure_mappers
from app.core.config import settings
from app.api.main import  router as api_router
from app.api.v1.router import v1_router
configure_mappers()
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)
app.include_router(v1_router, prefix="/api/v1")
app.include_router(api_router)

