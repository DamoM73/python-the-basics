'''example program for the frame containers'''
from tkinter import *


# **** Create window ****
root = Tk()
root.geometry("300x200")
root.title("Tkinter frames example")


# **** Add window content ****
# add content to top section
label_one = Label(root, text="One", bg="blue", fg="white")
label_one.pack(fill=BOTH, expand=TRUE)

# create middle frame and add content
middle_frame = Frame(root)
middle_frame.pack(fill=BOTH, expand=TRUE)

label_two = Label(middle_frame, text="Two", bg="yellow")
label_two.pack(fill=BOTH, expand=TRUE, side=LEFT)

label_three = Label(middle_frame, text="Three", bg="red")
label_three.pack(fill=BOTH, expand=TRUE, side=LEFT)

label_four = Label(middle_frame, text="Four", bg="green")
label_four.pack(fill=BOTH, expand=TRUE, side = LEFT)

# add content to the bottom section
label_five = Label(root, text="Five", bg="purple", fg="white")
label_five.pack(fill=BOTH, expand=TRUE)


# **** Run window loop ****
root.mainloop()
