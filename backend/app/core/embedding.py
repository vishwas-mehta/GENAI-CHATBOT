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
