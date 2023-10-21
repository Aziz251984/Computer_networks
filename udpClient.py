from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = input('Input lowercase sentance:')
clientSocket.sendto(msg.encode(), (serverName, serverPort))
returnMsg, serverAddress = clientSocket.recvfrom(2048)
print(returnMsg.decode())
clientSocket.close()
