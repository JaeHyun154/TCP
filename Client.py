#TCP Client

from socket import *
# 강아지 센서 정보 TCP Client
# serverName = 'nsl2.cau.ac.kr'
serverName = '192.168.1.99'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Client is running on port", clientSocket.getsockname()[1])
activity_data = clientSocket.getsockname()[0] + ":" + str(clientSocket.getsockname()[1])

while True:
    print('client is sending data : ', activity_data)

    message = input('to close connection enter -1, if not 1: ')
    data = '-1' if message == '-1' else activity_data

    clientSocket.send(data.encode())

    modifiedMessage = clientSocket.recv(2048)
    print('Reply from server:', modifiedMessage.decode())
    if modifiedMessage.decode() == '-1':
        clientSocket.close()
        break
