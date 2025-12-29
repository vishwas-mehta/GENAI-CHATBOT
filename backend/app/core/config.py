import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    ALLOWED_EXTENSIONS = {"pdf", "docx", "pptx", "xlsx"}
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "data/uploads")
    LOG_DIR = os.getenv("LOG_DIR", "logs")
    VECTOR_DIR = os.getenv("VECTOR_DIR", "data/vectorstore")
    MAX_CONTEXT_LENGTH_MB = int(os.getenv("MAX_CONTENT_LENGTH_MB", 2))
    