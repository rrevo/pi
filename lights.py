#!/usr/bin/env python3

import time
import RPi.GPIO as GPIO
import syslog

PIN = 11 # GPIO 17
MIN_HOUR = 17
MAX_HOUR = 23

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

hour = int(time.strftime("%H"))

message = None
if hour >= MIN_HOUR and hour < MAX_HOUR:
    message = 'ON'
    GPIO.output(PIN, GPIO.HIGH)
else:
    message = 'OFF'
    GPIO.output(PIN, GPIO.LOW)

print(message)
syslog.syslog(message)

