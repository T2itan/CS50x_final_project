import tkinter as tk

window = tk.Tk()
window.title("Sanity Check")
window.geometry("500x300")
window.configure(bg="white")

message = tk.Label(
    master=window,
    text="HELLO, ALEX! 🧠🔥",
    font=("Helvetica", 24, "bold"),
    bg="white",
    fg="black"
)
message.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
