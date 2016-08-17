import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN)
buttonPin = 3

while True:
  #assuming the script to call is long enough we can ignore bouncing
  if (GPIO.input(buttonPin)):
    #this is the script that will be called (as root)
    os.system("python /home/pi/Desktop/RaspberryPi3/getPinData.py")
