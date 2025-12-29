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

## API Endpoints

### Health Check
- **GET** `/` - Returns API status message

### Document Upload
- **POST** `/upload` - Upload documents for indexing
  - Accepts: `multipart/form-data` with `files` field
  - Supported formats: PDF, DOCX, PPTX, XLSX

### Query
- **POST** `/query` - Query the indexed documents
  - Body: `{ "query": "your question here" }`
  - Returns: AI-generated answer based on document context

### File Management
- **GET** `/files` - List all uploaded files
  - Returns: List of filenames in the upload directory
- **DELETE** `/files/<filename>` - Delete a specific file
  - Removes file from storage and ChromaDB index

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vishwas-mehta/GENAI-CHATBOT.git
cd GENAI-CHATBOT
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file in the backend directory
# Add your API keys and configuration
```

4. Run the application:
```bash
python run.py
```

## Features

- **Multi-format Document Support**: Upload and process PDF, DOCX, PPTX, XLSX, and TXT files
- **Intelligent Text Extraction**: Automatic text extraction from various document formats using specialized parsers
- **Vector Store Integration**: ChromaDB-powered semantic search for efficient document retrieval
- **LLM-Powered Q&A**: Get context-aware answers to your questions using Together AI
- **File Management**: Full CRUD operations for managing uploaded documents
- **RESTful API**: Clean Flask-based API endpoints for seamless integration

## Status

✅ **Backend Routes Complete** - All API routes for document upload, query, and file management are implemented.

✅ **Document Loaders Complete** - Text extraction for PDF (PyMuPDF), DOCX (python-docx), PPTX (python-pptx), XLSX (openpyxl), and TXT files.

✅ **ChromaDB Integration Complete** - Vector store for document indexing, similarity search, and document deletion by filename.

✅ **Configuration Module Complete** - Environment-based configuration with support for upload folder, log directory, and vector store paths.

🚧 **In Progress** - LLM query integration and embedding generation modules.
