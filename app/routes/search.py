from fastapi import APIRouter
from app.services.embeddings import create_embedding
from app.services.vectordb import search_documents

router = APIRouter()

@router.get("/")
def semantic_search(q: str):

    embedding = create_embedding(q)

    results = search_documents(embedding)

    return results