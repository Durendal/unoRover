unoRover Python Framework v0.01-alpha
=====================================

Based on the OpenWire python Framework I've built the unoRover package to handle navigation and diagnostics of an arduino based rover

To run this version of unoRover simply run:

chmod +x unoRover
./unoRover

or you can type 

python unoRover

directly.

**Important**

This program MUST be run through python v2.7, earlier versions 
do not support ternary operations and as such you will receive a syntax 
error. It is also not compatible with python v3.x.

Python Dependencies:

	colorama   - https://pypi.python.org/pypi/colorama
	pyserial   - https://pypi.python.org/pypi/pyserial
	pyreadline - https://pypi.python.org/pypi/pyreadline


Extract the Arduino folder to C:\yourusername\My Documents\Arduino(or wherever your sketch directory is) it will add
the required libraries as well as the rover sketch. At the moment it is set to work with a Serial connection over USB using w, a, s, and d to control it. Support for XBee wireless communication will soon be added.
	

Special Thanks:
	
	some code in this project has been borrowed with extreme gratitude from the following sources: 
	Getch.py - http://code.activestate.com/recipes/134892/ Written by Danny Yoo
	XBee.py - https://github.com/serdmanczyk/XBee_802.15.4_APIModeTutorial written by Steven Erdmanczyk Jr
	XBee.h - https://github.com/serdmanczyk/XBee_802.15.4_APIModeTutorial written by Steven Erdmanczyk Jr
	XBee.cpp - https://github.com/serdmanczyk/XBee_802.15.4_APIModeTutorial written by Steven Erdmanczyk Jr
	queue.h - https://github.com/serdmanczyk/XBee_802.15.4_APIModeTutorial written by Steven Erdmanczyk Jr
	queue.cpp - https://github.com/serdmanczyk/XBee_802.15.4_APIModeTutorial written by Steven Erdmanczyk Jr
	AFMotor.h - https://github.com/adafruit/Adafruit-Motor-Shield-library written by Adafruit
	AFMotor.cpp -  - https://github.com/adafruit/Adafruit-Motor-Shield-library written by Adafruit
