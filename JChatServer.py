import tkinter
from tkinter import *
import tkinter.scrolledtext as ST

root = tkinter.Tk()
verbose = IntVar()

def kickUser():
    print("KICK")

def quitConfirm():
    print("Quit?")

def restartConfirm():
    print("Restart?")

def toggleVerbose():
    print(verbose.get())

# GUI stuff
verboseToggle = Checkbutton(root, text = "Verbose Output", variable = verbose, onvalue = 1, offvalue = 0, height = 5,
                            command = toggleVerbose)
verboseToggle.grid(row = 0, column = 1)

kick = Button(root, text = "Kick User", command = kickUser)
kick.grid(row = 1, column = 1)

restart = Button(root, text = "Restart Server", command = restartConfirm)
restart.grid(row = 2, column = 1)

quit = Button(root, text = "Quit", command = quitConfirm)
quit.grid(row = 3, column = 1)

output = ST.ScrolledText(root)
output.grid(row = 0, column = 0)

root.mainloop()