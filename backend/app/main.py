from flask import Flask
from flask_cors import CORS
from app.core.logger import setup_logging
from app.routes import routes_bp
import os
from dotenv import load_dotenv
from app.core.config import Config

load_dotenv()
