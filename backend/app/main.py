from fastapi import FastAPI

app = FastAPI(
    title="Project ClinGraph API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Project ClinGraph Backend Running"}