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

import sys
import glob
import os

class libraries:

	def __init__(self, framework):

		#self.fw = framework
		self.fw = framework
		self._liblist = self.preloadLibs()
		for lib in self._liblist:
			if '__init__' in lib or '.pyc' in lib:
				continue

	# Create an instance of the library
	def loadLibrary(self, lib):

		if lib == "libs." or "__init__" in lib or ".pyc" in lib:
			return False
		libf = "libs."+str(lib)
		if not os.path.isfile("libs/"+lib+".py"):
			print "\t" + libf + " is not a valid library"
			return False
		#print self.fw.prompt+" Loading Library " + lib
		library = self.ezImport(libf)
		setattr(self, str(lib), library(self.fw))

	# Import Library
	def ezImport(self, name):
		components = name.split('.')
		comp = components[1]
		mod = __import__(name, fromlist=[comp])
		mod = getattr(mod, comp)
		return mod

		# Load modules into global namespace
	def preloadLibs(self):

		sys.path.append("libs")
		lib = glob.glob("libs/*.py")
		lib_files = []
		for i in range(len(lib)):
			self.loadLibrary(lib[i][5:-3])
			lib[i] = lib[i].split(".")[0].split(""+self.fw.seperator)[1]
			lib[i] = "libs."+lib[i]
			globals()[lib[i]] = self.ezImport(lib[i])
			lib_files.append(lib[i])

		return lib_files

	# List installed libraries
	def listLibs(self):

		classes = glob.glob("libs/*.py")
		for i in range(len(classes)):
			classes[i] = classes[i].split(".")[0].split(""+self.fw.seperator)[1]
			if classes[i] == '__init__':
				continue
			classes[i] = "libs."+classes[i]
			if classes[i] in globals():
				lib = self.ezImport(classes[i])
				library = lib(self)
				print "\t"+self.fw.cstring(' ~> ', 'cyan', None, "bright")+self.fw.cstring(library.name, "blue", None, "bright")+self.fw.cstring(" - ", "red")+self.fw.cstring(library.description, "white", None, "dark")
				library = None

		return True