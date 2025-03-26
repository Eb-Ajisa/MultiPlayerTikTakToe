from socket import *
from time import sleep
import tkinter
import tkinter.scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import threading
import pickle

#Socket Configuration
hostname = gethostname()
ip_address = gethostbyname(hostname)
ip_address = str(ip_address)

serverName = ip_address # server IP
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

game = True

#Execute functions mainly start the mainloop for the gui
def func(gm):
    exec(gm)

#Game initalization
sentence = input('Press 1 to start game: ')

#Error Handling
if sentence != '1':
      game = False
      print("Incorrect value, closing connection")
      clientSocket.shutdown(SHUT_RDWR)
      clientSocket.close()

#Game/SocketLoop
while game == True:

    clientSocket.send(sentence.encode())
    gm = clientSocket.recv(4096).decode()

    #Send the create_game() function to the thread
    tiktaktoe = threading.Thread(target=func, args=(gm,))
    tiktaktoe.start()
    tiktaktoe.join()
    again = input("Go again?(Press 1 to go again): ")
    if again != '1':
        game = False
        clientSocket.shutdown(SHUT_RDWR)
        clientSocket.close()
        break




