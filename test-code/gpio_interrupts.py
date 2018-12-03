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
BStop = 27
BReset = 22
GPIO.setup(A3,GPIO.OUT)
GPIO.setup(A2,GPIO.OUT)
GPIO.setup(A1,GPIO.OUT)
GPIO.setup(A0,GPIO.OUT)
GPIO.setup(BStart,GPIO.IN)
GPIO.setup(BStop,GPIO.IN)
GPIO.setup(BReset,GPIO.IN)

#Initialize Variables
#OSC_sequence = 0                #updated by PureData as sequence runs
#chosen_BPM = input("Please choose your BPM: ") #asks for user to input BPM
chosen_BPM = 60
BPM_secs = float(chosen_BPM)/60  #converts BPM to per second
BPM_delay = 1/BPM_secs         #converts to time delay in seconds

#Function definitions
#def button_stop(BStop):


#Wait for Start button press interrupt
#Note: Start is False when triggered
Start = GPIO.wait_for_edge(BStart, GPIO.RISING, timeout = 5000)
GPIO.add_event_detect(BStart, GPIO.RISING)
GPIO.add_event_detect(BStop, GPIO.RISING)
GPIO.add_event_detect(BReset, GPIO.RISING)

while True:
    if Start is None :
        print("Timed out waiting for start")
    else :
        print("Starting Sequencer!")
        current_sequence = 0            #updated by code to keep track of sequence
        reset = False

        #0
        GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #1
        GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue
        
        #2
        GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #3
        GPIO.output(A3,False) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #4
        GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #5
        GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #6
        GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue
        
        #7
        GPIO.output(A3,False) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue
        
        #8
        GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #9
        GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #10
        GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #11
        GPIO.output(A3,True) ; GPIO.output(A2,False) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #12
        GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue
        
        #13
        GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,False) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #14
        GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,False)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

        #15
        GPIO.output(A3,True) ; GPIO.output(A2,True) ; GPIO.output(A1,True) ; GPIO.output(A0,True)
        current_sequence += 1
        print(current_sequence)
        time.sleep(round(BPM_delay,3))
        if GPIO.event_detected(BStop): #if stopped, can play or reset
            while True:
                if GPIO.event_detected(BReset):
                    reset = True
                    break #if reset is detected, break then continue
                if GPIO.event_detected(BStart):
                    break #if start is detected, just break
            if reset:
                continue
            else:
                reset = False
        if GPIO.event_detected(BReset): #if reset, return to beginning
            continue

GPIO.cleanup()
