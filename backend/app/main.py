from fastapi import FastAPI

from app.core.config import settings
from app.routers.health import router as health_router
from app.routers.database import router as database_router
from app.routers.graph import router as graph_router
from app.routers.chat import router as chat_router
from app.routers.openai import router as openai_router
from app.services.schema_loader import schema_loader
from app.routers.groq_test import router as groq_router
from app.routers.neo4j_tool import router as neo4j_tool_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.on_event("startup")
def load_schema():
    schema_loader.load()

app.include_router(health_router)
app.include_router(database_router)
app.include_router(graph_router)
app.include_router(chat_router)
app.include_router(openai_router)
app.include_router(groq_router)
app.include_router(neo4j_tool_router)