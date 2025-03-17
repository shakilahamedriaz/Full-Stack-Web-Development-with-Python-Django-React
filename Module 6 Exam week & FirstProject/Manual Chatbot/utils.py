import json
import datetime

def load_responses():
    """Load chatbot responses from a JSON file."""
    try:
        with open("responses.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"default": "Sorry, I'm facing an issue loading responses."}

def log_conversation(user_input, bot_response):
    """Log chat history to a file with timestamps."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] User: {user_input} | Bot: {bot_response}\n"

    with open("conversation.log", "a") as file:
        file.write(log_entry)
