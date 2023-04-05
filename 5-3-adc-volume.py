import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)


       
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



def volume(value):
    if value == 0: GPIO.output(leds, dec2bin(0))
    elif 0 < value & value < 24: GPIO.output(leds, dec2bin(1))
    elif 24 <= value & value < 24: GPIO.output(leds, dec2bin(3))
    elif 24 <= value & value < 32: GPIO.output(leds, dec2bin(7))
    elif 32 <= value & value < 40: GPIO.output(leds, dec2bin(15))
    elif 40 <= value & value < 48: GPIO.output(leds, dec2bin(31))
    elif 48 <= value & value < 56: GPIO.output(leds, dec2bin(63))
    elif 56 <= value & value < 63: GPIO.output(leds, dec2bin(127))
    else:  GPIO.output(leds, dec2bin(255))
    
try: 
    while True:
        value = adc()
        volume(value)
        volt = value / 256 * 3.3
        print("value = {:^3}, volt = {:.2f}".format(value, volt))



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
