from socket import *
from time import sleep
import tkinter as tk
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
'''
root = tk.Tk()
def close_window():
    root.quit()
    root.destroy()
    print('Window closed')
#Title for TikTacToe
root.title("Tic Tac Toe")
#Window size
root.geometry("500x500")

#declare the name
label = tk.Label(root, text="Tic Tac Toe")
label.pack()
button = tk.Button(root, text="close", fg="red",font=("Arial", 16), command=close_window)
button.place(x=200, y=400)
root.mainloop()
'''
game = True

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
    topleft = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    topleft.place(x=100, y=100)
    topcenter = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    topcenter.place(x=350, y=100)
    topright = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    topright.place(x=550, y=100)

    #Middle row 2
    midleft = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    midleft.place(x=100, y=350)    
    midcenter = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    midcenter.place(x=350, y=350)
    midright = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    midright.place(x=550, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    botleft.place(x=100, y=600)
    botcenter = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    botcenter.place(x=350, y=600)
    botright = tk.Button(window, text="Go Here!", fg="red",font=("Arial", 16), command=close_window)
    botright.place(x=650, y=600)

    window.mainloop()

#Useless for now
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

    p2game = threading.Thread(target=create_game)
    p2game.start()
    p2game.join()

    again = input("Go again?(Press 1 to go again): ")
    if again != '1':
        game = False
        clientSocket.shutdown(SHUT_RDWR)
        clientSocket.close()
        break



