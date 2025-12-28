import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from app.core.embedding import get_embedding
import logging
from app.core.utils import get_uploaded_files

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="docs")

logger = logging.getLogger(__name__)

def add_documents_to_vector_store(docs: list[str], ids: list[str], filename: str) -> None:
    try:
        vectors = [get_embedding(text) for text in docs]
        cooection.add(documents=docs, embeddings=vectors, ids=ids, metadatas=[{"filename": filename} for _ in docs])

    except Exception as e:
        logger.error(f"Error adding documents to vector store: {e}")
        raise ValueError(f"Failed to add documents to vector store: {e}")

        
def query_similar_document(query: str, top_k: int = 3) -> list[str]:
    try:
        context_files = get_uploaded_files()
        print(f"Context files available: {context_files}")
        if len(context_files) == 0:
            return []

        query_vector = get_embedding(query)
        results = collection.query(query_embedding = [query_vector], n_results= tok_k, where = {"filename": {"$in": context_files}})

        return results["documents"][0]
    except Exception as e:
        logger.error(f"Error querying similar documents: {e}")
        raise ValueError(f"failed to uery similar documents: {e}")



