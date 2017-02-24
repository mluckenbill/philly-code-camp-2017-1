from gpiozero import LED
from time import sleep

led = LED(17)

current = 0
total = 3

while True:
    if current <= total:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        current = current + 1
    else:
        print('Turning off lights')
        break;
