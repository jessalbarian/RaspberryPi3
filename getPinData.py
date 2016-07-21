#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from firebase import firebase



#----------------
# Set up Firebase
#----------------
firebase = firebase.FirebaseApplication('https://madesensors.firebaseio.com/', None)
tap1 = firebase.get('/tap1', None)
tap2 = firebase.get('/tap2', None)
try:
    i = firebase.get('/tap1/times', None)
    i = len(i)-1
except Exception as Error:
    i = 1
try:
    j = firebase.get('/tap2/times', None)
    j = len(j)-1
except Exception as Error:
    j = 1


#------------
# Set up GPIO
#------------
GPIO.setmode(GPIO.BOARD) #BOARD instead of BCM
GPIO.setup(12, GPIO.IN) #Sensor 1
GPIO.setup(18, GPIO.IN) #Sensor 2


#----------
# Variables
#----------
current_state = 0
previous_state = 1
current_stateS2 = 0
previous_stateS2 = 1
counter = 0
counterS2 = 0
sensor1_pin = 12
sensor2_pin = 18


#---------------------
# Loop for sensor data
#---------------------
while True:
    sensor1_state = GPIO.input(sensor1_pin)
    sensor2_state = GPIO.input(sensor2_pin)

    if sensor1_state == 1:
        print("Sensor1 value is up")
	time.sleep(1)
	previous_state = sensor1_state
    else:
        print("Sensor1 value is down")
	if previous_state == sensor1_state:	
	    counter = counter + 1
	if counter == 1:
	    start_timeS1 = time.strftime("%m/%d/%y %H:%M:%S")
	    print(start_timeS1)
	previous_state = sensor1_state
	time.sleep(1)

    if sensor2_state == 1:
	print("Sensor2 value is up")
	time.sleep(1)
	previous_stateS2 = sensor2_state
    else:
	print("Sensor2 value is down")
	if previous_stateS2 == sensor2_state:
	    counterS2 = counterS2 + 1
	if counterS2 == 1:
    	    start_timeS2 = time.strftime("%m/%d/%y %H:%M:%S")
	    print(start_timeS2)
	previous_stateS2 = sensor2_state
	time.sleep(1)

    # If 6 seconds has passed, 1 beer has been poured
    if counter == 3:
	stop_timeS1 = time.strftime("%m/%d/%y %H:%M:%S")
	print("----------------------")
	print("Sensor1 poured a beer!")
	print("----------------------")
	counter = 0
	try:
            firebase.put('tap1', 'times/'+str(i), {'start_time': start_timeS1, 'stop_time': stop_timeS1})
        except Exception as Error:
            firebase.put('tap1', 'times/'+str(i), {'start_time': "", 'stop_time': ""})
        i = i + 1    
    if counterS2 == 3:
	stop_timeS2 = time.strftime("%m/%d/%y %H:%M:%S")
	print("----------------------")
	print("Sensor2 poured a beer!")
	print("----------------------")
	counterS2 = 0
        try:
            firebase.put('tap2', 'times/'+str(j), {'start_time': start_timeS2, 'stop_time': stop_timeS2})
        except Exception as Error:
            firebase.put('tap2', 'times/'+str(j), {'start_time': "", 'stop_time': ""})
        j = j + 1
"""
    try:
        firebase.put('tap1', 'times/'+str(i), {'start_time': start_timeS1, 'stop_time': stop_timeS1})
        firebase.put('tap2', 'times/'+str(i), {'start_time': start_timeS2, 'stop_time': stop_timeS2})
	print("try")
    except Exception as Error:
	firebase.put('tap1', 'times/'+str(i), {'start_time': "", 'stop_time': ""})
        firebase.put('tap2', 'times/'+str(i), {'start_time': "", 'stop_time': ""})	
	print("catch")
"""

#	firebase.put('beers/Sensor2', 'beerinfo'+j, {'datetime': thedate, 'beersPerDay': dailyPorterNum, 'name':'Chocolate Porter', 'date':today, 'id':j, 'beertimes' : beerTimesS2})
	
#        firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime': thedate, 'beersPerDay': dailyPorterNum, 'name':'Chocolate Porter', 'date':today, 'id':i, 'beertimes' : beerTimesS1})


        #firebase.put('beers/Sensor2', 'beerinfo'+j, {'datetime': thedate, 'beersPerDay': dailyPorterNum, 'name':'Chocolate Porter', 'date':today, 'id':j, 'beertimes' :{'beer'+str(n):beertimeS2}})
 #       firebase.put('beers', 'total_beers', total_beers)

GPIO.cleanup()
