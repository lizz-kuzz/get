import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)



GPIO.setup(14, GPIO.OUT)
pin = GPIO.PWM(14, 1000)
pin.start(0)

try:
    while True:
        x = int(input("input coef: "))
        pin.ChangeDutyCycle(x)
        print(x* 3.3 /100)
finally:
    GPIO.output(14, 0)
    GPIO.cleanup() 