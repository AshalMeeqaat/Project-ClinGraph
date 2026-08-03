# ClinGraph Methodology

## Objective

ClinGraph is an AI-powered biomedical knowledge graph system that enables retrieval of biomedical entities and relationships using Neo4j, FastAPI, and OpenWebUI.

---

## Overall Pipeline

Raw Hetionet Dataset
        ↓
Data Preprocessing
        ↓
CSV Generation
        ↓
Neo4j Graph Database
        ↓
FastAPI Backend
        ↓
OpenWebUI
        ↓
Large Language Model

---

## Technologies

- Python
- Neo4j
- Cypher
- FastAPI
- Poetry
- OpenWebUI
- Docker

---

## Workflow

1. Download Hetionet
2. Clean node and relationship files
3. Generate Neo4j CSVs
4. Import into Neo4j
5. Build REST APIs
6. Connect OpenWebUI
7. Query using LLM