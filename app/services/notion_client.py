from notion_client import Client
from app.config import settings

notion = Client(auth=settings.NOTION_TOKEN)