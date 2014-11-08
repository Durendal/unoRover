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
import socket
import subprocess
import time

class pscan:

	def __init__(self, framework):
		
		self.name = "pScan"
		self.description = "A simple port scanner"
		self.fw = framework
		self.variables = {}
		self.variables['portrange'] = {'required' : False, 'description' : 'Ports to scan', 'default' : '0-1000'}
		self.variables['verbose'] = {'required' : False, 'description' : 'Outputs ports that failed to connect', 'default' : 'False'}
		self.variables['target'] = {'required' : True, 'description' : 'Target hostname or IP Address to scan'}
		

	def execute(self):

		self.fw.time = time.time()
		if self.fw.os == 'posix':
			ret = subprocess.call("ping -c 1 %s" % self.target, shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
		else:
			ret = subprocess.call("ping -n 1 %s" % self.target, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		if ret == 0:
			print self.fw.printBox("green")+"%s: is up, Performing portscan." % self.target
		else:
			print self.fw.printBox("red")+"%s: is not up, cannot scan ports." % self.target
			return False
		self.scan(socket.gethostbyname(self.target))

		print self.fw.printBox("blue")+" Scan finished in: " + self.fw.getExecutionTime(True)
		return True

	def scan(self, ip):

		print self.fw.printBox("blue")+self.fw.libs.colours.cstring("Open Ports in range: ", "blue"),
		print self.fw.libs.colours.cstring(self.portrange, "green")
				
		if ',' in self.portrange:
			ports = self.portrange.split(",")
			for port in ports:
				self.connect(ip, int(port))
			return True
		elif '-' in self.portrange:
			ports = self.portrange.split("-")
			start = ports[0]
			stop = int(ports[1])+1
		else:
			self.connect(ip, int(self.portrange))
			return True
		if self.verbose.lower() != "true" and self.verbose.lower() != "false":
			print self.fw.printBox("red", "-")+"Invalid value specified for verbose variable. Reset this value and try again."
			return True

		for i in range(int(start), int(stop)):
			self.connect(ip, i)

		return True

	def connect(self, ip, i):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect((ip, i))
			print "\t"+self.fw.printBox("blue", "+")+self.fw.libs.colours.cstring(ip, "yellow")+self.fw.libs.colours.cstring(":", "green")+self.fw.libs.colours.cstring(str(i), "yellow")

			s.close()
		except:
			if self.verbose.lower() == "true":
				print "\t"+self.fw.printBox("yellow", "-")+self.fw.libs.colours.cstring(ip, "yellow")+self.fw.libs.colours.cstring(":", "green")+self.fw.libs.colours.cstring(str(i), "yellow")				
			pass
		
		
