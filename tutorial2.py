# frames buttons and pack info
from tkinter import *

main = Tk()

topFrame = Frame(main)
topFrame.pack(side=TOP)

bottomFrame = Frame(main)
bottomFrame.pack(side=BOTTOM)


btnA = Button(topFrame, text="OK, btn1", fg="red", highlightbackground="black")
btnB = Button(topFrame, text="OK, btn2", fg="yellow")
btnC = Button(topFrame, text="OK, btn3", fg="green")
btnD = Button(bottomFrame, text="OK, btn4", fg="blue")

btnA.pack(side=LEFT)
btnB.pack(side=LEFT)
btnC.pack(side=LEFT)
btnD.pack()

main.mainloop()
