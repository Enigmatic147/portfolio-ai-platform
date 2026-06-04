from fastapi import FastAPI

from app.routes.projects import router as projects_router
from app.routes.blogs import router as blogs_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="AI Portfolio Platform"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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