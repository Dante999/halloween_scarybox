#!/usr/bin/python

import time
import os
import sys
import mp3_organizer
from pygame import mixer

playtime_seconds = 5

audio_files = [] 
file_path = "./files"




########################################################################
# somthing like the 'main' function
########################################################################
print("")
print("***************************************************************")
print("* halloween scarybox                                          *")
print("***************************************************************")
print("")

audio_files 	= mp3_organizer.get_mp3s_from_path(file_path)
file_to_play 	= mp3_organizer.get_randomfile_from_list(audio_files)

mixer.init()

mixer.music.load(file_to_play)

print("")
print("playing file " + str(file_to_play))
mixer.music.play()
time.sleep(playtime_seconds)

print("stopping file " + str(file_to_play))
mixer.music.stop()

