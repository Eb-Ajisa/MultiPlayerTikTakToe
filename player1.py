from socket import *
from time import sleep
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
import threading
import pickle

serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

import tkinter as tk
import threading

cc =  '''
def create_game():
    #Create window
    window = tk.Tk()

    #Title for TikTacToe
    window.title("Tic Tac Toe")

    #Window size
    window.geometry("500x500")
    
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()
    window.mainloop()
create_game()
    '''
def create_game():
    #Create window
    window = tk.Tk()

    #Title for TikTacToe
    window.title("Tic Tac Toe")

    #Window size
    window.geometry("500x500")
    
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()
    window.mainloop()

print('Waiting for player 2')
game = True
while game == True:
    connectionSocket, addr = serverSocket.accept()
    gamestart = connectionSocket.recv(1024).decode()
    if gamestart == '1':
        print('Game started')
        connectionSocket.sendall(cc.encode())
        print("Sent to player 2")

        gap = threading.Thread(target=create_game)
        gap.start()
        gap.join()     
    else:
        print('Game not started Closing connection')
        sleep(1)
        game = False
        connectionSocket.shutdown(2)
        connectionSocket.close()
        
