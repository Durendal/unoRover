"""
    http://code.activestate.com/recipes/134892/
    code for reading in the keyboard input live
"""
import os
class Getch:

    def __init__(self, framework):
        self.os = os.name
        self.fw = framework
        self.name = 'Getch'
        self.description = 'Library to monitor for keyboard events'

    def GetchWindows(self):
        import msvcrt
        return msvcrt.getch()

    def GetchUnix(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def getdatch(self):
        if self.os == 'poxis':
            return self.GetchUnix()
        else:
            return self.GetchWindows()