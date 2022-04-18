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
    height=640
    )
topFrame.place(x=0,y=0)




root.mainloop()