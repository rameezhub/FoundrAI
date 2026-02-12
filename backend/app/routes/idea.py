from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.idea_schema import IdeaRequest, IdeaResponse
from app.services.scoring_engine import calculate_score
from app.services.similarity_engine import find_similar_startups
from app.database import SessionLocal
from app.models.idea_model import Idea


router = APIRouter(prefix="/idea", tags=["Idea"])


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Analyze Idea
@router.post("/analyze")
def analyze_idea(data: IdeaRequest, db: Session = Depends(get_db)):

    # 1️⃣ Calculate score
    score_result = calculate_score(data)

    # 2️⃣ Find similar startups
    similar_startups = find_similar_startups(data.industry)

    # 3️⃣ Save to database
    new_idea = Idea(
        problem=data.problem,
        target_audience=data.target_audience,
        revenue_model=data.revenue_model,
        industry=data.industry,
        region=data.region,
        final_score=score_result["final_score"],
        risk_level=score_result["risk_level"]
    )

    db.add(new_idea)
    db.commit()
    db.refresh(new_idea)

    # 4️⃣ Return combined response
    return {
        **score_result,
        "similar_startups": similar_startups
    }


# Get Idea History
@router.get("/history", response_model=list[IdeaResponse])
def get_ideas(db: Session = Depends(get_db)):
    ideas = db.query(Idea).all()
    return ideas
