# icons and photos

from tkinter import *

main = Tk()

iCopy = PhotoImage(file="duality.png")
pCopy = iCopy.subsample(50,50)

btn1 = Button(main, text="Copy", image=pCopy).pack()


main.mainloop()