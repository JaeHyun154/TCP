#TCP Server 

from socket import *
from datetime import datetime
import requests


serverPort = 12000
serverIP = '172.20.10.8'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('0.0.0.0', serverPort))
serverSocket.listen(1)

# arduino_dog = serial.Serial(
#     port = 'COM4',
#     baudrate= 9600,
# )    

webserver_url = 'http://127.0.0.1:8000/capstone/insertactivity'
# webserver_url = 'http://127.0.0.1:8000/capstone/'

print("Server is ready to receive on port", serverPort)
(connectionSocket, clientAddress) = serverSocket.accept()
print('Connection request from', clientAddress)
print('강아지와 연결되었습니다')

# while True:
    
#     try:
#         if arduino_dog.readable():
#             res = arduino_dog.readline()
#             json_data = json.loads(res.decode()[:-1])
#             json_data['time'] = datetime.now().strftime('%년--%월--%일--%시:%분:%초')
#             print(json_data)
#             client = requests.session()
            
#     except:
#         print('강아지와 연결되지 않았습니다')


while True:
    message = connectionSocket.recv(2048)
    print('received message ', message.decode())
    if message.decode() == '-1':
        reply = '-1'
        connectionSocket.send(reply.encode())
        connectionSocket.close()
        break
    else:
        post_url = webserver_url 
        parameters = message.decode().split(',')   
        for p in parameters:
            post_url += '/' + p
        print('get requst url : ', post_url)
        requests.get(post_url)
        modifiedMessage = message.decode().upper()
        connectionSocket.send(modifiedMessage.encode())

