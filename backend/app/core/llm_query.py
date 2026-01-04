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

def extract_qa(response_text):
    """Extract question and answer from LLM response text."""
    try:
        question_match = re.search(r"(?i)question:\s*(.+)", response_text)
        answer_match = re.search(r"(?i)answer:\s*(.+)", response_text, re.DOTALL)

        question = question_match.group(1).strip() if question_match else ""
        answer = answer_match.group(1).strip() if answer_match else ""

        return question, answer
    except Exception as e:
        logging.error(f"Error extracting QA: {str(e)}")
        raise ValueError("Failed to extract question and answer from the response.")


def answer_query(query: str) -> str:
    """
    Process a user query against indexed documents and return an AI-generated answer.
    
    Args:
        query: The user's question string
        
    Returns:
        AI-generated answer based on document context
    """
    try:
        # Get relevant documents from ChromaDB
        results = query_similar_documents(query, n_results=3)
        
        if not results or not results.get("documents"):
            return "No relevant documents found to answer your query."
        
        # Build context from retrieved documents
        context = "\n\n".join(results["documents"][0]) if results["documents"] else ""
        
        # Build prompt for LLM
        prompt = f"""Based on the following context, please answer the question.

Context:
{context}

Question: {query}

Answer:"""
        
        # Get response from LLM
        client = build_client()
        response = client.text_generation(
            prompt,
            max_new_tokens=500,
            temperature=0.7
        )
        
        return response.strip() if response else "Unable to generate an answer."
        
    except Exception as e:
        logging.error(f"Error answering query: {str(e)}")
        return f"Error processing query: {str(e)}"
    