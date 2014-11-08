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
	