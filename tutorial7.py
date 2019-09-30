# tkinter in a class
from tkinter import *


class ButtonButton1:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.btnPrint = Button(frame, text="click me now!", command=self.printIt)
        self.btnPrint.pack(side=LEFT)

        self.btnQuit = Button(frame, text="quit", command=frame.quit)
        self.btnQuit.pack(side=LEFT)

    def printIt(self):
        print("hello All")


main = Tk()

b = ButtonButton1(main)


main.mainloop()