from fastapi import APIRouter
from app.services.notion_sync import fetch_database
from app.config import settings

router = APIRouter()

@router.get("/")
def get_blogs():

    pages = fetch_database(settings.BLOGS_DB_ID)

    blogs = []

    for page in pages:

        props = page["properties"]

        # Skip unpublished blogs
        if not props["Published"]["checkbox"]:
            continue

        blogs.append({
            "id": page["id"],
            "title": (
                props["Title"]["title"][0]["plain_text"]
                if props["Title"]["title"]
                else ""
            ),
            "summary": (
                props["Summary"]["rich_text"][0]["plain_text"]
                if props["Summary"]["rich_text"]
                else ""
            ),
            "slug": (
                props["Slug"]["rich_text"][0]["plain_text"]
                if props["Slug"]["rich_text"]
                else ""
            ),
            "published": props["Published"]["checkbox"],
            "date": (
                props["Date"]["date"]["start"]
                if props["Date"]["date"]
                else None
            ),
            "tags": [
                tag["name"]
                for tag in props["Tags"]["multi_select"]
            ]
        })

    return {
        "blogs": blogs
    }