#!/usr/bin/env python

# Import libary functions we need
import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BCM)

# Set which GPIO pins the drive outputs are connected to
LEFT_WHEEL_FORWARD = 27
RIGHT_WHEEL_FORWARD = 5

LEFT_WHEEL_REVERSE = 22
RIGHT_WHEEL_REVERSE = 6


# Set all of the drive pins as output pins
motors = [LEFT_WHEEL_FORWARD, RIGHT_WHEEL_FORWARD, LEFT_WHEEL_REVERSE, RIGHT_WHEEL_REVERSE]

for item in motors:
        GPIO.setup(item, GPIO.OUT)        



# Function to set both drives off
def RobotStop():
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.LOW)
        GPIO.output(LEFT_WHEEL_REVERSE, GPIO.LOW)
	GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.LOW)	
	GPIO.output(RIGHT_WHEEL_REVERSE,GPIO.LOW)

def RobotForward():
	GPIO.output(LEFT_WHEEL_FORWARD, GPIO.HIGH)
	GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.HIGH)
	GPIO.output(LEFT_WHEEL_REVERSE, GPIO.LOW)
	GPIO.output(RIGHT_WHEEL_REVERSE, GPIO.LOW)

def RobotTurnRight():
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.LOW)
	GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.HIGH)
	GPIO.output(LEFT_WHEEL_REVERSE, GPIO.HIGH)
	GPIO.output(RIGHT_WHEEL_REVERSE, GPIO.LOW)
	

try:
        RobotStop()
	while True:                

		print "Enter the command"
		print 'Press ctrl + c to stop and exit'
		a=raw_input()
		if a == 'f':
			RobotForward()
		elif a == 'r':
                        RobotTurnRight()
                elif a=='s':
                        print 'Stop'
                        RobotStop()
		elif a=='z':
			print 'exiting'
			RobotStop()
			GPIO.cleanup()
			sys.exit()
		else: 
                        print 'wrong command'
			RobotStop()
		time.sleep(.1)

except KeyboardInterrupt:

# CTRL+C exit, turn off the drives and release GPIO pins
        print "Stopped early, please turn off my power!"
	RobotStop()
	GPIO.cleanup()

