from socket import *
from time import sleep
import tkinter
import tkinter.scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import threading
import pickle

#Initialize
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

import tkinter as tk
import threading

#Data that will be sent to socket/client to create a ui
cc =  '''
def create_game():
    def close_window():
        window.quit()
        window.destroy()
    #Create window
    window = tk.Tk()
    #Title for TikTacToe
    window.title("Tic Tac Toe")

    #Window size
    window.geometry("500x500")
    
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()

    button = tk.Button(window, text="close", fg="red",font=("Arial", 16), command=close_window)
    button.place(x=200, y=400)
    window.mainloop()
create_game()
        '''

#PL1 Create game func
def create_game():
    def close_window():
        window.quit()
        window.destroy()
    #Create window
    window = tk.Tk()
    #Title for TikTacToe
    window.title("Tic Tac Toe")

    #Window size
    window.geometry("500x500")
    
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()

    button = tk.Button(window, text="close", fg="red",font=("Arial", 16), command=close_window)
    button.place(x=200, y=400)
    window.mainloop()



print('Waiting for player 2')
game = True

#Start game
while game == True:
    connectionSocket, addr = serverSocket.accept()
    gamestart = connectionSocket.recv(1024).decode()

    #Error handling
    if gamestart == '1':
        print('Game started')
        connectionSocket.sendall(cc.encode())
        print("Sent to player 2")
        #Start game
        gap = threading.Thread(target=create_game)
        gap.start()   
        gap.join()
    else:
        print('Game not started due to another value, Closing connection')
        sleep(1)
        game = False
        connectionSocket.shutdown(SHUT_RDWR)
        connectionSocket.close()
        
        break
