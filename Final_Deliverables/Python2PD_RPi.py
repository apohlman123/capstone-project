#############################################################################################################
#Company:      Loyola Marymount University
#Engineer:     Austin Pohlman
#
#Last Edit: 9May2019
#Design Name:  Python2PD_RPi.py
#Project Name: Audio Production Instrument (API)
#Tool Versions: Python 3
#
#Description:
#    Python layer for hardware interfacing and communication with Pure Data patches
#    Designed for use with the Raspberry Pi 3B+ processor board
#
#Dependencies:
#    "pyOSC" python module (See OSC-updates for updated module with Python3 compatibility)
#    "RPi.GPIO" python module (Python 2 or 3)
#    "adafruit_mpr121" python module (Python 3 only)
#    "time", "socket", "threading", "board", "busio" preinstalled python modules (Python 2 or 3)
#Revisions:
#    See github for full revision history
#############################################################################################################

import OSC
import time
import RPi.GPIO as GPIO
import socket
import threading
import board
import busio
import adafruit_mpr121

# Variables keep track of I/O pins (Note that I/0 Pin 20 is not functional on the Pi)
Sq3 = 26
Sq2 = 13
Sq1 = 6
Sq0 = 5
BPlay = 11
BStop = 25 #Was 9
BReset = 10
Bt3 = 16
Bt2 = 12
Bt1 = 7
Bt0 = 8
Bt_int = 9 #Was 20
Bt_shift = 22

# Set BCM I/O (Numbered based on the Pi's Broadcom chip not the header)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Sq3,GPIO.OUT)
GPIO.setup(Sq2,GPIO.OUT)
GPIO.setup(Sq1,GPIO.OUT)
GPIO.setup(Sq0,GPIO.OUT)
GPIO.setup(BPlay,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BStop,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BReset,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Bt3,GPIO.IN)
GPIO.setup(Bt2,GPIO.IN)
GPIO.setup(Bt1,GPIO.IN)
GPIO.setup(Bt0,GPIO.IN)
GPIO.setup(Bt_int,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Bt_shift,GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Moved here to avoid "client not defined" errors
# Init OSC client for send, connect to virtual port on the Pi
client = OSC.OSCClient()
client.connect(('localhost', 9001))

# Init i2c comms for touchpads
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
touched = mpr121.touched_pins #returns 12-member tuple of current pin state

# Define functions
def sequence_control(channel):
    #Callback function for Play Stop Reset control buttons
    if channel==BPlay:
        client.send(OSC.OSCMessage("/play"))
    elif channel==BStop:
        client.send(OSC.OSCMessage("/stop"))
    elif channel==BReset:
        client.send(OSC.OSCMessage("/reset"))
    else :
        print("No control input detected")

def sequence_button(channel):
    #Callback function to recieve sequencer button input
    a3 = GPIO.input(Bt3)
    a2 = GPIO.input(Bt2)
    a1 = GPIO.input(Bt1)
    a0 = GPIO.input(Bt0)
    #print(a3)
    #print(a2)
    #print(a1)
    #print(a0)
    #print("Interrupt recieved on I/O {}" .format(channel))
    #Cascaded encoder setup is active high
    if a3==False and a2==False and a1==False and a0==False:
        client.send(OSC.OSCMessage("/B0"))
        #print("trigger 0")
    elif a3==False and a2==False and a1==False and a0==True:
        client.send(OSC.OSCMessage("/B1"))
        #print("trigger 1")
    elif a3==False and a2==False and a1==True and a0==False:
        client.send(OSC.OSCMessage("/B2"))
        #print("trigger 2")
    elif a3==False and a2==False and a1==True and a0==True:
        client.send(OSC.OSCMessage("/B3"))
        #print("trigger 3")
    elif a3==False and a2==True and a1==False and a0==False:
        client.send(OSC.OSCMessage("/B4"))
        #print("trigger 4")
    elif a3==False and a2==True and a1==False and a0==True:
        client.send(OSC.OSCMessage("/B5"))
        #print("trigger 5")
    elif a3==False and a2==True and a1==True and a0==False:
        client.send(OSC.OSCMessage("/B6"))
        #print("trigger 6")
    elif a3==False and a2==True and a1==True and a0==True:
        client.send(OSC.OSCMessage("/B7"))
        #print("trigger 7")
    elif a3==True and a2==False and a1==False and a0==False:
        client.send(OSC.OSCMessage("/B8"))
        #print("trigger 8")
    elif a3==True and a2==False and a1==False and a0==True:
        client.send(OSC.OSCMessage("/B9"))
        #print("trigger 9")
    elif a3==True and a2==False and a1==True and a0==False:
        client.send(OSC.OSCMessage("/B10"))
        #print("trigger 10")
    elif a3==True and a2==False and a1==True and a0==True:
        client.send(OSC.OSCMessage("/B11"))
        #print("trigger 11")
    elif a3==True and a2==True and a1==False and a0==False:
        client.send(OSC.OSCMessage("/B12"))
        #print("trigger 12")
    elif a3==True and a2==True and a1==False and a0==True:
        client.send(OSC.OSCMessage("/B13"))
        #print("trigger 13")
    elif a3==True and a2==True and a1==True and a0==False:
        client.send(OSC.OSCMessage("/B14"))
        #print("trigger 14")
    elif a3==True and a2==True and a1==True and a0==True:
        client.send(OSC.OSCMessage("/B15"))
        #print("trigger 15")
    else :
        print("No button input detected")

#Unused callback function for interrupt-driven touch pads
#def touchpad_pressed(channel):
    #Create a multi-message OSC bundle
    #The OSC messages addresses correspond to which of the touchpads are pressed
    #print("Interrupt recieved on I/O {}" .format(channel))
    #touchpads = OSC.OSCBundle("/test", time=0)
    #for i in range(12):
    #    if mpr121[i].value:
    #        touchpads.append(OSC.OSCMessage("/T{}" .format(i)))
    #client.send(touchpads)
    #start_time = time.time()
    #for i in range(12):
        #if mpr121[i].value:
            #client.send(OSC.OSCMessage("/T{}" .format(i)))
    #print("touchpad send took {} time to run" .format(time.time()-start_time))

def OSCreceive_handler(addr, tags, data, source):
    #Callback function to output sequence data to LEDs
    #print("Received from: {}, " .format(OSC.getUrlStr(source)))
    #print("Address: {}, " .format(addr))
    #print("Tags: {}, " .format(tags))
    #print("Data received: {}" .format(data))
    if data[0] == 0:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,False)
    elif data[0] == 1:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,True)
    elif data[0] == 2:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,False)
    elif data[0] == 3:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,True)
    elif data[0] == 4:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,False)
    elif data[0] == 5:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,True)
    elif data[0] == 6:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,False)
    elif data[0] == 7:
        GPIO.output(Sq3,False) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,True)
    elif data[0] == 8:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,False)
    elif data[0] == 9:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,True)
    elif data[0] == 10:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,False)
    elif data[0] == 11:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,False) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,True)
    elif data[0] == 12:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,False)
    elif data[0] == 13:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,False) ; GPIO.output(Sq0,True)
    elif data[0] == 14:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,False)
    elif data[0] == 15:
        GPIO.output(Sq3,True) ; GPIO.output(Sq2,True) ; GPIO.output(Sq1,True) ; GPIO.output(Sq0,True)
    else :
        print("Sequence out of range")
    #print("Position in sequence: {}" .format(data))

# Interrupt detection
GPIO.add_event_detect(Bt_int, GPIO.FALLING, callback=sequence_button, bouncetime=200)
GPIO.add_event_detect(BPlay, GPIO.RISING, callback=sequence_control)
GPIO.add_event_detect(BStop, GPIO.RISING, callback=sequence_control)
GPIO.add_event_detect(BReset, GPIO.RISING, callback=sequence_control)
#Unused callback function... Touchpads detected through polling instead
#GPIO.add_event_detect(Touch_int, GPIO.FALLING, callback=touchpad_pressed)

# Init OSC server for receive
server = OSC.OSCServer(('localhost', 9002))
server.addMsgHandler("/test", OSCreceive_handler)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()

input("Enter any key to establish Pure Data OSC connection: ")
#Use python exceptions to attempt to establish OSC connection and start sequencer
try:
    client.send(OSC.OSCMessage("/connect"))
    print("Connection established!")
    client.send(OSC.OSCMessage("/play"))
except:
    print("Could not establish connection")

#The following for loop polls the touchpad chip and loops through the 12 touchpads...
#...if one is pressed while the shift button is low, set the flag high and send a...
#...message. If one is pressed alone, set the flag high and send a different message...
#...otherwise, the flag is cleared; this prevents multiple triggers when a pad is pressed
#Flag vector, each element is a flag relating to the corresponding touchpad
beentouched = [0] * 12
try:
    while True:
        for i in range(12):
            if beentouched[i] != 1:
                if mpr121[i].value and not(GPIO.input(Bt_shift)):
                    #Bt_shift is active low
                    client.send(OSC.OSCMessage("/S{}" .format(i)))
                    beentouched[i] = 1
                    #print("shift to sequencer line {}" .format(i))
                elif mpr121[i].value:
                    client.send(OSC.OSCMessage("/T{}" .format(i)))
                    beentouched[i] = 1
                    #print("touchpad {} pressed!" .format(i))
            if mpr121[i].value == False:
                    beentouched[i] = 0
#While loop is interrupted by ctrl+C, safely shuts down OSC server and disables I/O
except KeyboardInterrupt:
    print("Shutting down OSC Server")
    server.close()
    client.send(OSC.OSCMessage("/disconnect"))
    print("Closing server thread")
    server_thread.join()
    GPIO.cleanup()
    print("Done!")
