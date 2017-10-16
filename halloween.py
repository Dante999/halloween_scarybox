#!/usr/bin/python

import time
import os
import sys
import mp3_organizer
import ultrasonic_sensor
from pygame import mixer
import RPi.GPIO as GPIO  



# how long the mp3 should be played before the player stops
MP3_PLAYTIME_SECONDS = 5

# Volume (value from 0.0 to 1.0)
MP3_VOLUME = 1.0

# folder where the mp3-files are stored
FILE_PATH = "./files"

# if the measured distance is under this level, the hysteresis will increased
MIN_DISTANCE_CM = 1500

# if the hysteresis is greater than this level, the mp3 will be played
MAX_HYSTERESIS 	= 5

# array with all mp3 files and their path
audio_files = [] 


########################################################################
# somthing like the 'main' function
########################################################################
print("")
print("***************************************************************")
print("* halloween scarybox                                          *")
print("***************************************************************")
print("")

hysteresis = 0
distance_cm = 0


audio_files = mp3_organizer.get_mp3s_from_path(FILE_PATH)
ultrasonic_sensor.init()


try:
	while True:
		distance_cm = ultrasonic_sensor.get_distance_cm()
		
		print("current distance = %.1f cm" % distance_cm)
		
		if (distance_cm < MIN_DISTANCE_CM):
			hysteresis += 1
		elif (hysteresis > 0):
			hysteresis -= 1
			
		if (hysteresis > MAX_HYSTERESIS):
			file_to_play = mp3_organizer.get_randomfile_from_list(audio_files)

			mixer.init()
			mixer.music.load(file_to_play)

			print("")
			print("playing file " + str(file_to_play))
			mixer.music.play()
			time.sleep(MP3_PLAYTIME_SECONDS)

			print("stopping file " + str(file_to_play))
			mixer.music.stop()
			
			hysteresis = 0
			
except KeyboardInterrupt:
	print("stopped from user")

finally:
	print("doing cleanup stuff...")
	GPIO.cleanup()
