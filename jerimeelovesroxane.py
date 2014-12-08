#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)


# Test character double-height on & off
printer.justify('C')
printer.doubleHeightOn()
printer.println("JJR <3 RAK")
printer.doubleHeightOff()

# Print the 75x75 pixel logo in jjrlogo.py
import gfx.jjrlogo as jjrlogo
printer.printBitmap(jjrlogo.width, jjrlogo.height, jjrlogo.data)

printer.feed(5)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
