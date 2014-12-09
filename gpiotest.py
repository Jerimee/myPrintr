#!/usr/bin/env python
from time import sleep
import os 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
	if ( GPIO.input(23) == True ):
		print("Printing")
		#os.system("/usr/games/fortune -s science | python ggd_printer4.py")
		print("Printed")
	sleep(1)