# Flashcard App

## Overview

This project is a flashcard application built using Python's Tkinter library for the graphical user interface and JSON for persistent data storage. It is designed to help users create, manage, and review flashcards for study purposes. Each flashcard contains a question (referred to in the code as a "definition") and an answer. The interface allows for navigating between cards, flipping to view answers, adding new cards, deleting existing ones, and viewing all flashcards at once.

The application runs locally, stores flashcards in a JSON file on the user’s machine, and does not require an internet connection. It is a useful tool for language learning, memorization tasks, and general self-study.

#### VIDEO DEMO: https://youtu.be/4Xo5QtxUUJ0

## File Structure and Description

### `main.py`

This is the primary file that sets up and controls the graphical interface. It includes:

- Creation and configuration of the main window
- Frames for input, navigation, and flashcard display
- Functions for interacting with flashcards (add, delete, flip, navigate)
- Switching between the main flashcard view and a scrollable list of all cards
- Logic for managing application state

All the core user interactions are handled here through Tkinter’s widget system.

### `flashcard.py`

This module contains two functions:

- `load_flashcards()`: Reads the `flashcards.json` file and returns the flashcard data as a list of dictionaries. If the file does not exist, it returns an empty list.
- `save_flashcards(data)`: Takes the current list of flashcards and writes it back to the JSON file.

Keeping these functions separate improves modularity and makes the application easier to maintain.

### `flashcards.json`

This is the local storage file where flashcards are saved. Each entry in the file is a dictionary with two keys: `"definition"` and `"answer"`. This format keeps the structure simple and allows for easy expansion or editing.

Note: This file should be excluded from version control using `.gitignore` since it contains user-specific data.

## Key Features

- **Add Flashcards**: Users can create new flashcards by entering a question and an answer and clicking the "Add" button.
- **Delete Flashcards**: The currently viewed flashcard can be deleted, and the data is updated accordingly.
- **Navigation**: Users can move through flashcards using "Next" and "Back" buttons. Navigation is cyclic, so the last card wraps around to the first.
- **Flip Cards**: A "Turn" button allows toggling between the question and the answer.
- **View All Flashcards**: A scrollable view that lists all saved flashcards with buttons for future actions like editing or deleting.
- **Scrollable Interface**: The "View All" section supports scrolling in case of a large number of cards.
- **Layout Consistency**: Cards in the list view are arranged in a consistent grid layout for clarity.

## Design Considerations

### Data Storage

A JSON file was chosen over a database because the data structure is simple, flat, and does not require advanced querying or relationships. JSON is human-readable and easy to debug, which makes it suitable for beginner-friendly applications.

### UI Management

The interface is built entirely with Tkinter and follows a frame-based layout. The main screen and the "View All" screen are distinct, and the transition between them is handled using `.pack_forget()` and `.pack()` methods. To avoid performance issues or layout conflicts, the scrollable area in the "View All" screen uses a `Canvas` widget with a `Scrollbar`.

### Code Organization

Separating GUI logic (`main.py`) from data logic (`flashcard.py`) promotes cleaner architecture and makes it easier to update individual components in the future.

### Version Control and User Data

The `flashcards.json` file should be excluded from Git commits by adding it to `.gitignore`. This ensures that sensitive or user-specific content does not end up in the remote repository.

## Future Enhancements

Several potential improvements could be made to extend functionality:

- **Edit Flashcards**: Add the ability to modify the content of existing flashcards.
- **Search or Filter**: Allow users to search for specific flashcards or filter by keywords.
- **Categories or Tags**: Organize flashcards into groups for more structured study.
- **Export/Import Options**: Enable backup and restore using CSV or JSON formats.
- **Study Mode**: Add a feature for timed or randomized review sessions.
- **Improved Styling**: Enhance the interface aesthetics using themes or third-party styling libraries.

## Conclusion

This flashcard application demonstrates a complete workflow for managing study content with a graphical interface, persistent storage, and interactive controls. It is modular, extendable, and designed with clarity in mind. The application is especially suitable as a personal learning tool or as a project for Python learners who want to practice GUI development and file handling.


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
python3 main.py
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

## License

MIT License. See `LICENSE` file for details.

---

## Contributions

Feel free to open issues or submit pull requests for improvements.

## Contact

For questions, suggestions, feel free to reach out via email: [alex.dmit03@gmail.com](mailto:alex.dmit03@gmail.com)
