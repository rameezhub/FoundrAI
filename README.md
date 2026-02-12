FoundrAI

FoundrAI is a simple startup idea evaluation tool built using FastAPI + React (Vite).
The goal of this project is to help founders quickly analyze their startup ideas based on basic parameters like problem statement, industry, revenue model, and target audience.
It calculates a feasibility score, assigns a risk level, and stores idea history in a database.

🛠 Tech Stack
Backend
FastAPI
SQLAlchemy
SQLite
=
Uvicorn

Frontend
React (Vite)
Tailwind CSS
Fetch API
💡 How It Works

User enters:

Problem
Target Audience
Revenue Model
Industry
Region
Frontend sends data to the backend using a POST request.

Backend:

Calculates score using a scoring engine
Classifies risk level
Stores idea in database
Returns analysis result

Frontend displays:

Final score
Risk level
Explanation
Similar existing startups (if available)

Features
Startup idea scoring
Risk classification
Database storage of ideas
Idea history endpoint
Simple modern UI
API documentation with Swagger

🧠 Why I Built This

I wanted to build something that combines:
Backend development
API design
Database handling
Frontend integration
This project helped me understand full-stack architecture and how frontend and backend communicate.

🚀 Future Improvements:

Add authentication
Improve scoring algorithm
Add real startup comparison from database
Deploy online (Render / Railway / Vercel)
Add charts & visualization

👨‍💻 Author
Rameez Sarguru
Computer Engineering Student
