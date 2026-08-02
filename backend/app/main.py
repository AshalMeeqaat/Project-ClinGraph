from fastapi import FastAPI

from app.core.config import settings
from app.routers.health import router as health_router
from app.routers.database import router as database_router
from app.routers.graph import router as graph_router
from app.routers.llm import router as llm_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(health_router)
app.include_router(database_router)
app.include_router(graph_router)
app.include_router(llm_router)