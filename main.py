import tkinter as tk
from flashcard import load_flashcards, save_flashcards
flashcards = load_flashcards()

window = tk.Tk()
window.title("flashcard")
window.geometry("500x600")
window.config(padx=20, pady=20, bg="#f4f4f4")

main_frame = tk.Frame(window)
main_frame.pack(fill=tk.BOTH, expand=True)

card_window = tk.Frame(window)
card_window.pack_forget()

message_frame = tk.Frame(main_frame)
message_frame.pack(fill=tk.X)

current_card = [0]
showing_answer = [True]

message = tk.Label(message_frame, text="", font=("Arial", 24, "bold"))
message.pack(pady=(20, 0))

input_frame = tk.Frame(main_frame)
input_frame.pack(pady=20)

tk.Label(input_frame, text="Question:", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=5)
input_entry = tk.Entry(input_frame, font=("Arial", 14), width=30)
input_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Answer:", font=("Arial", 14)).grid(row=1, column=0, sticky="w", pady=5)
answer_entry = tk.Entry(input_frame, font=("Arial", 14), width=30)
answer_entry.grid(row=1, column=1, pady=5)


if flashcards:
    message.config(text=(flashcards[current_card[0]]["definition"]))
else:
    message.config(text="No flashcards available.")

def show_message():
    if not showing_answer[0]:
        if flashcards:
            message.config(text=(flashcards[current_card[0]]["definition"]))
        else:
            message.config(text="No flashcards available.")
    else:
        if flashcards:
            message.config(text=flashcards[current_card[0]]["answer"])
        else:
            message.config(text="No Answer available.")

def add_flashcard():
    text = input_entry.get().strip()
    answer_text = answer_entry.get().strip()
    if text:
        if answer_text:
            flashcards.append({"definition": text, "answer": answer_text})
            save_flashcards(flashcards)
            input_entry.delete(0, tk.END)
            answer_entry.delete(0, tk.END)
            if showing_answer[0] == True:
                turn_card()
            current_card[0] = len(flashcards) - 1
            show_message()

def delete_card():
    if flashcards:
        del flashcards[current_card[0]]
        save_flashcards(flashcards)
        if current_card[0] >= len(flashcards):
            current_card[0] = max(0, len(flashcards) - 1)
        show_message()

def turn_card():
    showing_answer[0] = not showing_answer[0]
    show_message()

def next_message():
    if flashcards:
        current_card[0] = (current_card[0] + 1) % len(flashcards)
        if showing_answer[0] == True:
            turn_card()
        show_message()

def previous_message():
    if flashcards:
        current_card[0] = (current_card[0] - 1) % len(flashcards)
        if showing_answer[0] == True:
            turn_card()
        show_message()

navigation_frame = tk.Frame(main_frame)
navigation_frame.pack(pady=(200, 0))

button_prev = tk.Button(navigation_frame, text="Back", command=previous_message)
button_prev.pack(side=tk.LEFT, padx=20, expand=True)

button_next = tk.Button(navigation_frame, text="Next", command=next_message)
button_next.pack(side=tk.LEFT, padx=20, expand=True)

control_frame = tk.Frame(main_frame)
control_frame.pack(pady=(20, 0))

button_add = tk.Button(control_frame, text="Add", command=add_flashcard)
button_add.grid(row=0, column=0, padx=10)

button_delete = tk.Button(control_frame, text="Delete", command=delete_card)
button_delete.grid(row=0, column=1, padx=10)

button_turn = tk.Button(control_frame, text="Turn", command=turn_card)
button_turn.grid(row=0, column=2, padx=10)

def go_back_to_main():
    card_window.pack_forget()
    main_frame.pack(fill="both", expand=True)
    window.update_idletasks()

def delete_specific_card(index):
    if 0 <= index < len(flashcards):
        del flashcards[index]
        save_flashcards(flashcards)
        show_cards() 

def edit_specific_card(index):
    if 0 <= index < len(flashcards):
        input_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)
        input_entry.insert(0, flashcards[index]["definition"])
        answer_entry.insert(0, flashcards[index]["answer"])
        
        del flashcards[index]
        save_flashcards(flashcards)
        go_back_to_main()


def show_cards():
    main_frame.pack_forget()
    card_window.pack(fill="both", expand=True)
    window.update_idletasks()

    for widget in card_window.winfo_children():
        widget.destroy()

    back_button = tk.Button(card_window, text="Back to Main", command=go_back_to_main)
    back_button.pack(pady=10)

    canvas = tk.Canvas(card_window)
    scrollbar = tk.Scrollbar(card_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not flashcards:
        label = tk.Label(scrollable_frame, text="No flashcards available.", font=("Arial", 12))
        label.pack(padx=10, pady=5)
        return

    for index, card in enumerate(flashcards):
        question_text = f"{index + 1}. Q: {card['definition']}\n   A: {card['answer']}"
        
        label = tk.Label(scrollable_frame, text=question_text, anchor="w", font=("Arial", 12),bg="#000000" ,justify="left", wraplength=300)
        label.grid(row=index, column=0, sticky="w", padx=10, pady=5)

        btn_frame = tk.Frame(scrollable_frame)
        btn_frame.grid(row=index, column=1, sticky="e", padx=10, pady=5)

        edit_btn = tk.Button(btn_frame, text="Edit", command=lambda i=index: edit_specific_card(i))
        edit_btn.pack(side="top", pady=2)

        delete_btn = tk.Button(btn_frame, text="Delete", command=lambda i=index: delete_specific_card(i))
        delete_btn.pack(side="top", pady=2)


button_show_all = tk.Button(control_frame, text="View All", command=show_cards)
button_show_all.grid(row=0, column=3, padx=5)


window.mainloop()
