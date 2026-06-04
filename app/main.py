from fastapi import FastAPI

from app.routes.projects import router as projects_router
from app.routes.blogs import router as blogs_router

app = FastAPI(
    title="AI Portfolio Platform"
)

app.include_router(
    projects_router,
    prefix="/projects",
    tags=["Projects"]
)

app.include_router(
    blogs_router,
    prefix="/blogs",
    tags=["Blogs"]
)

@app.get("/")
def root():
    return {
        "message": "AI Portfolio Backend Running"
    }