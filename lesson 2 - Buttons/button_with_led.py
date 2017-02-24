from gpiozero import Button
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
                print('Press button to turn on lights')
                button.wait_for_press()
                led_on()
                print('Press button to turn off lights')
                button.wait_for_press()
except KeyboardInterrupt:
        print("Exiting Application")
        led_off()
        GPIO.cleanup()