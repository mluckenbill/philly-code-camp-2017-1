from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(17)


#buzzer.on()
#sleep(1)
#buzzer.off()
#sleep(1)


beep_count = 0
total_beeps = 3

while True:
    if beep_count < total_beeps:
        buzzer.off()
        buzzer.beep()
        sleep(1)
        buzzer.off()
        sleep(1)
        beep_count = beep_count + 1
    else:
        buzzer.off()
        print('no more beeps')
        break
