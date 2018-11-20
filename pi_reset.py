#AUDIO PRODUCTION INSTRUMENT
#LMU SENIOR CAPSTONE 2018/19 - ELECTRICAL ENGINEERING
#   Austin Pohlman ('19), Clay Sauter ('19)
#   2Nov18

#The following code resets the Pi to base state
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
