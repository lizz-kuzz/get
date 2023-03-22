import RPi.GPIO as GPIO
import time

dac =    [26, 19, 13, 6, 5, 11, 9, 10]

number = [0,   1,  1, 0, 0,  1, 0,  0]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


GPIO.output(dac, number)

time.sleep(15)

GPIO.output(dac, 0)

GPIO.cleanup()

#2   -> 0,482
#255 -> 3,254
#127 -> 1,622
#100 -> 1,280
#64  -> 0,822
#32  -> 0,497
#5   -> 0,482
#0   -> 0,482
#256 -> 0,482