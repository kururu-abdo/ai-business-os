from fastapi import APIRouter
from .auth import  router
v1_router = APIRouter()
v1_router.include_router(router, tags=["Auth V1"])



