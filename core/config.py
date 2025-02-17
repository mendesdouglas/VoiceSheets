import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env, se existir
load_dotenv()

class Config:
    GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE")
    GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
    SHEET_NAME = os.getenv("SHEET_NAME")
    PROJECT_PATH = os.getenv("PROJECT_PATH")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
