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

# Function to set both drives on
def RobotForward():
        RobotStop()
	GPIO.output(LEFT_WHEEL_FORWARD, GPIO.HIGH)
	GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.HIGH)
	GPIO.output(LEFT_WHEEL_REVERSE, GPIO.LOW)
	GPIO.output(RIGHT_WHEEL_REVERSE,GPIO.LOW)
        
def RobotLeft():
        RobotStop()
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.LOW)
        GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.HIGH)

        GPIO.output(LEFT_WHEEL_REVERSE, GPIO.LOW)
	GPIO.output(RIGHT_WHEEL_REVERSE,GPIO.LOW)
        

def RobotRight():
        RobotStop()
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.HIGH)
        GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.LOW)

        GPIO.output(LEFT_WHEEL_REVERSE, GPIO.LOW)
	GPIO.output(RIGHT_WHEEL_REVERSE,GPIO.LOW)

def RobotReverse():
        RobotStop()
        GPIO.output(LEFT_WHEEL_REVERSE, GPIO.HIGH)
        GPIO.output(RIGHT_WHEEL_REVERSE, GPIO.HIGH)
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.LOW)
        GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.LOW)

def RobotSpinLeft():
        RobotStop()
        GPIO.output(RIGHT_WHEEL_REVERSE, GPIO.LOW)
        GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.HIGH)
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.LOW)
        GPIO.output(LEFT_WHEEL_REVERSE, GPIO.HIGH)
        
        

def RobotSpinRight():
        RobotStop()
        GPIO.output(RIGHT_WHEEL_REVERSE, GPIO.HIGH)
        GPIO.output(RIGHT_WHEEL_FORWARD, GPIO.LOW)
        GPIO.output(LEFT_WHEEL_FORWARD, GPIO.HIGH)
        GPIO.output(LEFT_WHEEL_REVERSE, GPIO.LOW)


try:
        RobotStop()
	while True:                

		print "Enter the command"
		print 'Press ctrl + c to stop and exit'
		a=raw_input()
		if a=='w':
                        print '------FORWARD'
			RobotForward()			
		elif a=='a':
                        print '------LEFT'
			RobotLeft()
		elif a=='d':
                        print '------RIGHT'
			RobotRight()
		elif a=='s':
                        print '------REVERSE'
			RobotReverse()
		elif a=='q':
                        print '------SPIN LEFT'
                        RobotSpinLeft()
                elif a=='e':
                        print 'Spinning Right'
                        RobotSpinRight()
                elif a=='r':
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

