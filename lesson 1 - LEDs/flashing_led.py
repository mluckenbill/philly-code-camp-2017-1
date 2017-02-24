import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

def led_on():
        print("LED On")
        GPIO.output(17, GPIO.HIGH)
def led_off():
        print("LED Off")
        GPIO.output(17, GPIO.LOW)

try:
        print('Press ctrl + c to stop and exit')

        while True:
                led_on()
                time.sleep(1)
                led_off()
                time.sleep(1)
                
except KeyboardInterrupt:
        print("Turning off the lights now")
        led_off()
        GPIO.cleanup()
