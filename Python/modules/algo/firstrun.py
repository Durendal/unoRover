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
		self.lastmove = "forward"
		self.threshold = 30
		self.xbee = None

	def execute(self):
		self.fw.time = time.time()

		self.xbee = self.fw.libs['XBee'].setup(self.serial)

		while True:
			self.SendStr("query: Ultrasonic 0::0")
			time.sleep(0.25)
			rover_recv = xbee.Receive()
			if rover_recv:
				contents = rover_recv[7:-1].decode['ascii']
				print self.fw.printBox("green", "+", "blue") + contents
				self.parseSensorData(contents)
			time.sleep(1)
		
		return True
	# Check if there are any obstructions within 30 cm of the rover
	# if you find anything then we begin an elaborate scheme of turning choices
	# otherwise we stay the course.
	def parseSensorData(self, data):
		data = data.split(":")
		sensortype = data[0].split(" ")[0]
		sensorid = data[0].split(" ")[1]
		deviceid = data[3]
		data = data[4]
		if sensortype == "Ultrasonic":
			if data < self.threshold:
				if self.lastmove == "forward":
					self.turn("right", 90)
					self.lastmove = "right"
				elif self.lastmove == "right":
					self.turn("left", 180)
					self.lastmove = "left"
				elif self.lastmove == "left":
					self.turn("right", 270)
					self.lastmove = "right"
				else:
					if random.randint(0,1) == 0:
						direction = "left"
					else:
						direction = "right"

					self.turn(direction, random.randint(0,360))
			else:
				self.turn("forward", 0)
		elif sensortype == "Light":
			pass
		elif sensortype == "Temp":
			pass
		else:
			pass


	def turn(self, direction, degrees):
		self.xbee.SendStr("command: turn " + degrees + " " + direction)
		print self.fw.printBox("green", "*", "blue") + "Sending[command: turn " + degrees + " " + direction +"]"

	def speed(self, speed):
		self.xbee.SendStr("command: speed " + speed)
		print self.fw.printBox("green", "*", "blue") + "Sending[command: speed " + speed + "]"

	def findSpeed(self):
		self.xbee.SendStr("query: speed")
		print self.fw.printBox("green", "*", "blue") + "Sending[query: speed]"