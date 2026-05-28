import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    NOTION_TOKEN = os.getenv("NOTION_TOKEN")

    PROJECTS_DB_ID = os.getenv("PROJECTS_DB_ID")

    BLOGS_DB_ID = os.getenv("BLOGS_DB_ID")

    KNOWLEDGE_DB_ID = os.getenv("KNOWLEDGE_DB_ID")

settings = Settings()