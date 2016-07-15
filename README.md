# RaspberryPi3 Project
Working with a Raspberry Pi 3 and RPI-1031 Tilt-a-Whirl tilt sensors


Installed Raspbian operating system
Hooked up GND, 5V, G25 and G26 pins to tilt sensor


<img src="https://github.com/jessalbarian/RaspberryPi3/blob/master/setup.jpg?raw=true =" width="350" />


**Update Raspbian OS**
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

**Install [WiringPi](http://wiringpi.com/): GPIO Interface Library for the Raspberry Pi**
```
$ sudo apt-get install git-core
$ git clone git://git.drogon.net/wiringPi
$ cd wiringPi
$ sudo ./build
```

**Check to see if the pi is reading in the pins correctly**
```
$ gpio read 18
$ gpio read 19
```
18 should output 1, 19 should output to 0
Note: I have my tilt sensor connected to GPIO pins 18 and 19

**Install Web Server**
Install Apache HTTP server and PHP5 extension
```
$ sudo apt-get install apache2 php5 libapache2-mod-php5
```

**Get the IP Address of your Raspberry Pi**
```
$ sudo ifconfig
```
If you type in the IP address into your browser, you should see a start up page from Apache.

**Write a python script to get the sensor data as 0 or 1 (up or down)**
```python
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(19, GPIO.IN)

state = 0
while True:
    state = GPIO.input(18)
    if state == 1:
        print("Tilt sensor is up")
	time.sleep(1)
    else:
        print("Tilt sensor is down")
	time.sleep(1)

GPIO.cleanup()
```








