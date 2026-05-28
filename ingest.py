from app.services.notion_sync import fetch_database
from app.config import settings

pages = fetch_database(
    settings.KNOWLEDGE_DB_ID
)