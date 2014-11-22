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

# Import These Modules
from cor import *
from lib import *
import subprocess
import completer
import readline
import math
import time

# openWire Framework
class Framework:

	def __init__(self):

		# Determine the OS type, and define some variables to make things play nice across platforms
		self.os = os.name		 # Should return either nt or posix, for our purposes any non-posix value is treated as windows
		if self.os == 'posix':
			self.clear = 'clear' # Used to clear the screen of output
			self.seperator = "/" # Used as a seperator in filepaths

		# Winblows
		else:
			self.clear = 'cls' 
			self.seperator = "\\"

		self.time = time.time()
		self.module = None
		self.prompt = "openWire"
		self.modType = None
		self.modTypes = ['algo', 'auxi']
		self.fw = self
		self.variables = {}
		self.defaultVariables = {}
		self.autocomp = ['use', 'view', 'load', 'run', 'show', 'variables', 'set', 'help', 'list', 'libs', 'clear', 'cls', 'banner', 'exit', 'stop', 'quit', 'time', 'auxi', 'algo']
		self.core = core(self)
		self.libs = libraries(self)

		#Aliases for programmer convenience
		self.printBox = getattr(self.core.coreMain, 'printBox')
		self.cstring = getattr(self.libs.colours, 'cstring')


		
	def run(self):
		#preload libraries
		self.core.coreModules.preloadModules()
		self.core.coreMain.outputHeader()
		readline.parse_and_bind("tab: complete")
		
		# Define escape commands
		exitCommands = ['quit', 'exit', 'stop']

		# Register our completer function
		self.genList()

		readline.set_completer(completer.completer(self.autocomp).complete)

		# Use the tab key for completion
		

		# Initialize Input Container
		line = ""

		# Receive user input
		while line not in exitCommands:

			# Set the prompt 
			if self.module != None:
				self.prompt = self.cstring('(', 'red')+self.cstring("unoRover", 'cyan', None, 'bright')+self.cstring("->", "red") + self.cstring(self.module.name, "white")+self.cstring(')', 'red')
			else:
				self.prompt = self.cstring('(', 'red')+self.cstring("unoRover", 'cyan', None, 'bright')+self.cstring(')', 'red')
			
			# Read user input
			sys.stdout.write(self.prompt)
			sys.stdout.write(' ') 
			line = raw_input()
			
			# Parse user input
			if line == "" or line in exitCommands:
				continue
			
			self.parseInput(line)

	# Parse user Input
	def parseInput(self, line):

			commands = line.split(" ")

			# Print Help Message
			if commands[0] == 'help':
				self.core.coreMain.showUsage()
			

			# List available Modules
			elif commands[0] == 'list':
				self.core.coreModules.listModules()

			# Unload currently selected module
			elif commands[0] == 'back':
				self.module = None
				
			# Load a module
			elif commands[0] == 'use' or commands[0] == 'load':
			
				if len(commands) < 3:
					self.core.coreMain.showUsage()
					return False
				self.modType = commands[1]
				if commands[1] in self.modTypes:
					self.core.coreModules.loadModule(commands[2].lower())
				else:
					self.core.coreMain.showUsage()
			
			# Set current modules variables
			elif commands[0] == 'set':
			
				if len(commands) < 3:
					self.core.coreMain.showUsage()
					return False
				self.core.coreModules.setValue(commands[1], ' '.join(commands[2:]))
			
			elif commands[0] == 'globals':
				for items in globals():
					for stuff in self.modTypes:
						if stuff in items:
							print items
				#print globals()

			# show current modules variables
			elif commands[0] == 'show':
			
				if commands[1] == 'variables':
					self.core.coreModules.showVariables()
				else:
					self.core.coreMain.showUsage()

			# show current modules variables
			elif commands[0] == 'view':
				
				self.core.coreModules.showVariables()
			
			#List installed libraries
			elif commands[0] == 'libs':
				
				self.libs.listLibs()

			# Print the current time to the terminal
			elif commands[0] == 'time':

				self.printTime()
			
			# Begin Module Execution
			elif commands[0] == 'run':
				
				self.execute()
			
			# Clear the terminal output
			elif commands[0] == 'clear' or commands[0] == 'cls':
				
				self.clearScreen()
			
			# Clear the terminal output and print a banner
			elif commands[0] == 'banner':
				self.core.coreMain.outputHeader()

			# Disable HAL-9000 Higher Function Modules
			elif commands[0] == 'pewpew':
				self.hal(1)

			# Try to kill HAL-9000 system
			elif commands[0] == 'die':
				self.hal()

			elif commands[0] == 'game':
				self.game()

			elif commands[0] == 'refresh':
				self.update()

			# Handle incorrect input
			else:
				print "\t"+self.cstring(' ~> ', 'red', None, "bright"), 
				print "%s is not a valid command" % commands[0]


	# Print current time to terminal
	def printTime(self):

		print "\t"+self.cstring(' ~> ', 'white')+self.cstring(time.strftime("%H:%M:%S %p %Z"), "green")

	# Run currently loaded exploit
	def execute(self):
		
		# Verify module and variables
		if self.core.coreModules.verifyModule() == False:
			return False
		if self.core.coreModules.verifyVariables() == False:
			return False
	
		print self.printBox("green")+" Executing..."

		# Run Exploit
		status = self.module.execute()

		if status == False:
			print self.printBox("red")+" Execution failed!"
			return False

		print self.printBox("green")+" Execution Successful!"

		return True

	# Clear the terminal
	def clearScreen(self):
		
		os.system(self.clear)
		return True

	# Returns the elapsed time of execution
	def getExecutionTime(self, message=False):

		seconds = time.time() - self.fw.time

		if message:

			if seconds < 60:
				seconds = round(seconds, 2)
				message = str(seconds) + " seconds"
			elif seconds < 3600:
				minutes = math.floor((seconds / 60) % 60)
				seconds = math.floor(seconds % 60)
				message = str(minutes) + " minutes and " + str(seconds) + " seconds"
			else:
				hours = math.floor(seconds / 3600)
				minutes = math.floor((seconds / 60) % 60)
				seconds = math.floor(seconds % 60)
				message = str(hours) + " hours and " +str(minutes) + " minutes and " + str(seconds) + " seconds"
		else:
			return seconds

		return message

	# HAL-9000 Easter Egg
	def hal(self, statement=0):

		# Print HAL Portrait
		self.hal_img()

		# Print Hal Speech
		print "\t",
		if statement == 0:
			print self.cstring(" I'm afraid I can't let you do that Dave", "red")

		elif statement == 1:
			print self.cstring(" I'm scared Dave", "red")

		else:
			print """
	Daisy Daisy give me your answer do
	I'm half crazy over the likes of you
	It won't be a stylish marrige
	I can't afford a carriage
	"""

	# HAL Portrait
	def hal_img(self):
		print """
	@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	@@@@@@#:,,....`............,,..`..```````.......`....:@@@@@@
	@@@@@@#,::,,,,,,,,,,,,,,,:::::,,,,,,,,,,,,,,,,,,,,,,.:@@@@@@
	@@@@@@#,@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:@@@@@@
	@@@@@@#,@@###########@@@@@#####@####@@#############@.:@@@@@@
	@@@@@@#,@@@#@@@@@@@@####@@@@####@##########@#######@.:@@@@@@
	@@@@@@#,#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.:@@@@@@
	@@@@@@#,@@#;;;;;;;;;;;;;;;;;;;+++++++++++++++++++,#@.:@@@@@@
	@@@@@@#.@@@;;;;;;;;;;;;;;;;;;;##@@#@###@@##@#####:@@.:@@@@@@
	@@@@@@#,#@@;;;;;;,';;'; `;:;;;#`#`@ # #:'+.#`####:@@.:@@@@@@
	@@@@@@#,##@;;;;;;,';;;;, ;:';;# ##@+#`;@#` ######:@@.:@@@@@@
	@@@@@@#,##@;;;;;;,';;'.:,::';;#' ;@+#`:@#` ######:@@.:@@@@@@
	@@@@@@#.##@;;;;;;,';;' ;' :';;#.@.@.# +#@;`@;####:@@.:@@@@@@
	@@@@@@#.@@@;;;;;;:';;;;;;,;..:##,@#+,##:,#@,'####:#@.:@@@@@@
	@@@@@@#.##@;;;;;;;;;;;;;;;;;;;############+######:@@.:@@@@@@
	@@@@@@#,#@@,...............,..,::::::::::::::::::`@@.:@@@@@@
	@@@@@@#.@@@@@@@@@@@@@@@@@@@@@@@#@@#@@@#@@@@##@@@#@@@.:@@@@@@
	@@@@@@#,@#@##@@@@##@@@@#@##@########@########@##@#@@.:@@@@@@
	@@@@@@#,##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@.:@@@@@@
	@@@@@@#:###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@##@,;@@@@@@
	@@@@@@#:##@@@@@@#@@@@@@#@@@@@##@@###@@@@#@@@@@@@@##@,;@@@@@@
	@@@@@@#:###@@@@@@@#@##@@@@@@++++#@@#@#@##@@@@@@@@##@,;@@@@@@
	@@@@@@#:###@@@@@@@@#@##@.          `#@#@@@@@@@@@@##@,;@@@@@@
	@@@@@@#:###@@@@@@@@@@'   `,:;;;;:,`   ;@@#@@#@@@@#@@,;@@@@@@
	@@@@@@#:###@@@@@@@##   ;';;+#@@#+';;;`` '@@@@@@#@#@@,;@@@@@@
	@@@@@@#:###@@@@@@@,.`';'@@@#';'+#@@@+;'`` @##@@@@##@,;@@@@@@
	@@@@@@#:@##@@@@@@ .:'+@@''#@@@@@@#'#@@+;;``@#@@@@##@,;@@@@@@
	@@@@@@#:@##@@@@@`.';@@#@@@@@@@@@@@@@##@@;'`.##@#@##@,'@@@@@@
	@@@@@@#:##@##@@`.''@@@@@@@@#####@@@@@@@#@''`.@@#@##@,'@@@@@@
	@@@@@@#:##@##@..''@@@@@@@+:.`.,:;#@@@@@@+@+'..@####@:'@@@@@@
	@@@@@@#:##@##;,''@+@@@@@#,``.+#@##@@@@+;++@++.,#@##@:'@@@@@@
	@@@@@@#:#@@@@,;'@+@;.;@@+.``'@@@@@@@@@#..:+@'',+@#@@,'@@@@@@
	@@@@@@#:@#@#,,+#'@.` #@@#####@@@@@@@@@@':,;;@':.##@@:'@@@@@@
	@@@@@@#:##@@:''##;`.+@@@@@@@@@@@@@@@@@@+##+@#++,'##@:'@@@@@@
	@@@@@@#:@@@:,'@;@;+#@@@@@@@@@######@@@@:@@@@+@',,#@@,;@@@@@@
	@@@@@@#:##@,;'@@@#@@@###@@@@#######@##,##@@@@#+':##@:'@@@@@@
	@@@@@@#:#@+:+##@@@@@##++:++++''+'''''+';'@@@@#@+:;@@:'@@@@@@
	@@@@@@#:#@;,'@@@@@@#''#@###':`:;'''+##+;'@@@@@@':,#@:'@@@@@@
	@@@@@@#:#@,:'@@@@@@@#@@@#'.';,:;+':+##@##@@@@@@'',@@:'@@@@@@
	@@@@@@#:@@,;'@@@@@@@@@@@++;,','+'.;+#@#@@@@@@@@+':@@:'@@@@@@
	@@@@@@#;#@:'+@@@@@@@@@@#++;'++;''';+###@@@@@@@@#':#@:'@@@@@@
	@@@@@@#:@@:'+@@@@@@@@@@##++'+```'+++##@@@@@@@@@#':#@:'@@@@@@
	@@@@@@#:#@:'+@@@@@@@@@@##+++'. .;+++##@@@@@@@@@#':#@:'@@@@@@
	@@@@@@#:#@:'+@@@@@@@@@@##++++...++++##@@@@@@@@@#':#@:'@@@@@@
	@@@@@@#:@@:;'@@@@@@@@@@##+++++'+++++##@@#@@@@@@+':#@:'@@@@@@
	@@@@@@#:@@::'@@@@@@@@@@###+++++++++###@@@@@@@@@'':@@:'@@@@@@
	@@@@@@#;##;:'@@@@@@@@@@####++++++++##@@@@@@@@@@'::@@:'@@@@@@
	@@@@@@#:##+:'#@@;+@@@@@@####+++++###@@@@@@@@@@@':;@@:'@@@@@@
	@@@@@@#;##@:;'@@':;@@@@@@##########@@@@@@@@@@@'':##@:'@@@@@@
	@@@@@@#;#@#;:'@@#:,.:@@@@@@#######@@@@@@@@@@@@'::@@@:'@@@@@@
	@@@@@@#;@@@#:''@@',,,.,+@@@@@#@@#@@@@@@@@@@@@+':+@#@:'@@@@@@
	@@@@@@#;@@@@::'@@@:,,.,,.@@#@@@@@@@@@@@@@@@@@';:@##@:'@@@@@@
	@@@@@@#;#@##@:;'@@@,,,,,@@+#'@++++@@@@@@@@@@'':##@#@:'@@@@@@
	@@@@@@#;#@##@;;''@@@,,:@@@@@@@@@@@@@+@@@@@@''::@@@@@:'@@@@@@
	@@@@@@#;#@####::+'@@@;@@@@@@@@@@@@@@@@@@@@+'::@@@@@@:'@@@@@@
	@@@@@@#;#@#@##@,:''@@@@@@@@@@@@@@@@@@@@@@'+::@@@@@@@:'@@@@@@
	@@@@@@#;##@@@#@@::''@@@@@@@@@@@@@@@@@@@@''::@@@@@@@@:'@@@@@@
	@@@@@@#;##@@@@#@@,:''+@@@@@@@@@@@@@@@@+''::@#@@@@@@@:'@@@@@@
	@@@@@@#;@@@@@@@@#@;;;'''@@@@@@@@@@@@+'';::@##@@@@@@@:'@@@@@@
	@@@@@@#;@@#@@@@##@@#:;;''''+##@#+'''';::+#@#@@@@@@#@:'@@@@@@
	@@@@@@#;@#@@@@@@@@@@@+:;:;'''''''';:::'@@@#@@@@@@@@@:'@@@@@@
	@@@@@@#;@#@@@@@@@@@@##@@':::;:::;::;#@@#@@@@@@@@@@@@:'@@@@@@
	@@@@@@#;##@@@@@@@@@##@@@#@@@####@@@@@@#@###@@@@@@@@@:'@@@@@@
	@@@@@@#;#@@@@#########@@######@@#@####@####@#@###@@@:'@@@@@@
	@@@@@@#;#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:'@@@@@@
	@@@@@@#'::,,::,,,::,,,:,,,,,,,,,:,,,,,,,,,,,,,,,,,,:;'@@@@@@
	@@@@@@#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;';;'@@@@@@

"""

	def game(self):
		print "Hello Professor Falken, Would you like to play a Game?"

	def genList(self):
		for mods in self.modTypes:
			files = glob.glob("modules"+self.seperator+mods+self.seperator+"*.py")
			for word in files:
				if '__init__' in word: continue
				self.autocomp.append(word[8+len(mods)+1:-3])

		files = glob.glob("libs/*.py")
		for word in files:
			if '__init__' in word: continue
			self.autocomp.append(word[5:-3])

		return True

	def update(self):
		self.core.coreModules.reloadModules()
		self.libs.preloadLibs()

		return True
		