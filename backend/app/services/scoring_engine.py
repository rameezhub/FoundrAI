from app.services.similarity_engine import find_similar_startups


def calculate_score(data):

    industry_scores = {
        "AI": 90,
        "EdTech": 75,
        "Food Delivery": 60,
        "HealthTech": 85,
        "FinTech": 80
    }

    revenue_scores = {
        "Subscription": 85,
        "Ads": 50,
        "Marketplace": 75,
        "Freemium": 70
    }

    # Base Scores
    market_demand = industry_scores.get(data.industry, 65)
    revenue_strength = revenue_scores.get(data.revenue_model, 60)

    competition_risk = 70 if "delivery" in data.problem.lower() else 40
    tech_feasibility = 85
    scalability = 75

    # Weighted Final Score
    final_score = (
        market_demand * 0.25 +
        competition_risk * 0.20 +
        revenue_strength * 0.20 +
        tech_feasibility * 0.15 +
        scalability * 0.20
    )

    final_score = round(final_score, 2)

    # Risk Classification
    if final_score >= 80:
        risk_level = "Low Risk"
    elif final_score >= 60:
        risk_level = "Medium Risk"
    else:
        risk_level = "High Risk"

    # Similar Startup Matching
    similar_startups = find_similar_startups(data.industry)

    # Analysis Text
    analysis = (
        f"This startup targets {data.target_audience} in the {data.industry} industry. "
        f"The revenue model '{data.revenue_model}' shows moderate potential. "
        f"Competition risk is estimated at {competition_risk}%. "
        f"Overall feasibility score is {final_score}, categorized as {risk_level}."
    )

    # MVP Roadmap
    mvp_roadmap = [
        "Phase 1: Validate demand with landing page",
        "Phase 2: Build core feature MVP",
        "Phase 3: Conduct beta testing",
        "Phase 4: Launch and optimize revenue model"
    ]

    return {
        "market_demand": market_demand,
        "competition_risk": competition_risk,
        "revenue_strength": revenue_strength,
        "tech_feasibility": tech_feasibility,
        "scalability": scalability,
        "final_score": final_score,
        "risk_level": risk_level,
        "analysis": analysis,
        "mvp_roadmap": mvp_roadmap,
        "similar_startups": similar_startups
    }
