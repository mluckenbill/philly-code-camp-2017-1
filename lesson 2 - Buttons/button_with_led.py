import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

# here we complete the circuit when the button is pushed  we do this on GPIO Pin 2
# key to note is normally 3.3V is sent out of GPIO pins
# however, each GPIO pin has software configurable pull-up and pull-down resistors.

# When using a GPIO pin as an input, you can configure these resistors
# so that one or either or neither of the resistors is enabled, using the optional pull_up_down parameter to GPIO.setup

# If it is set to GPIO.PUD_UP, the pull-up resistor is enabled; if it is set to GPIO.PUD_DOWN, the pull-down resistor is enabled.
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

light_switch_on = False

def led_on():
        
        GPIO.output(17, GPIO.HIGH)
def led_off():
        
        GPIO.output(17, GPIO.LOW)


try:
        print ('Press ctrl+c to exit')

        while True:
                input_state = GPIO.input(2)

                if input_state == False:
                        
                        print('Button Pressed')

                        time.sleep(0.2)
                        
                        if light_switch_on == False:
                                led_on()
                                light_switch_on = True
                        else:
                                led_off()
                                light_switch_on = False
except KeyboardInterrupt:
        print("Turning off the lights now")
        led_off()
        GPIO.cleanup()
