import tkinter as tk
window = tk.Tk()
window.title("hello")
window.geometry("300x200")
window.config(padx=20, pady=20, bg="#f4f4f4")
tk.Button(window, text="Click me", command=lambda: print("hii")).pack()
window.mainloop()