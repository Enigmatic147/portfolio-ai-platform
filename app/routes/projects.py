from fastapi import APIRouter

from app.services.notion_sync import fetch_database
from app.config import settings

router = APIRouter()

@router.get("/")
def get_projects():

    return fetch_database(
        settings.PROJECTS_DB_ID
    )