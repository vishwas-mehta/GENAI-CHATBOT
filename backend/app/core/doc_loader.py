import os
import fitz
import docx
import openpyxl
from pptx import Presentation
from pathlib import Path
import logging

from app.config import Config
from pathlib import Path

logger = logging.getLogger(__name__)

SUPPORTED_EXTENTIONS = Config.ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path: str) -> str:
    doc= fitz.open(file_path)
    text=""
    for page in doc:
        text+=page.get_text()
    return text

