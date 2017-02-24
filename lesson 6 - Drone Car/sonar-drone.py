import RPi.GPIO as GPIO                    #Import GPIO library
import time
#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers

TRIG = 18
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input

time.sleep(5)


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
  count=0
  while True:
   i=0
   avgDistance=0
   for i in range(5):
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    time.sleep(0.1)                                   #Delay
    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
    time.sleep(0.00001)                           #Delay of 0.00001 seconds
    GPIO.output(TRIG, False)                 #Set TRIG as LOW
    pulse_start = time.time()
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
    distance = round(distance,2)                 #Round to two decimal points
    avgDistance=avgDistance+distance
   avgDistance=avgDistance/5
   print avgDistance
   flag=0
   if avgDistance < 15:      #Check whether the distance is within 15 cm range
      count=count+1
      RobotStop()
      time.sleep(1)
      RobotReverse()
      time.sleep(1.5)
      if (count%3 ==1) & (flag==0):
       RobotRight()
       flag=1
      else:
       RobotLeft()
       flag=0
      time.sleep(1.5)
      RobotStop()
      time.sleep(1)
   else:
      RoboForward()
      flag=0

except KeyboardInterrupt:

# CTRL+C exit, turn off the drives and release GPIO pins
  print "Stopped early, please turn off my power!"
  RobotStop()
  GPIO.cleanup()

