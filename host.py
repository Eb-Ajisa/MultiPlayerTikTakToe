from socket import *
from time import sleep
serverPort = 10000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('Waiting for player 2')
game = True
while game == True:
    connectionSocket, addr = serverSocket.accept()
    gamestart = connectionSocket.recv(1024).decode()
    if gamestart == '1':
        print('Game started')

    else:
        print('Game not started Closing connection')
        sleep(1)
        game = False
        connectionSocket.shutdown(2)
        connectionSocket.close()
        
