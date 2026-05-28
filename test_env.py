import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("NOTION_TOKEN"))
print(os.getenv("KNOWLEDGE_DB_ID"))