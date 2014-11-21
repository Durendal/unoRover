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
		self.variables['serial'] = {'required' : True, 'description' : 'address of serial port'}
		
		

	def execute(self):
		try:
			con = Serial(port=self.serial, baudrate=9600)
		except:
			print "Failed to connect to %s be sure it exists and isnt in use." % self.serial
			return False
		print "Prepare yourself foolish mortal:"
		pew = "\x00" #Write 0 into pew so it will pass the initial while condition
		while True:
			# Break the loop if the user presses esc
			if pew == "\x1b":
				break
			pew = self.fw.libs.Getch.getdatch()
			con.write(pew)
			print pew
		print "Other Barry says: later tater"
		return True