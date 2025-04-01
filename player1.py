from socket import *
from time import sleep
import tkinter.scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import threading
from PIL import Image, ImageTk
import pickle
import multiprocessing
#Winner 0: No winner yet
#Winner 1: Player 1 wins
#Winner 2: Player 2 wins
#Winner 3: Draw
winner = 0
answer = 0
print('Waiting for player 2 to connect')

#Database for player 1 (me) and player 2
mystuff = []
opponenetstuff = []
counter = 0
#Socket and imports 
hostname = gethostname()
ip_address = gethostbyname(hostname)
ip_address = str(ip_address)
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()

again = 0
import tkinter as tk
import threading
import random
def check_win(canvas, window):
    p = True
    global winner
    while p == True:
    #Check who wins for the firsrt row combination
        if " " in mystuff and "  " in mystuff and "   " in mystuff:
            winner = 2
            canvas.create_line(50,150, 800,150, fill="red", width = 5)
            p = False
        elif " "in opponenetstuff and "  " in opponenetstuff and "   " in opponenetstuff:
            winner = 1
            canvas.create_line(50,150, 800,150, fill="red", width = 5)
            p = False
        #Check who wins for the second row combination
        elif "    " in mystuff and "     " in mystuff and "      " in mystuff:
            winner = 2
            canvas.create_line(50,370, 800,370, fill="red", width = 5)
            p = False
        elif "    " in opponenetstuff and "     " in opponenetstuff and "      " in opponenetstuff:
            winner = 1
            canvas.create_line(50,370, 800,370, fill="red", width = 5)
            p = False
        #Check who wins for the third row combination
        elif "       " in mystuff and "        " in mystuff and "         " in mystuff:
            winner = 2
            canvas.create_line(50,610, 800,610, fill="red", width = 5)
            p = False
        elif "       " in opponenetstuff and "        " in opponenetstuff and "         " in opponenetstuff:
            winner = 1
            canvas.create_line(50,610, 800,610, fill="red", width = 5)
            p = False
#------------------------------------------------------------------------------------------------------
        #Check who wins for the first column combination
        elif " "in mystuff and "    " in mystuff and "       " in mystuff:
            winner = 2
            canvas.create_line(150,50, 150,800, fill="red", width = 5)
            p = False
        elif " " in opponenetstuff and "    " in opponenetstuff and "       " in opponenetstuff:
            winner = 1
            canvas.create_line(150,50, 150,800, fill="red", width = 5)
            p = False
        #Check who wins for the second column combination
        elif "  " in mystuff and "     " in mystuff and "        " in mystuff:
            winner = 2
            canvas.create_line(430,50, 430,800, fill="red", width = 5)
            p = False
        elif "  " in opponenetstuff and "     " in opponenetstuff and "        " in opponenetstuff:
            winner = 1
            canvas.create_line(430,50, 430,800, fill="red", width = 5)
            p = False
        #Check who wins for the third column combination
        elif "   " in mystuff and "      " in mystuff and  "         " in mystuff:
            winner = 2
            canvas.create_line(670,50, 670,800, fill="red", width = 5)
            p = False
        elif "   " in opponenetstuff and "      " in opponenetstuff and "         " in opponenetstuff:
            winner = 1
            canvas.create_line(670,50, 670,800, fill="red", width = 5)
            p = False
        #------------------------------------------------------------------------------------------------------    
        #Check who wins for the first diagonal combination
        elif " " in mystuff and "     " in mystuff and "         " in mystuff:
            winner = 2
            canvas.create_line(50,70, 790,800, fill="red", width = 5)
            p = False
        elif " " in opponenetstuff and "     " in opponenetstuff and "         " in opponenetstuff:
            winner = 1
            canvas.create_line(50,70, 790,800, fill="red", width = 5)
            p = False
        #Check who wins for the second diagonal combination
        elif "   " in mystuff and "     " in mystuff and "       " in mystuff:
            winner = 2
            canvas.create_line(800,50,0,790, fill="red", width = 5)
            p = False
        elif "   " in opponenetstuff and "     " in opponenetstuff and "       " in opponenetstuff:
            winner = 1
            canvas.create_line(800,50,0,790, fill="red", width = 5)

            p = False
        #Draw
        if counter == 9:
            winner = 3
            print("Draw")
            p = False
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
    label3 = tk.Label(window, text = "Play Again? Y/N", font=("Arial", 35)).pack()
    #play_gain1 = tk.Button(window, text = "Y", command = lambda: again(window, canvas, connectionSocket)).pack()
    #play_gain2 = tk.Button(window, text = "N", command = window.destroy).pack()
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='disabled')
    answerthread = threading.Thread(target=answercheck, args=(connectionSocket,))
    answerthread.start()
    play_gain2 = tk.Button(window, text = "N", command = lambda: (window.destroy(), window.quit())).pack()
    play_gain1 = tk.Button(window, text = "Y", command = lambda: stop(window, canvas, connectionSocket)).pack()
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='disabled')
    answerthread.join()
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='normal')
    
    return winner
def answercheck(connectionSocket):
    global answer
    connectionSocket.recv(1024).decode()
    answer = int(answer)

def stop(window, canvas, connectionSocket):
    global again
    canvas.delete('all')
    for widget in window.winfo_children():
        widget.destroy()
    window.destroy()
    window.quit()
    again = 1
    global counter
    global opponenetstuff
    global mystuff
    mystuff = []
    opponenetstuff = []
    counter = 0
#Create window thread
def create_game(connectionSocket):
    global answer
    if answer == 0:
        first = True
        print("going 1st")
    else:
        first = False
        print("going 2nd")
    sleep(4)

    window = tk.Tk()
    window.title("Tic Tac Toe")
    window.resizable(False, False)

    frame = tk.Frame(window)
    frame.pack()

    window.geometry("800x800")
    canvas = tk.Canvas(window, width=800, height=800)
    canvas.place(x=0, y=50)
    #Send updated ui to client and disable all buttons bec it is not
    #Our turn after we had clicked a button
    #Turn variable

    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()
    def replacebut(widget,x,y):
        widget.destroy()
        circle = canvas.create_oval(x, y - 10, x+170, y+150, fill="", outline="black", width=5)

    def send_msg(butt,x,y):
        global counter
        global winner
        counter += 1
        c = butt.cget('text')
        butt.destroy()
        turn.config(text="Its Opponents turn!")
        X1= canvas.create_line(x+ 20, y + 150, x+170, y-20, fill="black", width = 5)
        X2= canvas.create_line(x+170, y+150, x+20, y-20, fill="black", width = 5)
        #canvas.create_line(70, 250, 220, 80, fill="black", width = 5)
        #canvas.create_line(220, 250, 70, 80, fill="black", width = 5)
        #x - 50 y -100
        updated = {'butt': c, 'x': x, 'y': y}
        #Add to database to determine results
        mystuff.append(c)
        mystuff.append(x)
        mystuff.append(y)
        connectionSocket.send(pickle.dumps(updated))
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                #Disable state after we have picked a spot
                widget.config(state='disabled')
        turn.config(text="Its opponents turn!")
        #End turn by start receiving
        #rec()
        if winner == 0:
            g = threading.Thread(target=rec, daemon=True).start()
    def rec():
        msg = connectionSocket.recv(1024)
        window.after(0, lambda: turn.config(text="It's your turn!"))  # Schedule update in the main thread

        #Its your turn now so change text and recieve message
        window.after(0, lambda: turn.config(text="It's your turn!"))  # Schedule update in the main thread
        turn11 = pickle.loads(msg)
        #Add opponent to database
        p = turn11.get('butt')
        opponenetstuff.append(p)
        opponenetstuff.append(turn11.get('x'))
        opponenetstuff.append(turn11.get('y'))

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

    #Window size/Create board

    canvas.create_line(280, 70, 280, 800, fill="black", width = 5)
    canvas.create_line(525, 70, 525, 800, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 500, 760, 500, fill="black", width = 5)
    
    if first == True:
        turn = tk.Label(window, text="Its your turn!", font=("Arial", 20))
        turn.pack()
    else:
        turn = tk.Label(window, text="Its Opponents turn!", font=("Arial", 20))
        turn.pack()



    
    #Row 1
    topleft = tk.Button(window, text=" ", bd=0, width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topleft,50,100))
    topleft.place(x=50, y=120)
    topcenter = tk.Button(window, text="  ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topcenter,295,100))
    topcenter.place(x=295, y=120)
    topright = tk.Button(window, text="   ",bd=0,  width=17, height=6 ,font=("Arial", 16),command=lambda: send_msg(topright,540,100))
    topright.place(x=540, y=120)
    #Middle row 2
    midleft = tk.Button(window, text="    ", bd=0, width=17, height=6 ,font=("Arial", 16), command = lambda: send_msg(midleft,40,330))
    midleft.place(x=50, y=350)    
    midcenter = tk.Button(window, text="     ",bd=0,  width=17, height=6 ,font=("Arial", 16), command = lambda: send_msg(midcenter,300,330))
    midcenter.place(x=295, y=350)
    midright = tk.Button(window, text="      ",bd=0,  width=17, height=6 ,font=("Arial", 16), command = lambda: send_msg(midright,555,330))
    midright.place(x=540, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="       ",bd=0,  width=17, height=8 ,font=("Arial", 16), command = lambda: send_msg(botleft,50,580))
    botleft.place(x=40, y=580)
    botcenter = tk.Button(window, text="        ",bd=0,  width=17, height=8 ,font=("Arial", 16), command = lambda: send_msg(botcenter,310,580))
    botcenter.place(x=290, y=580)
    botright = tk.Button(window, text="         ",bd=0,  width=17, height=8 ,font=("Arial", 16), command = lambda: send_msg(botright,570,580))
    botright.place(x=540, y=580)
    #turn.config(text=f"Value: {data.get('value', 0)}")
    
    if first == False:
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state='disabled')

    checkwin = threading.Thread(target= lambda: check_win(canvas, window)).start()
    if first == False:
        g = threading.Thread(target=rec).start()

    window.mainloop()
        
answer = connectionSocket.recv(1024).decode()
answer = int(answer)
game = True
while game == True:
    gamestart = connectionSocket.recv(1024).decode()
    if gamestart == '1':

        #For structure we do this in a thread
        gap = threading.Thread(target=create_game, args=(connectionSocket,))
        gap.start()   
        gap.join()

        print("No Error")
        while again ==1:
            winner = 0
            again = 0
            poo = threading.Thread(target=create_game, args=(connectionSocket,))
            poo.start()
            poo.join()
        print("Byeee")
        game = False
    else:
        print('Game not started due to another value, Closing connection')
        sleep(1)
        game = False
        connectionSocket.shutdown(SHUT_RDWR)
        connectionSocket.close()
