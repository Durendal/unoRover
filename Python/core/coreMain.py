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


class coreMain:
	
	def __init__(self, framework):
		self.fw = framework
		self.name = 'Main'
		self.description = 'Main Framework Functions'
	
		# Print banner
	def outputHeader(self):

		self.fw.clearScreen()
		banner = """
                  ______                    
                  | ___ \                   
 _   _ _ __   ___ | |_/ /_____   _____ _ __ 
| | | | '_ \ / _ \|    // _ \ \ / / _ \ '__|
| |_| | | | | (_) | |\ \ (_) \ V /  __/ |   
 \__,_|_| |_|\___/\_| \_\___/ \_/ \___|_|   
                                            
                                            
		 """
		print self.fw.cstring(banner, "cyan")
		print "unoRover Arduino Rover Management Software"
		print "Based on OpenWire Framework By Brian Hewitt"
		print ""
		print "type 'help' to see a list of commands"
	
		return True

	# Print Help Message
	def showUsage(self):

		print self.fw.libs.colours.cstring("""
	unoRover Rover 0.01-alpha
	List of commands and description of usage""", "white")
		
		print self.fw.cstring("\thelp", "green")  +   self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Display this list" , "white", None, "dark")
		print self.fw.cstring("\tclear/cls", "green")  +  self.fw.cstring(" - " , "red", None, "bright")+self.fw.cstring( "Clears the Screen", "white", None, "dark")
		print self.fw.cstring("\tlibs", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring( "List current libraries", "white", None, "dark")
		print self.fw.cstring("\tbanner", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Displays the Banner" , "white", None, "dark")
		print self.fw.cstring("\tlist", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("List currently installed modules" , "white", None, "dark")
		print self.fw.cstring("\ttime", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Displays the current system time" , "white", None, "dark")
		print self.fw.cstring("\tdie", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Defuse HAL-9000 System" , "white", None, "dark")
		print self.fw.cstring("\tuse/load <moduletype> <module>", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Load a module" , "white", None, "dark")
		print self.fw.cstring("\tback", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Unloads current module" , "white", None, "dark")
		print self.fw.cstring("\tset <variable> <value>", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Set a variable to value (ex. set mode autonomous)" , "white", None, "dark")
		print self.fw.cstring("\tshow variables/view", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Show the modules configuration variables" , "white", None, "dark")
		print self.fw.cstring("\trun", "green")  +  self.fw.cstring(" - " , "red", None, "bright")  +  self.fw.cstring("Run the currently loaded module" , "white", None, "dark")
		return True
	
	# Print a formatted Box like [*]
	def printBox(self, colour="red", icon="*", border="white"):
		return self.fw.cstring("[", border)  +  self.fw.cstring(icon, colour)  +  self.fw.cstring("] ", border)