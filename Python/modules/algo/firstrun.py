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
class firstrun:

	def __init__(self, framework):
		
		self.name = "firstrun"
		self.description = "First attempt at a pathing algorithm"
		self.fw = framework
		self.variables = {}
		self.variables['serial'] = {'required' : True, 'description' : 'address of serial port'}
		self.variables['verbose'] = {'required': False, 'description' : 'prints out verbose output'}
		self.lastmove = "forward"
		self.threshold = 30
		self.xbee = None

	def execute(self):
		self.fw.time = time.time()
		
		
		self.fw.libs.XBee.setup(self.serial)
		self.xbee = self.fw.libs.XBee.serial
		self.xbee.write("COMMAND: WRIT MOVE FWD")
		time.sleep(0.5)
		while True:
			rover_recv = self.fw.libs.XBee.getReading("READ ULTRASONIC 0")
			if rover_recv > 0:
				
				if self.verbose.lower() == "true":
					print self.fw.printBox("green", "+", "blue") + rover_recv
					
				if int(rover_recv) < 45:
					
					self.xbee.write("COMMAND: WRIT TURN RGT")
				else:
					self.xbee.write("COMMAND: WRIT MOVE FWD")
				time.sleep(1)
				self.xbee.write("COMMAND: WRIT MOVE STP")
				time.sleep(0.25)
		return True
	