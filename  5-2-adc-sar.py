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
    value = 0
    for i in range(7, 1,  -1):
        value += 2**i
        signal = dec2bin(value)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        comp_value = GPIO.input(comp)
        if comp_value == 0:
            value -= 2**i
        
    return value

try: 
    while True:
        start = time.time()
        value = adc()
        volt = value / (2**8) * 3.3
        end = time.time() - start 
        print("value = {:^3}, volt = {:.2f}".format(value, volt))
        print("time = {:.4f}".format(end))



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
