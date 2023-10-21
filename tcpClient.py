from socket import *
from time import time
import openpyxl

# Server configuration
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(1)

# Connect to the server
try:
    t = time()
    clientSocket.connect((serverName, serverPort))
    print("RTT: ", time() - t, 'seconds')

    # Send a message to the server
    msg = input('Input message: ')
    clientSocket.send(msg.encode())

    # Receive a response from the server
    returnMsg = clientSocket.recv(1024)
    print("Return:", returnMsg.decode())

    # Close the socket
    clientSocket.close()
except timeout:
    print("Connection timed out.")

# Load the Excel workbook
try:
    workbook = openpyxl.load_workbook('sensorData.xlsx')

    # Select a specific sheet
    sheet = workbook['Sheet1']

    # Access data from the sheet
    cell_value = sheet['A1'].value
    print("sensorData", cell_value)
except FileNotFoundError:
    print("Excel file not found.")
