# grid and entry

from tkinter import *

main = Tk()

label1 = Label(main,text="name")
label2 = Label(main,text="password")
entry1 = Entry(main)
entry2 = Entry(main)
c = Checkbutton(main, text="keep me logged in")


label1.grid(row=0, column=0, stick=E) # compass rose NESW
label2.grid(row=1, column=0, stick=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
c.grid(row=3, column=0, columnspan=2)


main.mainloop()