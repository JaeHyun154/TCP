import serial
import requests
import json
import time

#급식기와 연결 (serial 통신)
ser = serial.Serial('COM5', 9600)  # COM에 연결된 Arduino에 맞춰서 수정
server_ip = '127.0.0.1'
server_port = 8000
while True:
    data = ser.readline().decode('latin-1').strip()
    print('Received:', data)

    if data == 'Requesting food amount...':
        
        server_url = 'http://127.0.0.1:8000/capstone/getmealAmount/'  # 서버 주소에 맞게 수정
        print('Sending request to server:', server_url)
        mealAmount = requests.get(server_url).json().get("meal amount")
        print(mealAmount)
        if(mealAmount >= 10):
            ser.write(str(mealAmount).encode())
        else:
            ser.write("move more".encode())
    time.sleep(1)


ser.close()