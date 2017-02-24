import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

print('Buzzer On')
GPIO.output(17,GPIO.HIGH)
time.sleep(1)

print('Buzzer')
GPIO.output(17,GPIO.LOW)

GPIO.cleanup()
