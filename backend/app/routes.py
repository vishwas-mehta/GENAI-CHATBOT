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

ALLOWED_EXTENTIONS = Config.ALLOWED_EXTENSIONS
UPLOAD_FOLDER = Path(Config.UPLOAD_FOLDER)
UPLOAD_FOLDER.mkdir(parents=True, exists_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENTIONS 

@routes_bp.route("/upload", methods=["POST"])
def upload_documents():
    try:
        if "files" not in request.files:
            return jsonify({"error": "No files part in the request"}), 400
        
        files=request.files.getlist("files")

        saved_files = []
        for file in files:
            if file and allowed_file(file.filename):
                filename=secure_filename(file.filename)
                file_path=UPLOAD_FOLDER / filename
                file.save(file_path)
                saved_files.append(str(file_path))
            else:
                return jsonify({"error": f"Unsupported file type: {file.filename}"}), 400
        
        texts = extract_texts_from_filepaths(saved_files)
        if not texts:
            raise Exception(status_code=400, detail="No vaild documents to process.")

        process_documents(texts)
        return jsonify(content = {"message" : "Documents uploaded and indexed successfully."})
    except Exception as e:
        logger.exception("Upload failed")
        return jsonify({"error": "Internal server error during file upload"}), 500



@routes_bp.route("/query", methods=["POST"])
def query_document():
    try:
        query = request.get_json()["query"]
        if not query:
            return jsonify({"error": "Query string is required"}), 400

        logger.info(f"Received query: {query}")

        answer= answer_query(query)
        return jsonify({"status_code": 200, "content": {"question": query, "answer": answer}})

    except Exception as e:
        logger.exception("Query processing failed")
        return jsonify({"error": "Internal server error during query processing"}), 500


@routes_bp.route("/files", methods=["GET"])
def list_files():
    try:
        files = [file.name for file in UPLOAD_FOLDER.iterdir() if file.is_file()]
        return jsonify("files": files)
    except Exception as e:
        logger.exception("Failed to list files")
        return jsonify({"error": "Internal server error during file listing"}), 500   



                

