# app/whisper_handler.py
import requests
from app.config import OPENAI_API_KEY

def handle_call(call_data):
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    response = requests.post(
        "https://api.openai.com/v1/engines/whisper-calls/transcriptions",
        headers=headers,
        json={"input": call_data}
    )
    if response.status_code == 200:
        return response.json().get("text", ""), {"context": call_data}
    return "Sorry, I'm unable to process your request.", None
