# example program for the label widget

from tkinter import *

# **** create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter label example")

# **** Add window content ****
example_label = Label(root, text="This is the example label")
example_label.pack()

Label(root, text="This is a second label").pack()


# **** Run window loop ****
root.mainloop()
