#!/usr/bin/python

from Adafruit_Thermal import *
import Image

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)


# Test character double-height on & off
printer.boldOn()
printer.justify('C')
printer.setSize('L')   # Set type size, accepts 'S', 'M', 'L'
printer.doubleHeightOn()
printer.println("\n\n\nJJR\n<3\nRAK")
printer.doubleHeightOff()

# Print the 75x75 pixel logo in jjrlogo.py
# import gfx.jjrlogo as jjrlogo
# printer.printBitmap(jjrlogo.width, jjrlogo.height, jjrlogo.data)

printer.printImage(Image.open('gfx/anarch.png'), True)

printer.feed(5)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
