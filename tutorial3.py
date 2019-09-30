# filling the screen

from tkinter import *

main = Tk()

one = Label(main, text="one", bg="red", fg="white")
one.pack()
two = Label(main, text="two", bg="blue", fg="white")
two.pack(fill=X)
three = Label(main, text="three", bg="black", fg="white")
three.pack(side=LEFT, fill=Y)


main.mainloop()
