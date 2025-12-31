import requests
from typing import List 
import os
import logging  

headers = {
    "Authorization": f"Bearer {os.getenv("HUGGINGFACEHUB_API_TOKEN")}",
    "Content-Type": "application/json"
}

logger = logging.getLogger(__name__)
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/distilbert-base-nli-mean-tokens")


def get_embedding(text: str) -> List[float]:
    try:
        url = f"https://api-inference.huggingface.co/models/{EMBEDDING_MODEL}"
        print(f"url: {url}")
        response = request.post(url, headers, json = {"inputs": text}, timeout=60, veryify=False)
        response.raise_for_status()
        embedding = response.json()
        return embedding

    except Exception as e:
        logger.exception("Error getting embedding")
        raise ValueError("Failed to get embedding from model.")

        