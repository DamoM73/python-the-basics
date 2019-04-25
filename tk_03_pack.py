# example program for the pack geometry manager
from tkinter import *

# **** Create window
root = Tk()
root.geometry("300x200")
root.title("Tkinter pack example")

# **** Add window content ****
label_one = Label(root, text="One", bg="blue", fg="white")
label_one.pack(fill=BOTH, side=TOP)

label_two = Label(root, text="Two", bg="yellow")
label_two.pack(fill=BOTH, side=LEFT)

label_three = Label(root, text="Three", bg="red")
label_three.pack(fill=BOTH, side=LEFT)

label_four = Label(root, text="Four", bg="green")
label_four.pack(fill=BOTH, side = LEFT)

label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.pack(fill=BOTH, side=BOTTOM)

# **** Run window loop ****
root.mainloop()
