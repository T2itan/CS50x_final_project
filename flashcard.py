import json
import os

FILENAME = "flashcards.json"

def load_flashcards():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    else:
        return []
    
def save_flashcards(flashcards):
    with open(FILENAME, "w") as file:
        json.dump(flashcards, file)


