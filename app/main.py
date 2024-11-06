# app/main.py
from flask import Flask, request, jsonify, render_template
from app.whisper_handler import handle_call
from app.context_manager import manage_context

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/call", methods=["POST"])
def call_handler():
    call_data = request.json.get("call_data", "")
    response, context = handle_call(call_data)
    response = manage_context(context, response)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
