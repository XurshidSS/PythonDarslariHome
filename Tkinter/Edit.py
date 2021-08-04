import tkinter as tk
window = tk.Tk()
window.geometry('1200x700')

label = tk.Label(text="Name")
entry = tk.Entry()

label.pack()
entry.pack()
window.mainloop()