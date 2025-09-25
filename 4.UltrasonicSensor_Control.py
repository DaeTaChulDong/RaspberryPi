import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER=17 #초음파 발생핀
GPIO_ECHO=18    #초음파 수신핀

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)  #발생은 출력 형태
GPIO.setup(GPIO_ECHO,GPIO.IN)#수신은 인풋 형태

try:
    while True:
        GPIO.output(GPIO_TRIGGER, True) #초음파 발생

        sleep(0.1)
        GPIO.output(GPIO_TRIGGER, False)    #초음파 발생 중지

        StartTime=time()
        StopTime=time()
        
        while GPIO.input(GPIO_ECHO)==0:
            StartTime=time()    #들어온 값에 따라 시작 시간 저장
        
        while GPIO.input(GPIO_ECHO)==1:
            StopTime=time() #들어온 값에 따라 종료시간 저장
        
        TimeElapsed=StopTime=StartTime
        distance=(TimeElapsed*34300)/2
        print("Measured Distance = %.1fcm" &distance)
        sleep(1)

except KeyboardInterrupt:
    pass
    print("Exit with ^C")
    GPIO.cleanup()
    exit()