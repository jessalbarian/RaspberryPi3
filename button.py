import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN)
buttonPin = 3

prev_input = 0
'''
while True:
  input = GPIO.input(3)
  if ((not prev_input) and input):
    print("Button pressed")
  prev_input = input
  time.sleep(0.05)
'''
while True:
  #assuming the script to call is long enough we can ignore bouncing
  if (GPIO.input(buttonPin)):
    #this is the script that will be called (as root)
    os.system("python /home/pi/Desktop/RaspberryPi3/getPinData.py")
