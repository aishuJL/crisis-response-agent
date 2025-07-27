import json
import os

HISTORY_FILE = "data/history.json"

def save_to_memory(user_input, agent_response):
    os.makedirs("data", exist_ok=True)
    history = load_history()
    history.append({"user": user_input, "agent": agent_response})
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)
