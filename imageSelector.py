import tkinter
from tkinter import Tk, Label
from PIL import Image, ImageTk
from tkinter import filedialog, Tk

root = Tk()

file_path = filedialog.askopenfilename(
    filetypes=[
        ("Images", "*.png *.jpg *.jpeg")
        ]    
        )
img = Image.open(file_path)
photo = ImageTk.PhotoImage(img)
label = Label(root, image=photo).pack()

root.mainloop()
