import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    val = input("введите число от 0 до 255\n")
    print(int(float(val)))
    print(val)
    while val != 'q':
        if not is_number(val):
            print("не число") 
        elif int(float(val)) == val:
            print("не целое число") 
        elif int(float(val)) < 0 or int(float(val)) > 255:
            print("число не из того диапазона") 
        else:
            binary = decimal2binary(int(float(val)))
            print(binary)
            print("{:.4f}".format(int(val)/256*3.3))
            GPIO.output(dac, binary)   
        val = input("введите число от 0 до 255\n")

        

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


    