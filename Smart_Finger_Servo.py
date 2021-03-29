import RPi.GPIO as GPIO
import time
cur_X =  12 #initial value of servo motor
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    global servo
    servo=GPIO.PWM(11,50)
    servo.start(0)
    #servo.ChangeDutyCycle(2.5)
    #start pwm with Duty Cycle is 2% --> Pulse width = 2%*20ms = 0.4ms
    #Create Pwm on pin 11 with frequency 50Hz --> period 20ms
def ServoOn():
    global cur_X
    cur_X -= 3
    if cur_X < 9:
        cur_X = 9
    servo.ChangeDutyCycle(cur_X)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    time.sleep(0.5)
def ServoOff():
    global cur_X
    cur_X += 3
    if cur_X > 12:
        cur_X = 12
    servo.ChangeDutyCycle(cur_X)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)
    time.sleep(0.5)
def close():
    servo.stop()
#if _name_ == '_main_':
  #  setup()