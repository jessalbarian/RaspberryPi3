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

#------------
# Set up GPIO
#------------
GPIO.setmode(GPIO.BOARD) #BOARD instead of BCM
GPIO.setup(12, GPIO.IN) #Sensor 1
#GPIO.setup(18, GPIO.IN) #Sensor 2


#----------
# Variables
#----------
current_state = -1
previous_state = -1
current_stateS2 = -1
previous_stateS2 = -1
counter = 0
counterS2 = 0
sensor1_pin = 12
sensor2_pin = 18


#---------------------
# Loop for sensor data
#---------------------
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


GPIO.cleanup()
