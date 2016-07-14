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

Installed [WiringPi](http://wiringpi.com/): GPIO Interface Library for the Raspberry Pi
```
$ sudo apt-get install git-core
$ git clone git://git.drogon.net/wiringPi
$ cd wiringPi
$ git pull origin
$ cd wiringPi
$ ./build
```
