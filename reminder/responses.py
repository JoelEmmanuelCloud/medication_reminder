import json
import re

RESPONSES_FILE = 'reminder/responses.json'

def load_responses():
    with open(RESPONSES_FILE, 'r') as file:
        return json.load(file)

def save_responses(responses):
    with open(RESPONSES_FILE, 'w') as file:
        json.dump(responses, file, indent=2)

def get_response(user_input):
    responses = load_responses()
    for entry in responses:
        if re.search(entry['pattern'], user_input, re.IGNORECASE):
            return entry['response']
    return "I'm sorry, I don't understand that."
