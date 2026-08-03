# ClinGraph Backend

This directory contains the FastAPI backend for the ClinGraph project. It is responsible for handling API requests, communicating with the Neo4j database, and providing services to the Open WebUI frontend.

---

## Prerequisites

Before running the backend, ensure the following are installed:

- Python 3.12+
- Poetry

---

## Install Dependencies

From the `backend` directory, install all required packages:

```bash
poetry install
```

---

## Environment Variables

Create a `.env` file using the `.env.example` template.

Example:

```env
NEO4J_URI=
NEO4J_USERNAME=
NEO4J_PASSWORD=
OLLAMA_BASE_URL=
OPENAI_API_KEY=
```

---

## Run the Backend

Start the FastAPI development server:

```bash
poetry run uvicorn app.main:app --reload
```

The backend will be available at:

```
http://localhost:8000
```

Interactive API documentation:

```
http://localhost:8000/docs
```

---

## Backend Structure

```
backend/
│
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Configuration and settings
│   ├── database/     # Database connections
│   ├── models/       # Data models
│   ├── routes/       # Route definitions
│   ├── services/     # Business logic
│   ├── tests/        # Unit tests
│   └── main.py       # FastAPI application entry point
│
├── .env              # Local environment variables (not committed)
├── .env.example      # Environment variable template
├── pyproject.toml    # Poetry project configuration
├── poetry.lock       # Locked dependency versions
└── README.md         # Backend documentation
```

---

## Current Status

- Poetry configured
- Backend project structure created

## Further Work
- FastAPI application setup
- Neo4j integration
- Open WebUI integration