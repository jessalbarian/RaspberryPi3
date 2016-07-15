#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.IN)

num = 0
while True:
    num = GPIO.input(18)
    if num == 1:
        print("Tilt sensor is up")
    else:
        print("Tilt sensor is down")

GPIO.cleanup()
