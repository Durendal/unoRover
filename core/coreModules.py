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

class coreModules:

    def __init__(self, framework):
        self.fw = framework
        self.fw.name = "Modules"
        self.fw.description = "Core Framework Module Functions"

    # Load modules into global namespace
    def preloadModules(self):
        sys.path.append("modules"+self.fw.seperator)

        for mod in self.fw.modTypes:
            # Add module directory
            sys.path.append("modules"+self.fw.seperator+mod+""+self.fw.seperator)

            # Create a list of available modules
            module = glob.glob("modules"+self.fw.seperator + mod + self.fw.seperator+"*.py")

            # Place each module in the global namespace
            for i in range(len(module)):
            
                module[i] = module[i].split(".")[0].split(""+self.fw.seperator)[2]
                module[i] = mod+"."+module[i]
                try:
                    globals()[module[i]] = self.ezImport(module[i])
                except:
                    print "Error Loading " + mod

        return True

    # Verify Module is set
    def verifyModule(self):

        # Verify that there is a currently loaded module
        if self.fw.module == None:

            print "\t"+self.fw.cstring(' ~> ', 'red', None, "bright"),
            print self.fw.cstring("No module defined", "white", None, "dark")
            return False

        return True

    # Load a module
    def loadModule(self, modname):
        
        # Verify that the module exists
        if not os.path.isfile("modules"+self.fw.seperator+self.fw.modType+""+self.fw.seperator+modname+".py"):
            print "\t"+self.fw.cstring(' ~> ', 'red', None, "bright"),
            print modname + " is not a valid module "
            return False
        
        # Empty framework module property
        self.fw.module = None

        # Generate name of module to load
        mod = self.fw.modType+"."+modname
        
        # Attempt to import and create an instance of module
        try:
            module = self.ezImport(mod)
            self.fw.module = module(self.fw)
        except:
            print "\t"+self.fw.cstring(' ~> ', 'red', None, "bright"),
            print modname + " is not a valid module "
            return False

        # Verify that module loaded correctly
        if self.fw.module == None:
            print self.fw.prompt+self.fw.cstring(' ~> ', 'red', None, "bright"),
            print "Error loading module " + module
            return False

        # Merge default variables with module variables
        self.fw.variables = dict(self.fw.defaultVariables.items() + self.fw.module.variables.items())
        print "\t"+self.fw.cstring(' ~> ', 'cyan', None, "bright")+self.fw.cstring("Module " + self.fw.module.name + " loaded", "green")

        return True

    # List currently available Modules
    def listModules(self):

        # Ensure all modules are loaded
        self.preloadModules()

        for modu in self.fw.modTypes:
            # Generate a list of all available modules
            classes = glob.glob("modules"+self.fw.seperator + modu + self.fw.seperator+"*.py")
            if modu == "algo":
                writeval = "Algorithms"
            elif modu == "auxi":
                writeval = "Auxiliaries"
            else:
                writeval = "Error check coreModules.listModules()"
            print "\t" + self.fw.cstring(".:", "red")+self.fw.cstring(writeval, "green")+self.fw.cstring(":.", "red")

            # Verify each module in the directory exists in the namespace, display name and description of the ones that match
            for i in range(len(classes)):
                
                classes[i] = classes[i].split(".")[0].split(""+self.fw.seperator)[2]
                if classes[i] == '__init__':
                    continue
                classes[i] = modu + "." + classes[i]
                
                if classes[i] in globals():
                    try:
                        mod = self.ezImport(classes[i])
                        module = mod(self.fw)
                    except:
                        continue
                    print "\t"+self.fw.cstring(' ~> ', 'cyan', None, "bright")+self.fw.cstring(module.name, "blue", None, 'bright')+self.fw.cstring(" - ", "red")+self.fw.cstring(module.description, "white", None, 'dark')
                    module = None

        return True

    # Returns the type of module in use
    def listType(self):

        return self.fw.modType

    # Method to dynamically load modules
    def ezImport(self, name):
        components = name.split('.')

        # Obtain module name
        comp = components[1]
        
        # Attempt to import module
        try:
            mod = __import__(name, fromlist=[comp])
            mod = getattr(mod, comp)
        except:
            return False

        return mod

    # Display module variables
    def showVariables(self):
        
        # Verify module is loaded
        if not self.verifyModule():
            return False

        # Check to see if all required variables are set
        self.verifyVariables()

        # Print module variables and information
        for key, variable in self.fw.variables.items():
            required = '*' if variable['required'] else ' '
            
            print self.fw.cstring("\t"+required, "red"),
            print self.fw.cstring(key, "blue", None, "bright"),
            if len(key) < 10:
                print "\t",
            print " => ",
            if hasattr(self.fw.module, key):
                val = getattr(self.fw.module, key)
                print self.fw.cstring(val, "green"),
            else:
                val = "Empty"
                print self.fw.cstring(val, "red", None, "bright"),
            if len(val) < 10:
                print "\t",
            print " => ",
            print self.fw.cstring(variable['description'], "yellow", None, "dark")

        print self.fw.cstring("\n\t*", "red"),
        print self.fw.cstring(" = required", "green")

    # Determine if a variable name is valid
    def variableExists(self, variable):
        return variable in self.fw.variables

    # Check if required variables are set
    def verifyVariables(self):

        # Check through each variables
        for key, data in self.fw.variables.items():
            
            # Ensure variable property has been set
            check = hasattr(self.fw.module, key)

            # Check if variable is required, and if it has been defined
            if data['required'] == True and not check:
                print "\t"+self.fw.cstring(' ~> ', 'red', None, "bright"),
                print "Missing Required Variable " + key
                return False

            # Check if variable is not required, and if it has been defined
            if data['required'] == False and not check:
                
                setattr(self.fw.module, key, self.fw.variables[key]['default'])

        return True

    # Set module variable value
    def setValue(self, variable, value):

        # Check if module is valid
        if self.verifyModule() == False:
            
            return False

        # Check that variable submitted is a valid module variable
        if self.variableExists(variable) == False:
            print "\t"+self.fw.cstring(' ~> ', 'red', None, "bright"),
            print "Variable " + variable + " doesn't exist"
            return False

        # Set module variable
        setattr(self.fw.module, variable, value)
        return True
