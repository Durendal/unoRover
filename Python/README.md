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
	

Special Thanks:
	
	some code in this project has been borrowed with extreme gratitude from the following sources: 
	Getch.py is based on: http://code.activestate.com/recipes/134892/ Written by Danny Yoo
	XBee.py is based on: https://github.com/serdmanczyk/XBee_802.15.4_APIModeTutorial written by Steven Erdmanczyk Jr