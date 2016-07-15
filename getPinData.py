#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

beer_count = 0
current_state = 0
previous_state = 0
start = 0
counter = 0
beerNum = 0

while True:
    current_state = GPIO.input(18)

    if current_state == 1:
        print("Tilt sensor value is up")
	time.sleep(1)
	previous_state = current_state
    else:
        print("Tilt sensor value is down")
	if previous_state == current_state:	
	    counter = counter + 1
	previous_state = current_state
	time.sleep(1)
    if counter == 6:
	print("-------------------------")
	print("One beer has been poured!")
	print("")
	print("         _.._..,_,_")
	print("        (          )")
	print("         ]~,'-\.~~[")
	print("       .=])' (;  ([")
	print("       | ]:: '    [")
	print("       '=]): \.) ([")
	print("         |:: '    |")
	print("          ~~----~")
	counter = 0
	beerNum = beerNum + 1

GPIO.cleanup()
