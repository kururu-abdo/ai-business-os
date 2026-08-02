import time
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from app.db.session import get_db

router = APIRouter()

@router.get("/health", status_code=200)
async def health_check(response: Response, db: AsyncSession = Depends(get_db)):
    start_time = time.time()
    health_status = {
        "status": "healthy",
        "timestamp": start_time,
        "services": {"database": "unhealthy"}
    }
    
    try:
        await db.execute(text("SELECT 1"))
        health_status["services"]["database"] = "healthy"
    except Exception as e:
        response.status_code = 503
        health_status["status"] = "unhealthy"
        
    health_status["duration_ms"] = round((time.time() - start_time) * 1000, 2)
    return health_status
