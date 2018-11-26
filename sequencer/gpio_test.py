#Initialize Pi3B+ GPIO
#   import GPIO structure, time  structure
#   setup GPIO naming as Broadcom (BCM), which goes by pin designations
#       -alternative is (BOARD), which goes by physical pins with top-left ref.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#Setup GPIO pins A0-A3 as output
A3 = 5 #chosen GPIO pin number
A2 = 6 #chosen GPIO pin number
A1 = 16 #chosen GPIO pin number
A0 = 26 #chosen GPIO pin number
BStart = 17
GPIO.setup(A3,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A0,GPIO.OUT)
GPIO.setup(BStart,GPIO.IN)

#Initialize Variables
#OSC_sequence = 0                #updated by PureData as sequence runs
current_sequence = 0            #updated by code to keep track of sequence
sequence_length = range(0,16)
#chosen_BPM = input("Please choose your BPM: ") #asks for user to input BPM
chosen_BPM = 60
BPM_secs = float(chosen_BPM)/60  #converts BPM to per second, rounds to whole
BPM_delay = 1/BPM_secs         #converts to time delay in seconds

#Wait for Start button press interrupt
Start = GPIO.wait_for_edge(BStart, Rising, timeout = 5000)

if Start != True :
    print("Timed out waiting for start")
else :
    print("Starting Sequencer!")

#0
GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
print(current_sequence)
time.sleep(round(BPM_delay,3))

#1
GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#2
GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#3
GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#4
GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#5
GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#6
GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#7
GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#8
GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#9
GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#10
GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#11
GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#12
GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#13
GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#14
GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

#15
GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
current_sequence += 1
print(current_sequence)
time.sleep(round(BPM_delay,3))

GPIO.cleanup()
