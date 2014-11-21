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

class test:

	def __init__(self, framework):
		
		self.name = "Test"
		self.description = "A test module for the python framework"
		self.fw = framework
		self.variables = {}
		self.variables['message'] = {'required' : False, 'description' : 'String to modify', 'default' : 'This is a test string'}


	def execute(self):

		self.test()

		return True

	def test(self):
		string = self.message
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+self.fw.libs.text.warpText(string)

		hexstr = self.fw.libs.text.strHex(string)
		print "\t"+self.fw.printBox("blue", "+", "green")+"Hex: " +hexstr
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+"And back again: " + self.fw.libs.text.hexStr(hexstr)

		base64 = self.fw.libs.text.strBase64(string)
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+"Base 64: " + base64
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+"And back again: " + self.fw.libs.text.base64Str(base64)

		rot13 = self.fw.libs.text.strRot13(string)
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+"ROT13: " + rot13
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+"And back again: " + self.fw.libs.text.rot13Str(rot13)	

		spaces = "This is a test+string+with+several different types+of+spaces"	
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+"Space substitutions: " +spaces
		print "\t"+self.fw.libs.colours.cstring("[", "green")+self.fw.libs.colours.cstring("+","blue")+self.fw.libs.colours.cstring("] ", "green")+self.fw.libs.text.sqlSpace(spaces)

		return True
