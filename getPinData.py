#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from firebase import firebase
from datetime import date
import datetime



#----------------
# Set up Firebase
#----------------
firebase = firebase.FirebaseApplication('https://tiltsensorarduino.firebaseio.com', None)



#--------------------------
# Get number of total beers
#--------------------------
result = firebase.get('/beers', None)
total_beers = result['total_beers']



#------------
# Set up date
#------------
today = time.strftime("%m/%d/%y")
beertime = time.strftime("%H:%M:%S")


# Get date formatted a specific way
thedate = datetime.date.today()

# Getting first database entry for date
first_day = result['Sensor1']['beerinfo1']['date']
first_dayS2 = result['Sensor2']['beerinfo1']['date']

# Calculate days in between to get value i and j
a = date(int(today[6:8]), int(today[0:2]), int(today[3:5]))

b1 = date(int(first_day[6:8]), int(first_day[0:2]), int(first_day[3:5]))
b2 = date(int(first_dayS2[6:8]), int(first_dayS2[0:2]), int(first_dayS2[3:5]))
days_in_betweenS1 =(a - b1).days
days_in_betweenS2 =(a - b2).days

if days_in_betweenS2 == 1:
    days_in_betweenS2 = days_in_betweenS2 + 1
if days_in_betweenS1 == 1:
    days_in_betweenS1 = days_in_betweenS1 + 1
i = str(days_in_betweenS1)
j = str(days_in_betweenS2)


#------------
# Set up GPIO
#------------
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN) #Sensor 1
GPIO.setup(18, GPIO.IN) #Sensor 2



#----------
# Variables
#----------
current_state = 0
previous_state = 0
current_stateS2 = 0
previous_stateS2 = 0
counter = 0
counterS2 = 0
sensor1_pin = 12
sensor2_pin = 18


#-------------------------------
# Create new objects to database
#-------------------------------
try:
    dailyIPANum = result['Sensor1']['beerinfo'+i]['beersPerDay']
    firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime':thedate, 'name': 'India Pale Ale', 'date':today, 'id':int(i), 'beersPerDay': dailyIPANum, 'beertimes' :{'beer'+i:beertime}})

except Exception as Error:
    firebase.put('beers/Sensor1', ('beerinfo'+i), {'datetime':thedate, 'name':'India Pale Ale', 'date':today, 'id':int(i), 'beersPerDay': 0, 'beertimes' :{'beer'+i:beertime}})
    dailyIPANum = 0


try:
    dailyPorterNum = result['Sensor2']['beerinfo'+j]['beersPerDay']
    firebase.put('beers/Sensor2', 'beerinfo'+j, {'datetime':thedate, 'name': 'Chocolate Porter', 'date':today, 'id': int(j), 'beersPerDay': dailyPorterNum, 'beertimes' : {'beer'+i:beertime}})

except Exception as Error:
    firebase.put('beers/Sensor2', ('beerinfo'+j), {'datetime':thedate, 'name':'Chocolate Porter', 'date':today, 'id':int(j), 'beersPerDay': 0, 'beertimes' :{'beer'+i:beertime}})
    dailyPorterNum = 0

#----------------
# Loop for sensor
#----------------
while True:
    sensor1_state = GPIO.input(sensor1_pin)
    sensor2_state = GPIO.input(sensor2_pin)

    if sensor2_state == 1:
	print("Sensor2 value is up")
	time.sleep(1)
	previous_stateS2 = sensor2_state
    else:
	print("Sensor2 value is down")
	if previous_stateS2 == sensor2_state:
	    counterS2 = counterS2 + 1
	previous_stateS2 = sensor2_state
	time.sleep(1)

    if sensor1_state == 1:
        print("Sensor1 value is up")
	time.sleep(1)
	previous_state = sensor1_state
    else:
        print("Sensor1 value is down")
	if previous_state == sensor1_state:	
	    counter = counter + 1
	previous_state = sensor1_state
	time.sleep(1)

    if counter == 3:
	print("----------------------")
	print("Sensor1 poured a beer!")
	print("----------------------")
	counter = 0
	dailyIPANum = dailyIPANum + 1
	total_beers = total_beers + 1

    if counterS2 == 3:
	print("----------------------")
	print("Sensor2 poured a beer!")
	print("----------------------")
	counterS2 = 0
	dailyPorterNum = dailyPorterNum + 1
	total_beers = total_beers + 1

	firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime': thedate, 'beersPerDay': dailyIPANum, 'name':'India Pale Ale', 'date':today, 'id':i, 'beertimes' :{'beer'+i:beertime}})
	firebase.put('beers/Sensor2', 'beerinfo'+j, {'datetime': thedate, 'beersPerDay': dailyPorterNum, 'name':'Chocolate Porter', 'date':today, 'id':j, 'beertimes' :{'beer'+i:beertime}})
	firebase.put('beers', 'total_beers', total_beers)


GPIO.cleanup()
