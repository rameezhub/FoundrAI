from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.idea import router as idea_router
from app.database import engine, Base
from app.models.idea_model import Idea

# Create DB tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app (ONLY ONCE)
app = FastAPI(title="FoundrAI API")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend (localhost:5173)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(idea_router)


# Root route
@app.get("/")
def root():
    return {"message": "FoundrAI Backend Running 🚀"}
