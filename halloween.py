#!/usr/bin/python

import time
import os
import sys
from pygame import mixer # Load the required library
from random import randint

playtime_seconds = 5

audio_files = [] 
file_path = "./files"

########################################################################
# returns a list with all mp3s from the directory
#
# @param	none
# 
# @return	list with all mp3s
#
########################################################################
def get_mp3s() :
	
	mp3_files = []

	if( os.path.exists(file_path) ):	

		print("scanning for mp3 files in folder 'files'")

		all_files = os.listdir(file_path)	
	
		for file in all_files:
		
			if ( file.endswith(".mp3") ):
				print("\tfound mp3: " + file)
				mp3_files.append(file)
	
		if( len(mp3_files) > 0 ):
			return mp3_files
		else:
			print("\tno mp3 files found in the directory!")
			print("\tplease add mp3s and restart the program")
			print("")
			print("the program will be exitet!")
			print("")
			sys.exit()
	else:
		print("directory '" + str(file_path) + "' does not exist!")
		print("program will be exited!")
		print("")
		sys.exit()
 

########################################################################
# returns a random file from a given list
#
# @param	filelist	a list with files
# 
# @return	a random file from the given list
#
########################################################################
def get_randomfile(filelist):
	
	if ( len(filelist) > 0 ):
		
		random_index = randint(0, len(filelist)-1)
		random_file  = filelist[random_index]
		return random_file
		
	else:
		print("there are no mp3 files found!")
		print("please add one into the 'files' folder")
		sys.exit()


########################################################################
# somthing like the 'main' function
########################################################################
print("")
print("***************************************************************")
print("* halloween scarybox                                          *")
print("***************************************************************")
print("")

audio_files = get_mp3s()


file_to_play = file_path + "/" + get_randomfile(audio_files)
mixer.init()


mixer.music.load(file_to_play)

print("")
print("playing file " + str(file_to_play))
mixer.music.play()
time.sleep(playtime_seconds)

print("stopping file " + str(file_to_play))
mixer.music.stop()

