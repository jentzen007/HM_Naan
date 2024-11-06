import os
import whisper

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set
if api_key is None:
    raise ValueError("API key not found. Make sure the OPENAI_API_KEY environment variable is set.")

# Load the Whisper model
model = whisper.load_model("base")

# Transcribe an audio file
result = model.transcribe("your_audio_file.mp3")
print(result["text"])
