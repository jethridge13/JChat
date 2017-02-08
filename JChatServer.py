import tkinter
from tkinter import *
import tkinter.scrolledtext as ST
import tkinter.messagebox as MB


DEFAULT_PORT = 9966


root = tkinter.Tk()
verbose = IntVar()


def kickUser():
    print("KICK")


def quitConfirm():
    confirm = MB.askquestion("Quit?", "Are you sure you want to quit?")
    if confirm == "yes":
        quitServer()


def quitServer():
    #TODO As program progresses, add additional shutdown logic.
    sys.exit()


def restartConfirm():
    print("Restart?")


def startServer():
    #TODO Start server

    start["text"] = "Restart Server"
    start.config(command = restartConfirm)


def toggleVerbose():
    print(verbose.get())


# GUI stuff
verboseToggle = Checkbutton(root, text = "Verbose Output", variable = verbose, onvalue = 1, offvalue = 0, height = 5,
                            command = toggleVerbose)
verboseToggle.grid(row = 0, column = 1)

kick = Button(root, text = "Kick User", command = kickUser)
kick.grid(row = 2, column = 1)

start = Button(root, text = "Start Server", command = startServer)
start.grid(row = 1, column = 1)

quit = Button(root, text = "Quit", command = quitConfirm)
quit.grid(row = 3, column = 1)

output = ST.ScrolledText(root)
output.grid(row = 0, column = 0)

root.mainloop()