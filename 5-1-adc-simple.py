import RPi.GPIO as GPIO
import time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
    
def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

    
def adc():
    for value in range(256):
        signal = dec2bin(value)
        GPIO.output(dac, signal) 
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        volt = value / (2**8) * 3.3
        if comp_value == 0:
            break 
    print("value = {:^3}, ".format(value))
    return volt

try: 
    while True:
        start = time.time()
        volt = adc()
        end = time.time() - start 
        print("volt = {:.2f}".format(volt))
        print("time = {:.4f}".format(end))


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
