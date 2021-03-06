# This file is part of the unoRover Framework.
#
#	unoRover is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	unoRover is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with unoRover.  If not, see <http://www.gnu.org/licenses/>.
import time
import os
from serial import *
class manual:

	def __init__(self, framework):
		
		self.name = "Manual"
		self.description = "Manually controlled diagnostic algorithm"
		self.fw = framework
		self.variables = {}
		self.variables['verbose'] = {'required' : False, 'description' : 'prints out the keys the user has entered', 'default' : 'False'}
		self.variables['serial'] = {'required' : True, 'description' : 'address of serial port'}
		self.speed = 200

	def execute(self):
		if self.verbose.lower() == "true":
			verbose = True
		else:
			verbose = False
		try:
			con = Serial(port=self.serial, baudrate=9600)
		except:
			print "Failed to connect to %s be sure it exists and isnt in use." % self.serial
			return False
		print "Prepare yourself foolish mortal:"
		pew = "\x00" #Write 0 into pew so it will pass the initial while condition
		while True:
			# If verbose is set, we need to print out the message every ten millionth iteration
			if verbose:
				recv =  con.inWaiting()
				msg = ""
				while recv:
					chunk = con.read(recv)
					msg += chunk
					recv -= len(chunk)
					time.sleep(0.1)
				
				if len(msg) > 1:
					print msg

			# Break the loop if the user presses esc
			if pew == "\x1b":
				break
			pew = self.fw.libs.Getch.getdatch()
			try:
				if pew.lower() == 'w':
					command = "FWD"
				elif pew.lower() == 's':
					command = "BAC"
				elif pew.lower() == 'a':
					command = "LFT"
				elif pew.lower() == 'd':
					command = "RGT"
				elif pew.lower() == 'f':
					self.speed += 5
					command = "SPD " + str(self.speed)
				elif pew.lower() == 'v':
					self.speed -= 5
					command = "SPD " + str(self.speed)
				else:
					command = "STP"

				con.write(command)
			except:
				print "Error writing to serial. Terminating."
				return False
			print pew
		print "Other Barry says: later tater"
		return True
