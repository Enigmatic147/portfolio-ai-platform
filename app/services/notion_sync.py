import requests
from app.config import settings

NOTION_VERSION = "2022-06-28"

headers = {
    "Authorization": f"Bearer {settings.NOTION_TOKEN}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json"
}

def fetch_database(database_id):

    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    response = requests.post(
        url,
        headers=headers
    )

    response.raise_for_status()

    data = response.json()

    return data["results"]