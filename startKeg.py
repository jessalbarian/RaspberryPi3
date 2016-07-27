#!/usr/bin/env python

import time
from firebase import firebase



#----------------
# Set up Firebase
#----------------
firebase = firebase.FirebaseApplication('https://madesensors.firebaseio.com/', None)
tap1 = firebase.get('/tap1', None)
tap2 = firebase.get('/tap2', None)

check = True
check2 = True

while check2:
    user_input1 = raw_input("Are you replacing the Coffee or Beer keg? (C/B): ")
    if user_input1 == 'C' or user_input1 == 'c':	
        keg = "coffee"
        check2 = False
    elif user_input1 == 'B' or user_input1 == 'b':
  	keg = "beer"
	check2 = False
    else:
	print("Please enter C or B.")

while check:
    user_input2 = raw_input("Enter gallons of keg: ")
    try:
        val = float(user_input2)
	time = time.strftime("%m/%d/%Y %H:%M:%S")
	check = False	
    except ValueError:
        print("Please enter a number.")
    
if keg == "beer":
    firebase.put('tap1', 'current_keg', {'start_time': time, 'amount': user_input2})
elif keg == "coffee":
    firebase.put('tap2', 'current_keg', {'start_time': time, 'amount': user_input2})
