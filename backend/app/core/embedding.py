import requests
from typing import List 
import os
import logging  

headers = {
    "Authorization": f"Bearer {os.getenv("HUGGINGFACEHUB_API_TOKEN")}",
    "Content-Type": "application/json"
}
