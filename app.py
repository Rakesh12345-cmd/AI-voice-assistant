from flask import Flask, request, jsonify, render_template
from main import get_assistant_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("text", "")
    
    response = get_assistant_response(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)