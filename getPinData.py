#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from firebase import firebase
from datetime import date
import datetime


# Set up Firebase
firebase = firebase.FirebaseApplication('https://tiltsensorarduino.firebaseio.com', None)

# Get number of total beers
result = firebase.get('/beers', None)
total_beers = result['total_beers']
sensor1 = result['Sensor1']
sensor2 = result['Sensor2']


# Get today's date and find JSON section based on beerinfo + #
# If beerinfo1 was on 07/15/16, that is day 1
today = time.strftime("%m/%d/%y")
# Get date formatted a certain way
thedate = datetime.date.today()
first_day = result['Sensor1']['beerinfo1']['date']
print(first_day)

a = date(int(today[6:8]), int(today[0:2]), int(today[3:5]))
b = date(int(first_day[6:8]), int(first_day[0:2]), int(first_day[3:5]))
days_in_between =(a - b).days

i = str(days_in_between)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)


current_state = 0
previous_state = 0
counter = 0


sensor1_pin = 18

# Set name of beer
if sensor1_pin == 18:
    name = "India Pale Ale"


try:
    dailyBeerNum = result['Sensor1']['beerinfo'+i]['beersPerDay']
    firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime':thedate, 'name':name, 'date':today, 'id':int(i), 'beersPerDay': dailyBeerNum})
except Exception as Error:
    firebase.put('beers/Sensor1', ('beerinfo'+i), {'datetime':thedate, 'name':name, 'date':today, 'id':int(i), 'beersPerDay': 0})
    dailyBeerNum = 0

while True:
    sensor1_state = GPIO.input(sensor1_pin)
    
    if sensor1_state == 1:
        print("Tilt sensor value is up")
	time.sleep(1)
	previous_state = sensor1_state
    else:
        print("Tilt sensor value is down")
	if previous_state == sensor1_state:	
	    counter = counter + 1
	previous_state = sensor1_state
	time.sleep(1)
    if counter == 6:
	print("-------------------------")
	print("One beer has been poured!")
	print("         _.._..,_,_")
	print("        (          )")
	print("         ]~,'-\.~~[")
	print("       .=])' (;  ([")
	print("       | ]:: '    [")
	print("       '=]): \.) ([")
	print("         |:: '    |")
	print("          ~~----~")
	print("-------------------------")

	counter = 0
	dailyBeerNum = dailyBeerNum + 1
	total_beers = total_beers + 1
	firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime': thedate, 'beersPerDay': dailyBeerNum, 'name':name, 'date':today, 'id':i})
	firebase.put('beers', 'total_beers', total_beers)

GPIO.cleanup()
