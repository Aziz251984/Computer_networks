from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("serverStatus: Ready")
while True:
    msg, clientAddr = serverSocket.recvfrom(2048)
    print("Recieving from: ", clientAddr) 
    returnMsg = msg.decode().upper()
    serverSocket.sendto(returnMsg.encode(), clientAddr)
