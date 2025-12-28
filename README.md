# GENAI-CHATBOT

A Document-based AI Chatbot powered by GenAI for intelligent document search and question answering.

## Overview

This project is an intelligent document search bot that allows users to upload documents and query them using natural language. The backend is built with Flask and integrates with AI/LLM services for generating context-aware responses.

## Project Structure

```
GENAI-CHATBOT/
├── backend/
│   ├── app/
│   │   ├── core/           # Core modules (config, logger, document loaders, LLM query)
│   │   ├── main.py         # Flask application entry point
│   │   └── routes.py       # API route definitions
│   ├── requirements.txt    # Python dependencies
│   └── run.py              # Application runner
└── .gitignore
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend Framework | Flask |
| CORS Handling | Flask-CORS |
| Vector Store | ChromaDB, FAISS |
| LLM Integration | Together AI |
| Document Parsing | PyPDF2, python-docx, python-pptx, PyMuPDF |
| Embeddings | HuggingFace Hub |
| Environment | python-dotenv |
