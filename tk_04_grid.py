# example program for the grid geometry manager
from tkinter import *

# **** Create window
root = Tk()
root.geometry("300x200")
root.title("Tkinter grid example")

# **** Add window content ****
label_one = Label(root, text="One", bg="blue", fg="white")
label_one.grid(row=0,column=0, columnspan=3)

label_two = Label(root, text="Two", bg="yellow")
label_two.grid(row=1,column=0)

label_three = Label(root, text="Three", bg="red")
label_three.grid(row=1,column=1)

label_four = Label(root, text="Four", bg="green")
label_four.grid(row=1,column=2, rowspan=2)

label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.grid(row=2,column=0, columnspan=2)

# **** Run window loop ****
root.mainloop()
