# Flashcard App

A simple yet functional flashcard application built using Python and Tkinter. This GUI-based tool allows users to create, view, delete, and manage flashcards with persistent storage in JSON format. Ideal for language learners, programmers, or anyone needing spaced repetition for memorization.

---

## Features

- Add and store custom flashcards (question-answer pairs)
- Flip between questions and answers
- Navigate to next/previous card
- Delete the current flashcard
- Scrollable list view of all cards
- Persistent JSON storage (`flashcards.json`)
- Lightweight, no external libraries

---

## File Structure

```
flashcard-app/
├── flashcard.py        # JSON read/write functions
├── main.py             # Main application with GUI logic
├── flashcards.json     # Flashcard data (auto-generated)
└── README.md           # Project documentation
```

---

## File Descriptions

### `main.py`
This is the application's entry point. It initializes the Tkinter window, sets up the interface, and manages interactions:
- `add_flashcard()` – Adds a new card from user input
- `turn_card()` – Flips between question and answer
- `next_message()` / `previous_message()` – Navigates through flashcards
- `delete_card()` – Removes the current card
- `show_cards()` – Opens a scrollable list of all cards
- `go_back_to_main()` – Returns to main card view

### `flashcard.py`
Contains:
```python
def load_flashcards():  # Loads JSON data into memory
def save_flashcards(data):  # Saves modified data back to JSON
```
Handles safe reading/writing of flashcard data.

### `flashcards.json`
Stores the flashcards in the format:
```json
[
  {
    "definition": "What is a dictionary in Python?",
    "answer": "A collection of key-value pairs."
  }
]
```
This file is created automatically on first use.

---

## Installation & Usage

### 1. Clone the repository:
```bash
git clone https://github.com/<your-username>/flashcard-app.git
cd flashcard-app
```

### 2. Run the app:
```bash
python main.py
```

### Requirements:
- Python 3.6 or newer
- No third-party libraries required (only `tkinter` and built-in `json`)

---

## Optional Git Setup

If you want to avoid committing your personal flashcards, add this to `.gitignore`:
```
flashcards.json
```

You can create `.gitignore` using:
```bash
echo "flashcards.json" >> .gitignore
```

To remove `flashcards.json` from tracking without deleting it locally:
```bash
git rm --cached flashcards.json
```

---

## Design Decisions

### Why `Tkinter`?
Tkinter is included with Python and is cross-platform, making it perfect for lightweight desktop tools.

### Why JSON for storage?
JSON offers human-readable structure and integrates seamlessly with Python's standard library.

### Modular structure:
Logic is separated (`flashcard.py`) from UI (`main.py`) to keep code maintainable and testable.

### Scrollable card view:
Implemented via `Canvas` + `Scrollbar` + `Frame` to ensure usability with large card sets.

---

## Suggested Demo Video Flow

**Duration**: ~2 minutes

**Script Outline**:
1. **Intro (10 sec)**: State app purpose: “a minimal flashcard app to memorize content.”
2. **Add cards (30 sec)**: Show entering Q&A, click 'Add', and verify it's saved.
3. **Navigation (20 sec)**: Show 'Next', 'Back', and 'Turn' features.
4. **Delete card (10 sec)**: Delete current card and confirm its removal.
5. **View All (20 sec)**: Click 'View All', scroll through the list, then return.
6. **Outro (10 sec)**: Mention local JSON storage and invite users to try it.

---

## License

MIT License. See `LICENSE` file for details.

---

## Contributions

Feel free to open issues or submit pull requests for improvements.

## Contact

For questions, suggestions, feel free to reach out via email: [alex.dmit03@gmail.com](mailto:alex.dmit03@gmail.com)
