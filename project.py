import tkinter as tk
from flashcard import load_flashcards, save_flashcards
flashcards = load_flashcards()


window = tk.Tk()
window.title("hello")
window.geometry("500x600")
window.config(padx=20, pady=20, bg="#f4f4f4")

main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

message_frame = tk.Frame(main_frame)
message_frame.pack(fill=tk.X)
current_card = [0]

message = tk.Label(message_frame, text="", font=("Arial", 24, "bold"))
message.pack(pady=(20, 0))

input_entry = tk.Entry(main_frame, font=("Arial", 14, "bold"))
input_entry.pack(pady=(20, 0))
if flashcards:
    message.config(text=(flashcards[current_card[0]]["definition"]))
else:
    message.config(text="No flashcards available.")

def show_message():
    if flashcards:
        message.config(text=(flashcards[current_card[0]]["definition"]))
    else:
        message.config(text="No flashcards available.")

def add_flashcard():
    text = input_entry.get().strip()
    if text:
        flashcards.append({"definition": text})
        save_flashcards(flashcards)
        input_entry.delete(0, tk.END)
        current_card[0] = len(flashcards) - 1
        show_message()

def delete_card():
    if flashcards:
        del flashcards[current_card[0]]
        save_flashcards(flashcards)

        if current_card[0] >= len(flashcards):
            current_card[0] = max(0, len(flashcards) - 1)
        
        show_message()

def next_message():
    if flashcards:
        current_card[0] = (current_card[0] + 1) % len(flashcards)
        show_message()

def previous_message():
    if flashcards:
        current_card[0] = (current_card[0] - 1) % len(flashcards)
        show_message()

button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X)

button_next = tk.Button(button_frame, text="Next", command=lambda: [next_message()])
button_next.grid(row=0, column=0, padx=(140, 25), pady=(320, 0))

button_prev = tk.Button(button_frame, text="Back", command=lambda: [previous_message()])
button_prev.grid(row=0, column=1, padx=(20, 25), pady=(320, 0))

button_add = tk.Button(button_frame, text="Add", command=add_flashcard)
button_add.grid(row=1, column=0, padx=(140, 25), pady=(32, 0))

button_delete = tk.Button(button_frame, text="delete", command=delete_card)
button_delete.grid(row=1, column=1, padx=(20, 25), pady=(32, 0))

window.mainloop()
