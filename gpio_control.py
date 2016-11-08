# https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/

from gpiozero import LED, Button
from time import sleep

# Connect LED in pin 17
led = LED(17)

# Button is connected in pin 2
button = Button(2)

while True:
    # Wait for button press
    button.wait_for_press():
    # Turn on LED for 3 secs
    led.on()
    sleep(3)
    led.off()

