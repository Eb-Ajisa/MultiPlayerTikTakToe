from socket import *
from time import sleep
import tkinter as tk
import tkinter.scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import threading
import random
import pickle
#Winner 0: No winner yet
#Winner 1: Player 1 wins
#Winner 2: Player 2 wins
#Winner 3: Draw
winner = 0
answer = 0
#Socket Configuration
hostname = gethostname()
ip_address = gethostbyname(hostname)
ip_address = str(ip_address)

serverName = ip_address # server IP
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
counter = 0
#Loop for socket
game = True
again = 0
#Database for player 2
mystuff = []
#Database for player 1
opponenetstuff = []

def check_win(canvas, window):
    p = True
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
            canvas.create_line(50,70, 790,800, fill="black", width = 5)
            p = False
        elif " " in opponenetstuff and "     " in opponenetstuff and "         " in opponenetstuff:
            winner = 1
            canvas.create_line(50,70, 790,800, fill="black", width = 5)
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
    #play_gain1 = tk.Button(window, text = "Y", command = lambda: again(window, canvas, clientSocket)).pack()
    #play_gain2 = tk.Button(window, text = "N", command = window.destroy).pack()
    answer = random.randint(0,1)
    answerr = str(answer)
    clientSocket.send(answerr.encode())
    play_gain2 = tk.Button(window, text = "N", command = lambda: (window.destroy(), window.quit())).pack()
    play_gain1 = tk.Button(window, text = "Y", command = lambda: stop(window, canvas, clientSocket)).pack()
    return winner

def stop(window, canvas, clientSocket):
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
def create_game(clientSocket):
    global answer
    if answer == 0:
        first = False
        print("Going second")
    else:
        first = True
        print("Going first")
    sleep(4)



    #Create window
    window = tk.Tk()
    #Title for TikTacToe
    window.title("Tic Tac Toe")
    window.resizable(False, False)


    frame = tk.Frame(window)
    frame.pack()
    
    def replacebut(widget,x,y):
        #Player 1 symbol
        widget.destroy()
        X1= canvas.create_line(x+ 20, y + 150, x+170, y-20, fill="black", width = 5)
        X2= canvas.create_line(x+170, y+150, x+20, y-20, fill="black", width = 5)
        #canvas.create_line(70, 250, 220, 80, fill="black", width = 5)
        #canvas.create_line(220, 250, 70, 80, fill="black", width = 5)
        #x - 50 y -100
    def send_msg(butt,x,y):
        global winner
        global counter 
        counter += 1
        #Recieve text and destroy button and switch turns 
        c = butt.cget('text')
        butt.destroy()
        turn.config(text="Its Opponents turn!")
        #Player 2 symbol and add player 2 stuff to database
        circle = canvas.create_oval(x, y - 10, x+170, y+150, fill="", outline="black", width=5)
        updated = {'butt': c, 'x': x, 'y': y}
        mystuff.append(c)
        mystuff.append(x)
        mystuff.append(y)
        #Send to player 1
        clientSocket.send(pickle.dumps(updated))
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                #Disable all buttons/window
                widget.config(state='disabled')
        #Say whos turn it is
        turn.config(text="Its opponents turn!")

        #End turn by start receiving thread
        if winner == 0:
            g = threading.Thread(target=rec, daemon=True).start()


    #Window size
    window.geometry("800x800")
    #Create tiktaktoe board
    canvas = tk.Canvas(window, width=800, height=800)
    canvas.place(x=0, y=50)
    canvas.create_line(280, 70, 280, 800, fill="black", width = 5)
    canvas.create_line(525, 70, 525, 800, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 260, 760, 260, fill="black", width = 5)
    canvas.create_line(20, 500, 760, 500, fill="black", width = 5)

    if first == False:
        turn = tk.Label(window, text="Its opponents turn", font=("Arial", 20))
        turn.pack()
    else:
        turn = tk.Label(window, text="Its your turn", font=("Arial", 20))
        turn.pack()
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()
    #Row 1 we will use text for database to determine winner/loser/draw
    topleft = tk.Button(window, text=" ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topleft,50,100))
    topleft.place(x=50, y=120)
    topcenter = tk.Button(window, text="  ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topcenter,295,100))
    topcenter.place(x=295, y=120)
    topright = tk.Button(window, text="   ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topright,540,100))
    topright.place(x=540, y=120)
    
    #Middle row 2
    midleft = tk.Button(window, text="    ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(midleft,40,330))
    midleft.place(x=50, y=350)    
    midcenter = tk.Button(window, text="     ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(midcenter,300,330))
    midcenter.place(x=290, y=350)
    midright = tk.Button(window, text="      ",bd=0,  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(midright,550,330))
    midright.place(x=540, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="       ",bd=0,  width=18, height=8 ,font=("Arial", 16), command=lambda: send_msg(botleft,50,580))
    botleft.place(x=40, y=580)
    botcenter = tk.Button(window, text="        ",bd=0,  width=17, height=8 ,font=("Arial", 16), command=lambda: send_msg(botcenter,310,580))
    botcenter.place(x=290, y=580)
    botright = tk.Button(window, text="         ",bd=0,  width=17, height=8 ,font=("Arial", 16), command=lambda: send_msg(botright,570,580))
    botright.place(x=540, y=580)

    #Recieve (Will use semaphore to allow for automation)
    def rec():
        msg = clientSocket.recv(1024)
        window.after(0, lambda: turn.config(text="It's your turn!"))  # Schedule update in the main thread

        #Its your turn now so change text and recieve message
        turn11 = pickle.loads(msg)
        #Add to opponenetstuff/player 1 database
        p = turn11.get('butt')
        opponenetstuff.append(p)
        opponenetstuff.append(turn11.get('x'))
        opponenetstuff.append(turn11.get('y'))


        print(turn11)
        for widget in window.winfo_children():

            if isinstance(widget, tk.Button):
                #Recieve the text based on any button clicked to find the right one
                #Start your own turn
                widget.config(state='normal')
                widget.cget('text')
                #If recieved text == button text then replace button with symbol
                if turn11.get('butt') == widget.cget('text'):
                    x = turn11.get('x')
                    y = turn11.get('y')
                    window.after(0, replacebut(widget,x,y))
        global counter
        counter += 1
        return None
    
    #For work in progress
    if first == False:
        for widget in window.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state='disabled')

    
    checkwin = threading.Thread(target= lambda: check_win(canvas, window)).start()
    if first == False:
        g= threading.Thread(target=rec).start()
    


    window.mainloop()
    #rec()


#Game initalization
sentence = input('Press 1 to start game: ')

#Error Handling
if sentence != '1':
      game = False
      print("Incorrect value, closing connection")
      clientSocket.shutdown(SHUT_RDWR)
      clientSocket.close()

answer = random.randint(0,1)
answerr = str(answer)
clientSocket.send(answerr.encode())
#Game/SocketLoop
while game == True:

    clientSocket.send(sentence.encode())

    p2game = threading.Thread(target=create_game, args=(clientSocket,))
    p2game.start()
    p2game.join()
    while again ==1:
        winner = 0
        again = 0
        poo = threading.Thread(target=create_game, args=(clientSocket,))
        poo.start()
        poo.join()
    print("Byeee")
    game = False

clientSocket.shutdown(SHUT_RDWR)
clientSocket.close()
