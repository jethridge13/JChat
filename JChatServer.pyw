import tkinter
import threading
from tkinter import *
from socket import *
import tkinter.scrolledtext as ST
import tkinter.messagebox as MB


DEFAULT_PORT = 9966

EOM = "\"\r\n\r\n\""


root = tkinter.Tk()
verbose = IntVar()
output = ST.ScrolledText(root)
users = ST.ScrolledText(root, height = 5)

outputLock = threading.Lock()
usersLock = threading.Lock()
threads = []


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


def sPrint(s):
    s += "\n"
    outputLock.acquire()
    output.configure(state="normal")
    output.insert(tkinter.END, s)
    output.configure(state="disabled")
    outputLock.release()

def vPrint(s):
    if verbose.get():
        outputLock.acquire()
        output.configure(state="normal")
        output.insert(tkinter.END, s)
        output.configure(state="disabled")
        outputLock.release()


def startServer():
    #TODO Start server
    # Prepare the socket
    serverPort = DEFAULT_PORT
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))

    sPrint("Starting server...")
    sPrint("Listening on port " + str(serverPort))
    start["text"] = "Restart Server"
    start.config(command = restartConfirm)


# *** THREAD STUFF ***
class ConnThread (threading.Thread):

    # This is the constructor for the thread.
    def __init__(self, threadID, socket, ip, port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.socket = socket
        self.ip = ip
        self.port = port
        self.identity = "Thread" + str(self.threadID) + "@" + str(self.ip) + ":" + str(self.port)
    #TODO More functionality here

class LoginThread(threading.Thread):

    def __init__(self, serverSocket):
        threading.Thread.__init__(self)
        self.serverSocket = serverSocket

    def run(self):
        print("Login Thread running")
        freeThreadID = 0
        runServer = True
        # Functionality loop
        while runServer:
            try:
                self.serverSocket.listen(1)
                # Connection received from client
                clientSocket, addr = self.serverSocket.accept()
                sPrint("Connection received from " + str(addr[0]) + ":" + str(addr[1]))
                thread = ConnThread(freeThreadID, clientSocket, addr[0], addr[1])
                freeThreadID += 1

                # Add the thread to the list of threads
                usersLock.acquire()
                threads.append(thread)
                usersLock.release()

                # Start the thread
                thread.start()
            except OSError:
                sPrint("The socket in the login thread has closed.")
                sPrint("If this was triggered by something other than a server shutdown, a critical error has occured.")
                runServer = False



# GUI stuff
verboseToggle = Checkbutton(root, text = "Verbose Output", variable = verbose, onvalue = 1, offvalue = 0, height = 5)
verboseToggle.grid(row = 0, column = 1)

kick = Button(root, text = "Kick User", command = kickUser)
kick.grid(row = 2, column = 1)

start = Button(root, text = "Start Server", command = startServer)
start.grid(row = 1, column = 1)

quit = Button(root, text = "Quit", command = quitConfirm)
quit.grid(row = 3, column = 1)

output.configure(state = "disabled")
output.grid(row = 0, column = 0)

users.configure(state = "disabled")
users.grid(row = 1, column = 0)

root.mainloop()