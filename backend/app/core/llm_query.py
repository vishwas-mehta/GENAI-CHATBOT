import os
import requests
import logging
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import chromadb
from chromadb.config import Settings
from app.core.chroma_store import query_similar_documents, add_documents_to_vector_store

from huggingface_hub import InferenceClient

HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
LLM_MODEL = os.getenv("LLM_MODEL")

headers = {
    "Authorization": f"Bearer {os.getenv("HUGGINGFACEHUB_API_TOKEN")}",
    "Content-Type": "application/json"
}

client = chromadb.Client(Settings(persist_directory= "./chroma_store"))

collection = client.get_or_create_collection("documents")

def build_client() -> InferenceClient:
    return InferenceClient(token=HUGGINGFACE_API_TOKEN,
    model = LLM_MODEL,
    timeout=300)
