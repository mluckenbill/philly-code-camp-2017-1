import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 23
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for sensor to settle"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

print "Starting sonar"

while GPIO.input(ECHO) == 0:
	pass

start = time.time()

while GPIO.input(ECHO) == 1:
	pass

stop = time.time()

print "Sonar responded"

pulse_duration = stop - start
distance  = pulse_duration * 17150
distance = round(distance, 2)

print "Distance: ", distance, " cm"

GPIO.cleanup()
