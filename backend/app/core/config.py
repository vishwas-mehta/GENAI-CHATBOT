import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_PORT = int(os.getenv("APP_PORT", 8000))
    ALLOWED_EXTENSIONS = {"pdf", "docx", "pptx", "xlsx"}
    MAX_CONTENT_LENGTH_MB = int(os.getenv("MAX_CONTENT_LENGTH_MB", 5))