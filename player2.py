from socket import *
from time import sleep
import tkinter as tk
import tkinter.scrolledtext
from tkinter import messagebox
from tkinter import simpledialog
import threading
import pickle
#Winner 0: No winner yet
#Winner 1: Player 1 wins
#Winner 2: Player 2 wins
#Winner 3: Draw
winner = 0
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

#Database for player 2
mystuff = []
#Database for player 1
opponenetstuff = []


def check_win(canvas):
    p = True
    while p == True:
    #Check who wins for the firsrt row combination
        if " " and "  " and "   " in opponenetstuff:
            winner = 1
            canvas.destroy()
            print("Player 1 wins")
            p = False
        
        if " " and "  " and "   " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the second row combination
        if "    " and "     " and "      " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if "    " and "     " and "      " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the third row combination
        if "       " and "        " and "         " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if "       " and "        " and "         " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the first column combination
        if " " and "    " and "       " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if " " and "    " and "       " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the second column combination
        if "  " and "     " and "        " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if "  " and "     " and "        " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the third column combination
        if "   " and "      " and "         " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if "   " and "      " and "         " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the first diagonal combination
        if " " and "     " and "         " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if " " and "     " and "         " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
            

        #Check who wins for the second diagonal combination
        if "   " and "     " and "       " in opponenetstuff:
            winner = 1
            print("Player 1 wins")
            p = False
            
        if "   " and "     " and "       " in mystuff:
            winner = 2
            print("Player 2 wins")
            p = False
        if counter == 9:
            winner = 3
            print("Draw")
            p = False
        
def create_game(clientSocket):
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
        g = threading.Thread(target=rec).start()


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

    turn = tk.Label(window, text="Its opponents turn", font=("Arial", 20))
    turn.pack()
    #declare the name
    label = tk.Label(window, text="Tic Tac Toe")
    label.pack()
    
    #Row 1 we will use text for database to determine winner/loser/draw
    topleft = tk.Button(window, text=" ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topleft,50,100))
    topleft.place(x=50, y=120)
    topcenter = tk.Button(window, text="  ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topcenter,295,100))
    topcenter.place(x=295, y=120)
    topright = tk.Button(window, text="   ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(topright,540,100))
    topright.place(x=540, y=120)

    #Middle row 2
    midleft = tk.Button(window, text="    ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(midleft,40,330))
    midleft.place(x=50, y=350)    
    midcenter = tk.Button(window, text="     ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(midcenter,300,330))
    midcenter.place(x=290, y=350)
    midright = tk.Button(window, text="      ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(midright,550,330))
    midright.place(x=540, y=350)

    #Bot row 3
    botleft = tk.Button(window, text="       ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(botleft,50,580))
    botleft.place(x=50, y=600)
    botcenter = tk.Button(window, text="        ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(botcenter,310,580))
    botcenter.place(x=290, y=600)
    botright = tk.Button(window, text="         ",  width=17, height=6 ,font=("Arial", 16), command=lambda: send_msg(botright,570,580))
    botright.place(x=540, y=600)

    #Recieve (Will use semaphore to allow for automation)
    def rec():
        msg = clientSocket.recv(1024)
        #Its your turn now so change text and recieve message
        turn.config(text="Its your turn!")
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
    for widget in window.winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state='disabled')

    
    checkwin = threading.Thread(target= lambda: check_win(canvas)).start()
    g= threading.Thread(target=rec).start()


    window.mainloop()


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
    print(counter)
    again = input("Go again?(Press 1 to go again): ")
    if again != '1':
        game = False
        clientSocket.shutdown(SHUT_RDWR)
        clientSocket.close()
        break


