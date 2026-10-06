import os
from pathlib import Path

from dotenv import load_dotenv

repo_root = Path(__file__).resolve().parents[3]
load_dotenv(repo_root / '.env')


class Settings:
    APP_NAME = os.getenv('APP_NAME', 'AI City Command Center')
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./ai_city_command_center.db')
    AI_SERVICE_URL = os.getenv('AI_SERVICE_URL', 'http://localhost:8001')
    AI_TIMEOUT_SECONDS = float(os.getenv('AI_TIMEOUT_SECONDS', '5'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')


settings = Settings()
