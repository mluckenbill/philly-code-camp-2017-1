from gpiozero import Button, TrafficLights

# note 25 is GPIO Pin 25, 8 is GPIO 8 and etc
lights = TrafficLights(25, 8, 7)
button = Button(21)


# step 1
while True:
    button.wait_for_press()
    lights.on()
    button.wait_for_release()
    lights.off()

# step 2

while True:
    lights.blink()
    button.wait_for_press()
    lights.off()
    button.wait_for_release()
