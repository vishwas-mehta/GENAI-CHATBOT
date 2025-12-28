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

        