from tkinter import *

root=Tk()
#Override settings
root.configure(bg="black")
root.geometry('480x640')
root.title("Minesweeper")
root.resizable(False,False)


topFrame=Frame(
    root,
    bg="white",
    width=480,
    height=64
    )
topFrame.place(x=0,y=0)




root.mainloop()
1234567