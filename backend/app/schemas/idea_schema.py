from pydantic import BaseModel


class IdeaRequest(BaseModel):
    problem: str
    target_audience: str
    revenue_model: str
    industry: str
    region: str


class IdeaResponse(BaseModel):
    id: int
    problem: str
    target_audience: str
    revenue_model: str
    industry: str
    region: str
    final_score: float
    risk_level: str

    class Config:
        from_attributes = True
