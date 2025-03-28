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

def create_game(clientSocket):
    #Create window
    window = tk.Tk()
    #Title for TikTacToe
    window.title("Tic Tac Toe")

    frame = tk.Frame(window)
    frame.pack()
    def close_window():
        window.quit()
        window.destroy()
        print('Window closed')
    
    def replacebut(widget,x,y):
        widget.destroy()
        label2 = tk.Label(window, text="GG")
        label2.place(x=x, y=y)


    #Window size
    window.geometry("800x800")
    canvas = tk.Canvas(window, width=800, height=800)
    canvas.place(x=0, y=50)
    canvas.create_line(280, 70, 280, 800, fill="black", width = 5)
    canvas.create_line(525, 70, 525, 800, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 500, 760, 500, fill="black", width = 5)

    turn = tk.Label(window, text="Its oppobnents turn", font=("Arial", 20))
    turn.pack()
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()
    
    #Row 1
    topleft = tk.Button(window, text=" ",  width=17, height=6 ,font=("Arial", 16))
    topleft.place(x=50, y=120)
    topcenter = tk.Button(window, text="  ",  width=17, height=6 ,font=("Arial", 16))
    topcenter.place(x=295, y=120)
    topright = tk.Button(window, text="   ",  width=17, height=6 ,font=("Arial", 16))
    topright.place(x=540, y=120)

    #Middle row 2
    midleft = tk.Button(window, text="    ",  width=17, height=6 ,font=("Arial", 16))
    midleft.place(x=50, y=350)    
    midcenter = tk.Button(window, text="     ",  width=17, height=6 ,font=("Arial", 16))
    midcenter.place(x=290, y=350)
    midright = tk.Button(window, text="      ",  width=17, height=6 ,font=("Arial", 16))
    midright.place(x=540, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="       ",  width=17, height=6 ,font=("Arial", 16))
    botleft.place(x=50, y=600)
    botcenter = tk.Button(window, text="        ",  width=17, height=6 ,font=("Arial", 16))
    botcenter.place(x=290, y=600)
    botright = tk.Button(window, text="         ",  width=17, height=6 ,font=("Arial", 16))
    botright.place(x=540, y=600)

    #Recieve (Will use semaphore to allow for automation)
    def rec():
        msg = clientSocket.recv(1024)
        #Its your turn now so change text and recieve message
        turn.config(text="Its your turn!")
        turn11 = pickle.loads(msg)

        print(turn11)
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                #Recieve the text based on any button clicked to find the right one
                widget.cget('text')
                #If recieved text == button text then replace
                if turn11.get('butt') == widget.cget('text'):
                    x = turn11.get('x')
                    y = turn11.get('y')
                    window.after(0, replacebut(widget,x,y))
        return None


    g= threading.Thread(target=rec).start()


    window.mainloop()

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

    p2game = threading.Thread(target=create_game, args=(clientSocket,))
    p2game.start()
    p2game.join()

    again = input("Go again?(Press 1 to go again): ")
    if again != '1':
        game = False
        clientSocket.shutdown(SHUT_RDWR)
        clientSocket.close()
        break
