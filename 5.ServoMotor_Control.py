import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

ServoPin=17
GPIO.setup(ServoPin, GPIO.OUT)
p=GPIO.PWM(ServoPin, 50)    #서보모터<-PWM으로 데이터 변환해서 주어야 함
p.start(50)

while True:
    p.ChangeDutyCycle(12.0)
    sleep(1)
    p.ChangeDutyCycle(9.5)
    sleep(1)
    p.ChangeDutyCycle(7.0)
    sleep(1)
    p.ChangeDutyCycle(4.5)
    sleep(1)
    p.ChangeDutyCycle(2.0)
    sleep(1)