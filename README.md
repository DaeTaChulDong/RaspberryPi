# RaspberryPi

# GPIO control code

# 핀 번호를 라즈베리파이 보드(BOARD) 번호로 참조 BCM 모드
GPIO.setmode(GPIO.BOARD/BCM)

# 핀을 입력으로 설정하여 핀을 출력으로 설정
GPIO.setup(pin, GPIO.IN/OUT)

# 디지털 출력을 HIGH / LOW로 설정
GPIO.output(pin.GPIO.HIGH/LOW)

# 디지털 값을 읽음
GPIO.input(pin)

# GPIO 모듈의 점유 리소스를 해제
GPIO.cleanup()

# RPI.GPIO 모듈의 버전값을 갖는 변수
GPIO. VERSION
