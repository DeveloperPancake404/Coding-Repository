import tkinter as tk
from tkinter import ttk
username_var = 0

def tab_one_button_clicked():
    print("Button on tab 1 clicked")

def tab_two_button_clicked():
    print("Button on tab 2 clicked")
window = tk.Tk()
window.title("Window Title")
window.geometry("400x300")

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

ttk.Label(tab1, text="This is tab one").pack()
tk.Entry(tab1, window, textvariable=username_var).pack()
ttk.Button(tab1, text="Click me", commsand=tab_one_button_clicked).pack()
ttk.Label(tab2, text="This is tab two").pack()
ttk.Button(tab2, text="Click me", command=tab_two_button_clicked).pack()

window.mainloop()
