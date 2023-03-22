import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO.setup(14, GPIO.OUT)

#GPIO.output(14, 1)




for i in range(4):
    print("on")
    GPIO.output(14, 1)
    time.sleep(2)
    GPIO.output(14, 0)
    print("off")
    time.sleep(2)
 