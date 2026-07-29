from fastapi import FastAPI
from app.routers.health import router

app = FastAPI(
    title="ClinGraph API",
    description="Backend API for ClinGraph",
    version="0.1.0",
)

app.include_router(router)