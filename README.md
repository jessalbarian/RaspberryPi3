#RaspberryPi3 Project
Working with a Raspberry Pi 3 and RPI-1031 Tilt-a-Whirl tilt sensors
Installed Raspbian operating system Hooked up GND, 5V, G25 and G26 pins to tilt sensor

<img src="https://github.com/jessalbarian/RaspberryPi3/blob/master/setup.jpg" alt="Raspberry Pi Setup" style="width: 100;"/>

##Update Raspbian OS
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

##Install [WiringPi](http://wiringpi.com/): GPIO Interface Library for the Raspberry Pi
```
$ sudo apt-get install git-core
$ git clone git://git.drogon.net/wiringPi
$ cd wiringPi
$ sudo ./build
```

##***Install Web Server*** Install Apache HTTP server and PHP5 extension
```
$ sudo apt-get install apache2 php5 libapache2-mod-php5
```

##Get the IP Address of your Raspberry Pi
```
$ sudo ifconfig
```

If you type in the IP address into your browser, you should see a start up page from Apache.
Write a python script to get the sensor data as 0 or 1 (up or down) See getPinData.py

##Interact with the Firebase REST API using Ozgur
```
$ sudo pip install requests
$ sudo pip install python-firebase
```

![screen shot]()

![screen shot]()

![screen shot]()
