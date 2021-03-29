import Smart_Finger_Servo #importing servo motor program
import send_email #importing email when on program
from socket import *
from time import ctime
import RPi.GPIO as GPIO

Smart_Finger_Servo.setup()

ctrCMD = ['1','0']
HOST = '' #allows any client to communicate with the server
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
while True:
    print ('Waiting for connection')
    tcpCliSock,addr = tcpSerSock.accept() #printing clients address once it connects
    print ('...connected from :', addr)
    try:
        while True: #checking what data is being recieved, stops if there is no data
            data = ''
            data = tcpCliSock.recv(BUFSIZE)
            datanew = data.decode('UTF-8')           
            if not data:
                break
            if datanew == ctrCMD[0]:
                Smart_Finger_Servo.ServoOn()
                print ('Increase: ',Smart_Finger_Servo.cur_X)
                send_email.On()
            if datanew == ctrCMD[1]:
                Smart_Finger_Servo.ServoOff()
                print ('Decrease: ',Smart_Finger_Servo.cur_X)
                send_email.Off()
    except KeyboardInterrupt:
        Smart_Finger_Servo.close()
        GPIO.cleanup()
tcpSerSock.close()