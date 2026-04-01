from flask import Flask, request, jsonify, render_template
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/challenge", methods=["POST"])
def challenge():
    data = request.get_json()
    theme = data.get("theme", "")
    pieces = data.get("pieces", "")
    age = data.get("age", "")

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"You are a fun and enthusiastic Lego building coach. Generate a creative Lego building challenge for someone who is {age} years old, has approximately {pieces} pieces available, and wants to build something with a {theme} theme. Include a fun challenge name, a description, step by step building tips, and a fun fact about the theme. Keep it exciting and encouraging!"
            }
        ]
    )

    return jsonify({"result": message.content[0].text})

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    interests = data.get("interests", "")

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"You are a Lego expert and enthusiast. Based on these interests: {interests}, recommend 3 official Lego sets the person would love. For each set include the set name, set number, a description of why it matches their interests, approximate price range, and difficulty level. Make it fun and enthusiastic!"
            }
        ]
    )

    return jsonify({"result": message.content[0].text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)