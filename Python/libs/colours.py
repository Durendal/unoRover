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
from colorama import init
init()
from colorama import Fore, Back, Style



class colours:
	
	def __init__(self, framework):

		self.fw = framework

		#self.fw = framework
	   	self.name = 'Colours'
	   	self.description = 'Library to provide text colouring in python CLI'
				
		# Set up shell colours
		self.foreground_colours = { 'black' : Fore.BLACK,
								    'blue' : Fore.BLUE,
								    'green' : Fore.GREEN,
								    'cyan' : Fore.CYAN,
								    'red' : Fore.RED,
								    'purple' : Fore.MAGENTA,
								    'yellow' : Fore.YELLOW,
								    'white' : Fore.WHITE
								  }
 			
		self.background_colours = { 'black' : Back.BLACK,
								 	'red' : Back.RED,
								 	'green' : Back.GREEN,
								 	'yellow' : Back.YELLOW,
								 	'blue' : Back.BLUE,
								 	'magenta' : Back.MAGENTA,
								 	'cyan' : Back.CYAN,
								 	'white' : Back.WHITE 
								  }
		self.styles = { 'normal' : Style.NORMAL,
						'dim' : Style.DIM,
						'bright' : Style.BRIGHT
					  }
 
	# Returns coloured string
	def cstring(self, string, foreground_colour = None, background_colour = None, styles = None):
		coloured_string = "";

		# Check if given Style found
		if styles in self.styles.keys():
			coloured_string += self.styles[styles]
		# Check if given foreground colour found
		if foreground_colour in self.foreground_colours.keys():
			coloured_string += self.foreground_colours[foreground_colour]
			
		# Check if given background colour found
		if background_colour in self.background_colours.keys():
			coloured_string += self.background_colours[background_colour]
			
 
		# Add string and end colouring
		coloured_string +=  string + Fore.RESET + Back.RESET + Style.RESET_ALL
 
		return coloured_string
		
 
	# Returns all foreground colour names
	def getfgcolours(self):
		return self.foreground_colours.keys()
	
 
	# Returns all background colour names
	def getbgcolours(self):
		return self.background_colours.keys()
	