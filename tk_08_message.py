'''example program for using tkinter's message widget'''
from tkinter import *


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter Message Example \nAllows for multiple lines")


# **** Add window content ****
Message(root, text="Mesages are just like labels, except their text can go over several lines.", width=150).pack()


# **** Run window loop ****
root.mainloop()
