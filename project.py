import tkinter as tk
window = tk.Tk()
window.title("hello")
window.geometry("500x600")
window.config(padx=20, pady=20, bg="#f4f4f4")

main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

message_frame = tk.Frame(main_frame)
message_frame.pack(fill=tk.X)
current_card = [0]
flashcards =[
    {"type": "Fruits", "definition": "Apple", "difficulty": "Easy"},
    {"type": "Fruits", "definition": "Pear", "difficulty": "Easy"}
]

# input = tk.Lable(main_frame, font=("Arial", 14, "bold"),) доделать input

message = tk.Label(main_frame, font=("Arial", 14, "bold"), text=(flashcards[current_card[0]]["definition"]))
message.pack(pady=(60, 0))
def next_message():
    current_card[0] = (current_card[0] + 1) % len(flashcards)
def change_message():
    message.config(text=(flashcards[current_card[0]]["definition"]))

button_frame = tk.Frame(main_frame)
button_frame.pack(fill=tk.X)

button = tk.Button(button_frame, text="Click me", command=lambda: [next_message(), change_message()])
button.grid(row=0, column=0, padx=75, pady=(320, 0))
def previous_message():
    current_card[0] = (current_card[0] - 1) % len(flashcards)
def clear_message():
    message.config(text=(flashcards[current_card[0]]["definition"]))

button_dest = tk.Button(button_frame, text="Change", command=lambda: [previous_message(), clear_message()])
button_dest.grid(row=0, column=1, padx=50, pady=(320, 0))

window.mainloop()