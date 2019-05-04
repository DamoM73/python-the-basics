'''example of how to use the tkinter button widget'''
from tkinter import *


# **** Functions ****
def say_hello():
    display_lbl.config(text="Hello")


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Button Example")


# **** Add content to window ****
Button(root, text="Click to say hello", command=say_hello).pack()

display_lbl = Label(root)
display_lbl.pack()

# **** Run window loop ****
root.mainloop()
