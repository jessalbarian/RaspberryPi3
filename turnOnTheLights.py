#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
print "LED on"

GPIO.output(24, GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(24,GPIO.LOW)



GPIO.cleanup()
