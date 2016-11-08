# https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/

from gpiozero import LED
from time import sleep

# Connect LED to pin 17
led = LED(17)

# Flash LED on/off every 1 second
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
