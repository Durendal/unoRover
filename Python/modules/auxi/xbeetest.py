# This file is part of the unoRover Framework.
#
#    unoRover is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    unoRover is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with unoRover.  If not, see <http://www.gnu.org/licenses/>.

import time
import random
from serial import *
from time import sleep

class xbeetest:

	def __init__(self, framework):
		
		self.name = "XBeeTest"
		self.description = "Testing XBee Wireless Communications"
		self.fw = framework
		self.variables = {}
		self.variables['serial'] = {'required' : True, 'description' : 'address of serial port'}

	def execute(self):
		self.fw.time = time.time()
	
		con = Serial(port=self.serial, baudrate=9600)
		while True:
			sleep(0.5)
			remaining = con.inWaiting()
			if remaining < 1:
				msg = raw_input("\t" + self.fw.cstring("Enter some text: ", "green"))

				if msg.lower() == 'exit' or msg.lower() == 'quit':
					break
				con.write(msg)
			else:
				msg = ""
				while remaining:
					chunk = con.read(remaining)
					msg += chunk
					remaining -= len(chunk)
				if len(msg) > 0:
					print "\t"+self.fw.cstring("Returned Message:", "green"), self.fw.cstring(msg, "blue")
		
		print self.fw.cstring("\nUser quitting... big quitter... *smirk*", "red")
		return True
	