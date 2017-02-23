from socket import *

CONNECT_ATTEMPTS = 3

host = input("Host: ")
host = host.lower()
port = input("Port: ")
port = int(port)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(3)
print("Attempting to connect to " + str(host) + ":" + str(port))
i = 1
connect = False
while not connect:
    if i > CONNECT_ATTEMPTS:
        print("Connection aborted. Exiting program.")
        sys.exit()
    try:
        if i != 1:
            print("Attempting to connect. Attempt " + str(i) + " of " + str(CONNECT_ATTEMPTS))
        clientSocket.connect((host, port))
        connect = True
    except OSError:
        print("Connection refused")
        i += 1
print("Connection successful!")