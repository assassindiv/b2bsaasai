B2B SaaS AI Copilot – MVP

B2B SaaS AI Copilot – MVP

An embeddable AI widget for SaaS apps that acts as an intelligent onboarding and support agent. 
It understands which page the user is on, reads feature descriptions and FAQs, and responds with contextual answers using Groq's blazing-fast LLMs.

# Features:
- Floating AI widget on any page
- Page-aware context (auto-detects current route)
- Dynamic responses based on feature + FAQ JSON
- Powered by Groq (Mixtral / LLaMA3)
- .env-based API key management
- React frontend + Flask backend
- CORS-enabled, deployable to Render/Vercel
- Easy to expand into full AI agent with memory + config dashboard

# Project Structure:
b2bsaasai/
├── backend/          # Flask server with /api/ask route
├── frontend/         # React widget (chat interface)
├── embed-script/     # (optional) embeddable <script> loader
├── deploy/           # render.yaml / vercel.json files
└── README.md

# Tech Stack:
Frontend  : React
Backend   : Flask + Python
AI Model  : Groq API (Mixtral, LLaMA 3)
Data      : JSON (MVP), SQLite/Firebase (planned)
Hosting   : Vercel (frontend), Render (backend)

Getting Started:
1. Clone the Repo
   git clone https://github.com/yourname/b2bsaasai
   cd b2bsaasai

2. Setup Backend
   - Create .env file with GROQ_API_KEY
   - Run:  pip install -r requirements.txt
   - Run backend: python app.py

3. Setup Frontend
   - cd frontend
   - Create .env file with REACT_APP_BACKEND_URL
   - Run: npm install && npm start

You're now ready to build your SaaS AI Copilot MVP! 
