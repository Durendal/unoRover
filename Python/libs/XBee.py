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
	   	self.commands = { 'ENDMSG' : 0x00, 
	   					  'FWD' : 0x01, 
	   					  'BAC' : 0x02,
	   					  'STP' : 0x03,
	   					  'LFT' : 0x04,
	   					  'RGT' : 0x05,
	   					  'GSP' : 0x06,
	   					  'SPD' : 0x07,
	   					  'READ' : 0x08,
	   					  'TYPS' : 0x09,
	   					  'NUMS' : 0x0A
	   					}
				

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
		cmd = cmd.split(" ")
		if cmd[0] == "FWD":
			self.serial.write(self.commands['FWD'])
		elif cmd[0] == "BAC":
			self.serial.write(self.commands['BAC'])
		elif cmd[0] == "LFT":
			self.serial.write(self.commands['LFT'])
		elif cmd[0] == "RGT":
			self.serial.write(self.commands['RGT'])
		elif cmd[0] == "STP":
			self.serial.write(self.commands['STP'])
		elif cmd[0] == "NUMS":
			self.serial.write(self.commands['NUMS'])
		elif "READ" == cmd[0]:
			self.serial.write(self.commands['READ'])
			self.serial.write(cmd[1])
			self.serial.write(cmd[2])
		elif "TYPS" == cmd[0]:
			self.serial.write(self.commands['TYPS'])
			self.serial.write(cmd[1])
		elif "GSP" == cmd[0]:
			self.serial.write(self.commands['GSP'])
		elif "SPD" == cmd[0]:
			self.serial.write(self.commands['SPD'])
			self.serial.write(cmd[1])
		self.serial.write(self.commands['ENDMSG'])