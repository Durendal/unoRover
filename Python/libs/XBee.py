import serial
from time import sleep

class XBee:
	def __init__(self, framework):
		self.serial = ""
		self.fw = framework

		#self.fw = framework
	   	self.name = 'XBee'
	   	self.description = 'Library to manage XBee communications'
	   	self.reading = 0
				

	def setup(self, ser):
		self.serial = serial.Serial(port=ser, baudrate=9600)

	def getReading(self, read="READ ULTRASONIC 0"):
		self.serial.write(read)
		sleep(0.45)
		data = self.serial.inWaiting()
		msg = ""
		while data:
			chunk = self.serial.read()
			data -= len(chunk)
			if chunk == '\n' or chunk == '\r' or chunk == '':
				break
			msg += chunk
		if msg == "":
			return self.reading
		self.reading = msg
		return msg
		
	def sendCmd(self, cmd):
		if cmd == "FWD":
			self.serial.write("COMMAND: WRIT MOVE FWD")
		elif cmd == "BAC":
			self.serial.write("COMMAND: WRIT MOVE BAC")
		elif cmd == "LFT":
			self.serial.write("COMMAND: WRIT TURN LFT")
		elif cmd == "RGT":
			self.serial.write("COMMAND: WRIT TURN RGT")
		elif cmd == "STP":
			self.serial.write("COMMAND: WRIT MOVE STP")
		elif "READ" in cmd or "TYPE" in cmd or "NUMS" in cmd:
			self.serial.write("COMMAND: "+cmd)