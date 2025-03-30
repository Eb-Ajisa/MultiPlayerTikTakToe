from socket import *
from time import sleep
import tkinter.scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import threading
from PIL import Image, ImageTk
import pickle

hostname = gethostname()
ip_address = gethostbyname(hostname)
ip_address = str(ip_address)
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
    def replacebut(widget,x,y):
        widget.destroy()
        Rec = canvas.create_rectangle(x + 15, y - 10, x+170, y+150, fill="", outline="black", width=5)
       
    def send_msg(butt,x,y):
        
        c = butt.cget('text')
        butt.destroy()
        turn.config(text="Its Opponents turn!")
        circle = canvas.create_oval(x, y - 10, x+170, y+150, fill="", outline="black", width=5)
        updated = {'butt': c, 'x': x, 'y': y}
        connectionSocket.send(pickle.dumps(updated))
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state='disabled')
        turn.config(text="Its opponents turn!")
        g = threading.Thread(target=rec).start()

    def rec():
        msg = connectionSocket.recv(1024)
        #Its your turn now so change text and recieve message
        turn.config(text="Its your turn!")
        turn11 = pickle.loads(msg)

        print(turn11)
        for widget in window.winfo_children():

            if isinstance(widget, tk.Button):
                #Recieve the text based on any button clicked to find the right one
                widget.config(state='normal')
                widget.cget('text')
                #If recieved text == button text then replace
                if turn11.get('butt') == widget.cget('text'):
                    x = turn11.get('x')
                    y = turn11.get('y')
                    window.after(0, replacebut(widget,x,y))
        return None

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
    topcenter = tk.Button(window, text="  ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topcenter,295,100))
    topcenter.place(x=295, y=120)
    topright = tk.Button(window, text="   ",  width=17, height=6 ,font=("Arial", 16),command=lambda: send_msg(topright,540,100))
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
