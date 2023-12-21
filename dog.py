import serial
import requests
import json
import time
import datetime

# 강아지 센서 정보 (serial 통신)
ser = serial.Serial('COM5', 9600)  # COM에 연결된 Arduino에 맞춰서 수정
server_ip = '127.0.0.1'
server_port = 8000
while True:
    data = ser.readline().decode('latin-1').strip()
    print('Received:', data)

    if data == '-1':
        break
    
    parameters = json.loads(data)
    server_url = 'http://127.0.0.1:8000/capstone/insertactivity/'  # 서버 주소에 맞게 수정
    if len(parameters) >= 1:
        # post_data = {'ip': '10.124.0.50', 'Acc_x': parameters['AcX'], 'Acc_y': parameters['AcY'], 'Acc_z': parameters['AcZ'],
                    #  'Gyro_x': parameters['GyX'], 'Gyro_y': parameters['GyY'], 'Gyro_z': parameters['GyZ']}
        server_url += '127.0.0.1:8000/'
        for v in parameters.items():
            server_url += str(v[1]) + '/'
        print(server_url)
        server_url = server_url[:-1]

        print('Sending data to server:', server_url)
        response = requests.get(server_url, data=server_url)
        # print('Server response:', response.text)
    time.sleep(1)


ser.close()