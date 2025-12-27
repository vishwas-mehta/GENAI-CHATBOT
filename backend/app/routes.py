from flask import Blueprint, request, jsonify
import os
import logging
from werkzeug.utils import secure_filename
from pathlib import path
from app.core.config import Config
from app.core.doc_loader import extract_texts_from_filepaths
from app.core.llm_query import answer_query
from app.core.process_documents import process_documents
from app.core.chroma_store import delete_document_by_filename

routes_bp = Blueprint("routes", __name__)
logger = logging.getLogger(__name__)

