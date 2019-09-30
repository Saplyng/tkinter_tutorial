# menu, toolbar
from tkinter import *

def doNothing():
    print("ok ok")


main = Tk()


# Main Menu

menu = Menu(main)
main.config(menu=menu)

subMenu = Menu(main)
menu.add_cascade(label="File", menu=subMenu)
subMenu = Menu(menu, tearoff=0)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_command(label="Open", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(main)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu = Menu(menu, tearoff=0)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)

# Toolbar
toolbar = Frame(main,bg="gray")
btnCut = Button(toolbar, text="Cut", command=doNothing)
btnCut.pack(side=LEFT, padx=2, pady=2)

btnPrint = Button(toolbar, text="Print", command=doNothing)
btnPrint.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

main.mainloop()