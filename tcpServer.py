from socket import *
import openpyxl

# Server configuration
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server Status: Ready")

# Load the Excel workbook
try:
    workbook = openpyxl.load_workbook('sensorData.xlsx')

    # Select a specific sheet
    sheet = workbook['Sheet1']

    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Connected: ", addr)
        msg = connectionSocket.recv(1024).decode()
        print("Received Message: ", msg)

        # Access data from the sheet
        cell_value = sheet['A1'].value
        print("Excel Cell Value:", cell_value)

        returnMsg = input("Input return message: ")
        connectionSocket.send(returnMsg.encode())
        connectionSocket.close()
        print("Closed: ", addr, '\n')

except FileNotFoundError:
    print("Excel file not found.")

serverSocket.close()
