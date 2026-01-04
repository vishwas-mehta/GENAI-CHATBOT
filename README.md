# 🤖 GENAI-CHATBOT

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Store-FF6B6B?style=for-the-badge)](https://www.trychroma.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🔍 A Document-based AI Chatbot powered by GenAI for intelligent document search and question answering.

## 📋 Overview

This project is an **intelligent document search bot** powered by **Retrieval-Augmented Generation (RAG)**. Users can upload documents, and the system will index them using vector embeddings. When a user asks a question, the bot retrieves the most relevant document chunks using semantic similarity search (ChromaDB) and uses an LLM (via HuggingFace Inference API) to generate accurate, context-aware answers.

### 🧠 How It Works

1. **Document Upload** → Files are parsed and text is extracted
2. **Embedding Generation** → Text is converted to vector embeddings using HuggingFace models
3. **Vector Storage** → Embeddings are stored in ChromaDB for efficient similarity search
4. **Query Processing** → User queries are matched against stored embeddings
5. **Answer Generation** → Relevant context is passed to an LLM for accurate responses

### ✨ Key Features

- **📄 Multi-format Document Support**: Upload and process PDF, DOCX, PPTX, XLSX, and TXT files
- **🔎 Intelligent Text Extraction**: Automatic text extraction using specialized parsers
- **🗄️ Vector Store Integration**: ChromaDB-powered semantic search for efficient document retrieval
- **🤖 LLM-Powered Q&A**: Get context-aware answers using HuggingFace Inference API
- **📁 File Management**: Full CRUD operations for managing uploaded documents
- **🌐 RESTful API**: Clean Flask-based API endpoints for seamless integration
- **⚡ Fast Retrieval**: Semantic search with cosine similarity for quick relevant document matching

## 🏗️ Project Structure

```
GENAI-CHATBOT/
├── backend/
│   ├── app/
│   │   ├── core/              # Core AI/ML modules
│   │   │   ├── config.py      # Environment configuration
│   │   │   ├── doc_loader.py  # Document text extraction
│   │   │   ├── chroma_store.py # ChromaDB vector store
│   │   │   ├── embedding.py   # HuggingFace embedding generation
│   │   │   └── llm_query.py   # LLM query and response generation
│   │   ├── main.py            # Flask application entry point
│   │   └── routes.py          # API route definitions
│   ├── uploads/               # Uploaded documents storage
│   ├── requirements.txt       # Python dependencies
│   └── run.py                 # Application runner
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend Framework** | Flask |
| **CORS Handling** | Flask-CORS |
| **Vector Store** | ChromaDB, FAISS |
| **LLM Integration** | Together AI |
| **Document Parsing** | PyPDF2, python-docx, python-pptx, PyMuPDF |
| **Embeddings** | HuggingFace Hub |
| **Environment** | python-dotenv |

## 🔌 API Endpoints

### Health Check
- **GET** `/` - Returns API status message

### Document Upload
- **POST** `/upload` - Upload documents for indexing
  - Accepts: `multipart/form-data` with `files` field
  - Supported formats: PDF, DOCX, PPTX, XLSX, TXT

### Query
- **POST** `/query` - Query the indexed documents
  - Body: `{ "query": "your question here" }`
  - Returns: AI-generated answer based on document context

### File Management
- **GET** `/files` - List all uploaded files
  - Returns: List of filenames in the upload directory
- **DELETE** `/files/<filename>` - Delete a specific file
  - Removes file from storage and ChromaDB index

### 📝 Usage Examples

**Upload a document:**
```bash
curl -X POST http://localhost:5000/upload \
  -F "files=@/path/to/document.pdf"
```

**Query your documents:**
```bash
curl -X POST http://localhost:5000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the main topic of the document?"}'
```

**List all uploaded files:**
```bash
curl http://localhost:5000/files
```

**Delete a file:**
```bash
curl -X DELETE http://localhost:5000/files/document.pdf
```

## 🚀 Installation

### Prerequisites
- Python 3.9+
- pip

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/vishwas-mehta/GENAI-CHATBOT.git
cd GENAI-CHATBOT
```

2. **Install dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

3. **Set up environment variables:**
```bash
# Create a .env file in the backend directory
cp .env.example .env
# Add your API keys and configuration
```

4. **Run the application:**
```bash
python run.py
```

The server will start at `http://localhost:5000`

## 📊 Development Status

| Module | Status |
|--------|--------|
| Backend Routes | ✅ Complete |
| Document Loaders | ✅ Complete |
| ChromaDB Integration | ✅ Complete |
| Configuration Module | ✅ Complete |
| Embedding Generation | ✅ Complete |
| LLM Query Integration | ✅ Complete |

### Completed Features

- ✅ **Backend Routes** - All API routes for document upload, query, and file management
- ✅ **Document Loaders** - Text extraction for PDF, DOCX, PPTX, XLSX, and TXT files
- ✅ **ChromaDB Integration** - Vector store for document indexing and similarity search
- ✅ **Configuration Module** - Environment-based configuration with dotenv support
- ✅ **Embedding Module** - HuggingFace Inference API for generating semantic embeddings
- ✅ **LLM Query Module** - Together AI and HuggingFace integration for Q&A

## 🗺️ Roadmap

- [x] Complete embedding generation module
- [x] Implement LLM query integration with Together AI
- [ ] Add frontend UI with React/Next.js
- [ ] Implement user authentication
- [ ] Add support for more document formats (Markdown, HTML, CSV)
- [ ] Add conversation history and context management
- [ ] Implement document chunking for better context retrieval
- [ ] Add rate limiting and API key management
- [ ] Deploy to cloud platform (AWS/GCP/Heroku)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [Together AI](https://www.together.ai/) - LLM services
- [HuggingFace](https://huggingface.co/) - Embeddings and models

---

<p align="center">
  <b>Made with ❤️ by <a href="https://github.com/vishwas-mehta">Vishwas Mehta</a></b>
</p>
