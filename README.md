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

**Turn on pin locations on pin 1 and 3** (1 is ON, 0 is OFF)
```
$ gpio mode 1 out
$ gpio mode 3 out
$ gpio write 1 1
```
**Check to see if the pi is reading in the pins correctly**
```
$ gpio read 2
$ gpio read 4
```
These should output 1 instead of 0, meaning they are on

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










