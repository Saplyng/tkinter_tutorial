# message boxes, title, NOT MAKE IT SMALL

from tkinter import *
import tkinter.messagebox as tkm

main = Tk()
main.geometry('800x800')
main.title("Our Humble Project")

tkm.showinfo("Title Area", "This is a message.")



main.mainloop()
