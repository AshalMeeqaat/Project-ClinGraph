from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to ClinGraph API"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }