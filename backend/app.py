from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import json
import os

print("Starting Groq backend...")

load_dotenv()

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # ✅ Use Groq key from .env

# Load the feature data
with open("feature_data.json") as f:
    feature_data = json.load(f)

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.json
    page = data.get("page", "").strip()
    question = data.get("question", "").strip()

    if not page or not question:
        return jsonify({"error": "Missing page or question"}), 400

    feature = feature_data.get(page, {}).get("feature", "general SaaS feature")
    faqs = feature_data.get(page, {}).get("faqs", [])

    prompt = f"""
You are a helpful assistant for a B2B SaaS company.
User is currently on this page: {page}
Feature description: {feature}
FAQs:
{json.dumps(faqs, indent=2)}
User asked: "{question}"
Respond concisely and helpfully.
    """

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistral-saba-24b",  # Or "llama3-8b-8192"
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
    )

    if response.status_code != 200:
        return jsonify({
            "error": "Groq API error",
            "status_code": response.status_code,
            "details": response.text
        }), 500

    answer = response.json()["choices"][0]["message"]["content"]
    return jsonify({"answer": answer})


@app.route("/")
def home():
    return "✅ Groq backend is running!"

if __name__ == "__main__":
    app.run(debug=True)
