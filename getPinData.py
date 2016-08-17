#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from firebase import firebase



#----------------
# Set up Firebase
#----------------
<<<<<<< HEAD
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
try:
    k = firebase.get('/tap1/alltimes', None)
    k = len(k)-1
except Exception as Error:
    k = 1
try:
    l = firebase.get('/tap2/alltimes', None)
    l = len(l)-1
except Exception as Error:
    l = 1
=======
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

# Get date formatted a specific way
thedate = datetime.date.today()

# Getting first database entry for date
first_day = result['Sensor1']['beerinfo1']['date']
first_dayS2 = result['Sensor2']['beerinfo1']['date']

# Calculate days in between to get value i
a = date(int(today[6:8]), int(today[0:2]), int(today[3:5]))

b1 = date(int(first_day[6:8]), int(first_day[0:2]), int(first_day[3:5]))
b2 = date(int(first_dayS2[6:8]), int(first_dayS2[0:2]), int(first_dayS2[3:5]))
days_in_betweenS1 =(a - b1).days
days_in_betweenS2 =(a - b2).days
i = str(days_in_betweenS1)
j = str(days_in_betweenS2)

>>>>>>> parent of 42d1194... added beer time


#------------
# Set up GPIO
#------------
<<<<<<< HEAD
GPIO.setmode(GPIO.BOARD) #BOARD instead of BCM
GPIO.setup(12, GPIO.IN) #Sensor 1
#GPIO.setup(18, GPIO.IN) #Sensor 2
=======
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) #Sensor 1
GPIO.setup(22, GPIO.IN) #Sensor 2

>>>>>>> parent of 42d1194... added beer time


#----------
# Variables
#----------
current_state = -1
previous_state = -1
current_stateS2 = -1
previous_stateS2 = -1
counter = 0
counterS2 = 0
sensor1_pin = 18
sensor2_pin = 22


<<<<<<< HEAD
#---------------------
# Loop for sensor data
#---------------------
=======
#-------------------------------
# Create new objects to database
#-------------------------------
try:
    dailyIPANum = result['Sensor1']['beerinfo'+i]['beersPerDay']
    dailyPorterNum = result['Sensor2']['beerinfo'+j]['beersPerDay']
    firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime':thedate, 'name': 'India Pale Ale', 'date':today, 'id':int(i), 'beersPerDay': dailyIPANum})
    firebase.put('beers/Sensor2', 'beerinfo'+j, {'datetime':thedate, 'name': 'Chocolate Porter', 'date':today, 'id': int(j), 'beersPerDay': dailyPorterNum})

except Exception as Error:
    firebase.put('beers/Sensor1', ('beerinfo'+i), {'datetime':thedate, 'name':'India Pale Ale', 'date':today, 'id':int(i), 'beersPerDay': 0})
    firebase.put('beers/Sensor2', ('beerinfo'+j), {'datetime':thedate, 'name':'Chocolate Porter', 'date':today, 'id':int(j), 'beersPerDay': 0})
    dailyIPANum = 0
    dailyPorterNum = 0

try:

#----------------
# Loop for sensor
#----------------
>>>>>>> parent of 42d1194... added beer time
while True:
    sensor1_state = GPIO.input(sensor1_pin)
 #   sensor2_state = GPIO.input(sensor2_pin)

    if sensor1_state == 1:
        print("Sensor1 value is up")
	#if previous_state == 0:
            #try:
             #   firebase.put('tap1', 'alltimes/'+str(k), {'start_time': start1, 'stop_time': stop1})
            #except Exception as Error:
            #    firebase.put('tap1', 'alltimes/'+str(k), {'start_time': "", 'stop_time': ""})
            #k = k + 1
	    #start1 = None
	    #stop1 = None
	previous_state = sensor1_state
	time.sleep(1)
    else:
        print("Sensor1 value is down")
	if previous_state == sensor1_state or previous_state == -1:	
	    counter = counter + 1
	if counter == 1:
	    start_timeS1 = time.strftime("%m/%d/%Y %H:%M:%S")
	    print(start_timeS1)
	    #start1 = time.strftime("%m/%d/%Y %H:%M:%S")
	previous_state = sensor1_state
	time.sleep(1)

  #  if sensor2_state == 1:
#	print("Sensor2 value is up")
	#if previous_stateS2 == 0:
            #stop2 = time.strftime("%m/%d/%Y %H:%M:%S")
	    #print(stop2)
            #try:
             #   firebase.put('tap2', 'alltimes/'+str(l), {'start_time': start2, 'stop_time': stop2})
            #except Exception as Error:
            #    firebase.put('tap2', 'alltimes/'+str(l), {'start_time': "", 'stop_time': ""})
            #l = l + 1
	    #start2 = None
	    #stop2 = None
#	previous_stateS2 = sensor2_state
#	time.sleep(1)
 #   else:
#	print("Sensor2 value is down")
#	if previous_stateS2 == sensor2_state or previous_stateS2 == -1:
#	    counterS2 = counterS2 + 1
#	if counterS2 == 1:
 #   	    start_timeS2 = time.strftime("%m/%d/%Y %H:%M:%S")
#	    print(start_timeS2)
	    #start2 = time.strftime("%m/%d/%Y %H:%M:%S")
#	previous_stateS2 = sensor2_state
#	time.sleep(1)
    

    # If 6 seconds has passed, 1 beer has been poured
    if counter == 6:
	stop_timeS1 = time.strftime("%m/%d/%Y %H:%M:%S")
	print("----------------------")
	print("Sensor1 poured a beer!")
	print("----------------------")
	counter = 0
<<<<<<< HEAD
	try:
            firebase.put('tap1', 'times/'+str(i), {'start_time': start_timeS1, 'stop_time': stop_timeS1})
        except Exception as Error:
            firebase.put('tap1', 'times/'+str(i), {'start_time': "", 'stop_time': ""})
        i = i + 1    
#    if counterS2 == 3:
#	stop_timeS2 = time.strftime("%m/%d/%Y %H:%M:%S")
#	print("----------------------")
#	print("Sensor2 poured a beer!")
#	print("----------------------")
#	counterS2 = 0
 #       try:
  #          firebase.put('tap2', 'times/'+str(j), {'start_time': start_timeS2, 'stop_time': stop_timeS2})
#        except Exception as Error:
 #           firebase.put('tap2', 'times/'+str(j), {'start_time': "", 'stop_time': ""})
  #      j = j + 1
=======

    if counterS2 == 3:
	print("----------------------")
	print("Sensor2 poured a beer!")
	print("----------------------")
	counterS2 = 0
	
	dailyIPANum = dailyIPANum + 1
	dailyPorterNum = dailyPorterNum + 1
	total_beers = total_beers + 1

	firebase.put('beers/Sensor1', 'beerinfo'+i, {'datetime': thedate, 'beersPerDay': dailyIPANum, 'name':'India Pale Ale', 'date':today, 'id':i})
	firebase.put('beers/Sensor2', 'beerinfo'+j, {'datetime': thedate, 'beersPerDay': dailyPorterNum, 'name':'Chocolate Porter', 'date':today, 'id':j})
	firebase.put('beers', 'total_beers', total_beers)
>>>>>>> parent of 42d1194... added beer time


GPIO.cleanup()
