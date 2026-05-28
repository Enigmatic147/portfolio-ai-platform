from fastapi import APIRouter

from app.services.notion_sync import fetch_database
from app.config import settings

router = APIRouter()

@router.get("/")
def get_blogs():

    return fetch_database(
        settings.BLOGS_DB_ID
    )