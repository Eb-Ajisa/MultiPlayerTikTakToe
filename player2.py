from socket import *
import tkinter as tk
import tkinter.scrolledtext
from tkinter import simpledialog
import pickle
import threading
hostname = gethostname()
ip_address = gethostbyname(hostname)
ip_address = str(ip_address)

serverName = ip_address # server IP
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

game = True


while game == True:
    sentence = input('Press 1 to start game: ')
    clientSocket.send(sentence.encode())
    
    gamestart = clientSocket.recv(4096).decode()
    exec(gamestart)

    input("Press Enter to continue...")



