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

#Create window thread
def create_game(connectionSocket):
    window = tk.Tk()
    window.title("Tic Tac Toe")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    #Close window function
    def close_window():
        window.quit()
        window.destroy()
        print('Window closed')

    #Send updated ui to client and disable all buttons bec it is not
    #Our turn after we had clicked a button
    def send_msg(butt,x,y):
        c = butt.cget('text')
        butt.destroy()
        turn.config(text="Its Opponents turn!")
        ll = tk.Label(window, text="Go here", font=("Arial", 20))
        ll.place(x=x, y=y)
        updated = {'butt' : c, 'x' : x, 'y' : y}
        connectionSocket.send(pickle.dumps(updated))
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state='disabled')
        turn.config(text="Its opponents turn!")

    #Window size
    window.geometry("800x800")
    canvas = tk.Canvas(window, width=800, height=800)
    canvas.place(x=0, y=50)
    canvas.create_line(280, 70, 280, 800, fill="black", width = 5)
    canvas.create_line(525, 70, 525, 800, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 500, 760, 500, fill="black", width = 5)
    
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()

    #Turn variable
    turn = tk.Label(window, text="Its your turn!", font=("Arial", 20))
    turn.pack()
    
    #Row 1
    topleft = tk.Button(window, text=" ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topleft,50,100))
    topleft.place(x=50, y=120)
    topcenter = tk.Button(window, text="  ",  width=17, height=6 ,font=("Arial", 16))
    topcenter.place(x=295, y=120)
    topright = tk.Button(window, text="   ",  width=17, height=6 ,font=("Arial", 16))
    topright.place(x=540, y=120)
    #Middle row 2
    midleft = tk.Button(window, text="    ",  width=17, height=6 ,font=("Arial", 16))
    midleft.place(x=50, y=350)    
    midcenter = tk.Button(window, text="     ",  width=17, height=6 ,font=("Arial", 16))
    midcenter.place(x=295, y=350)
    midright = tk.Button(window, text="      ",  width=17, height=6 ,font=("Arial", 16))
    midright.place(x=540, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="       ",  width=17, height=6 ,font=("Arial", 16))
    botleft.place(x=50, y=600)
    botcenter = tk.Button(window, text="        ",  width=17, height=6 ,font=("Arial", 16))
    botcenter.place(x=295, y=600)
    botright = tk.Button(window, text="         ",  width=17, height=6 ,font=("Arial", 16))
    botright.place(x=540, y=600)
    #turn.config(text=f"Value: {data.get('value', 0)}")
    
    

    window.mainloop()
        

print('Waiting for player 2')
game = True
while game == True:
    connectionSocket, addr = serverSocket.accept()
    gamestart = connectionSocket.recv(1024).decode()
    if gamestart == '1':
        print('Game started')
        print("Sent to player 2")

        #For structure we do this in a thread
        gap = threading.Thread(target=create_game, args=(connectionSocket,))
        gap.start()   
        gap.join()


    else:
        print('Game not started due to another value, Closing connection')
        sleep(1)
        game = False
        connectionSocket.shutdown(SHUT_RDWR)
        connectionSocket.close()
