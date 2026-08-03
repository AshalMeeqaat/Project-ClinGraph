from fastapi import FastAPI

app = FastAPI(
    title="ClinGraph API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ClinGraph API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }