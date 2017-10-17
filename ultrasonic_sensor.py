#!/usr/bin/python

#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time


GPIO_TRIGGER 	= 14
GPIO_ECHO	= 15

MAX_DISTANCE_CM = 250

########################################################################
# initializes the ultrasonic sensor
#
# @param	none
# 
# @return	none
#
########################################################################
def init():

	#GPIO Mode (BOARD|BCM)
	GPIO.setmode(GPIO.BCM)

	#GPIO Direction (IN|OUT)
	GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
	GPIO.setup(GPIO_ECHO, GPIO.IN)

	return


########################################################################
# returns the distance in cm 
#
# @param	none
# 
# @return	the distance in cm
#
########################################################################
def get_distance_cm():

	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	start_time_seconds = time.time()
	stop_time_seconds  = time.time()

	# repeat until the echo is send
	while GPIO.input(GPIO_ECHO) == 0:
		start_time_seconds = time.time()

	#stop_time_seconds = time.time()

	# repeat until the echo is received
	while GPIO.input(GPIO_ECHO) == 1:
		stop_time_seconds = time.time()

	# measure the difference between sending and receiving the echo
	time_difference_seconds = stop_time_seconds - start_time_seconds
    
	# calculate the distance from the time difference
	# speed of sound (34300 cm/s) x  time
	distance_cm = (time_difference_seconds * 17150)
	distance_cm = round(distance_cm,0)

	if( distance_cm > 350 ):
		distance_cm = 350

	return distance_cm
	





