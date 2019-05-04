'''Example of creating widgets without assigning vairables'''
from tkinter import *


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter frames example")


# **** Add window content ****
# add content to top section
Label(root, text="One", bg="blue", fg="white").pack(fill=BOTH, expand=TRUE)

# create middle frame and add content
middle_frame = Frame(root)
middle_frame.pack(fill=BOTH, expand=TRUE)

Label(middle_frame, text="Two", bg="yellow").pack(fill=BOTH, expand=TRUE, side=LEFT)
Label(middle_frame, text="Three", bg="red").pack(fill=BOTH, expand=TRUE, side=LEFT)
Label(middle_frame, text="Four", bg="green").pack(fill=BOTH, expand=TRUE, side = LEFT)

# add content to the bottom section
Label(root, text="Five", bg="purple", fg="white").pack(fill=BOTH, expand=TRUE)


# **** Run window loop ****
root.mainloop()
