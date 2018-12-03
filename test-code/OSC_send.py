#This is to test the OSC between python scripts

# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
import time

# Start the system.
osc_startup()

# Make client channels to send packets, "pd" is client channel name
osc_udp_client("localhost", 9001, "pd")
#Create OSC message format ("/address/subaddress", data type, [data])
msg = oscbuildparse.OSCMessage("/test/me", None, [10])
i = 0

while True:
    #Send message on channel "pd"
    osc_send(msg, "pd")
    #OSC process is required to run osc_send
    osc_process()
    print('osc_sent')
    #Resend message every 5 seconds for 20 seconds
    time.sleep(5)
    i = i+1
    if i == 5:
        break

#end osc client
osc_terminate()
print("osc_send done")
