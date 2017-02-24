from gpiozero import Button, LED

button = Button(21)
led = LED(25)

#step 1
##while True:
##        button.wait_for_press()
##        led.on()
##        print("Pressed")
##        button.wait_for_release()
##        led.off()
##        print("Released")

#step 2
##while True:
##    led.on()
##    button.wait_for_press()
##    led.off()
##    button.wait_for_release()
    
#step 3
while True:
        led.blink()
        button.wait_for_press()
        led.off()
        button.wait_for_release()

#step 4: Blink Parameters
##led.blink(2, 2) - 2 seconds on, 2 seconds off
##led.blink(0.5, 0.5) - half a second on, half a second off
##led.blink(0.1, 0.2) - one tenth of a second on, one fifth of a second off
