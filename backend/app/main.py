from flask import Flask
from flask_cors import CORS
from app.core.logger import setup_logging
from app.routes import routes_bp
import os
from dotenv import load_dotenv
from app.core.config import Config

load_dotenv()

app=Flask(__name__)

CORS(app, resources={r"/*":{"origins":"*"}})

app.register_blueprint(routes_bp)

app.comfig['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH_MB * 1024 *1024

@app.route("/")
def root():
    return {"message": "Document Search Bot API (FLASK) is running"}
    