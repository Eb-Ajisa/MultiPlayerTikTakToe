from socket import *
from time import sleep
import tkinter.scrolledtext
from tkinter import messagebox
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


def create_game():
    def close_window():
        window.quit()
        window.destroy()
        print('Window closed')
    #Create window
    window = tk.Tk()
    #Title for TikTacToe
    window.title("Tic Tac Toe")

    #Window size
    window.geometry("800x800")
    
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()

    close_button = tk.Button(window, text="close", fg="red",font=("Arial", 16), command=close_window)
    close_button.place(x=400, y=750)
    
    #Row 1
    topleft = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    topleft.place(x=100, y=100)
    topcenter = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    topcenter.place(x=350, y=100)
    topright = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    topright.place(x=550, y=100)

    #Middle row 2
    midleft = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    midleft.place(x=100, y=350)    
    midcenter = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    midcenter.place(x=350, y=350)
    midright = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    midright.place(x=550, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    botleft.place(x=100, y=600)
    botcenter = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    botcenter.place(x=350, y=600)
    botright = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16))
    botright.place(x=650, y=600)

    window.mainloop()
        

print('Waiting for player 2')
game = True
while game == True:
    connectionSocket, addr = serverSocket.accept()
    gamestart = connectionSocket.recv(1024).decode()
    if gamestart == '1':
        print('Game started')
        print("Sent to player 2")

        gap = threading.Thread(target=create_game)
        gap.start()   
        gap.join()


    else:
        print('Game not started due to another value, Closing connection')
        sleep(1)
        game = False
        connectionSocket.shutdown(SHUT_RDWR)
        connectionSocket.close()
