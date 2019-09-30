# button interaction mouse parameters
from tkinter import *

main = Tk()


def callMe(event):
    print(event.num)
    print("thank you!")


btn1 = Button(main,text="Click Me")
btn1.bind("<Button-1>", callMe)
btn1.bind("<Button-2>", callMe)
btn1.bind("<Button-3>", callMe)
btn1.pack()



main.mainloop()
