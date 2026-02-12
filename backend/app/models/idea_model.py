from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Idea(Base):
    __tablename__ = "ideas"

    id = Column(Integer, primary_key=True, index=True)
    problem = Column(String)
    target_audience = Column(String)
    revenue_model = Column(String)
    industry = Column(String)
    region = Column(String)
    final_score = Column(Float)
    risk_level = Column(String)
