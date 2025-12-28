import chromadb
from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
from app.core.embedding import get_embedding
import logging
from app.core.utils import get_uploaded_files

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="docs")
