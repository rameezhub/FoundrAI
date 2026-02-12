from app.services.startup_data import startups

def find_similar_startups(industry):

   

    database = {
        "EdTech": ["Coursera", "Byju's", "Udemy"],
        "AI": ["OpenAI", "Anthropic", "HuggingFace"],
        "HealthTech": ["Practo", "1mg", "HealthifyMe"],
        "Food Delivery": ["Zomato", "Swiggy", "Uber Eats"]
    }

    return database.get(industry, ["No major competitors found"])

