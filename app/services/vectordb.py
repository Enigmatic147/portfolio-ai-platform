import chromadb

client = chromadb.PersistentClient(
    path="app/chroma_db"
)

collection = client.get_or_create_collection(
    name="portfolio_knowledge"
)

def add_document(doc_id, text, embedding):

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )

def search_documents(query_embedding):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results