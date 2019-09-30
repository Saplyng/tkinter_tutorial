# button interaction
from tkinter import *

main = Tk()


def callMe(arg):
    print(arg)
    print("thank you")


btn1 = Button(main,text="Click Me", command=lambda: callMe("hello"))
btn1.pack()



main.mainloop()
