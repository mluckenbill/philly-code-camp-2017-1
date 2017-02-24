from gpiozero import Button, TrafficLights, Buzzer
from time import sleep
lights = TrafficLights(25, 8, 7)
button = Button(21)
buzzer = buzzer(15)


# step 1 - Adding a buzzer
while True:
    lights.on()
    buzzer.off()
    button.wait_for_press()
    lights.off()
    buzzer.on()
    button.wait_for_release()

#step 2 - Adding a buzzer
while True:
    lights.blink()
    buzzer.beep()
    button.wait_for_press()
    lights.off()
    buzzer.off()
    button.wait_for_release()

#step 3 - Adding Traffic Light Sequence
while True:
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()


#step 4 - Refactor Traffic Light Sequence
while True:
    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()
