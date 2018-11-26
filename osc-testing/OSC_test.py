#This code will test the OSC communication in python using the pyOSC library

# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse

# Start the system.
osc_startup()

# Make client channels to send packets.
osc_udp_client("localhost", 9001, "pd_comms")

# Build a simple message and send it.
msg = oscbuildparse.OSCMessage("/test/me", None, [10])
osc_send(msg, "pd_comms")

# Build a message with autodetection of data types, and send it.
#msg = oscbuildparse.OSCMessage("/test/me", None, ["text", 672, 8.871])
#osc_send(msg, "pd_comms")

# Buils a complete bundle, and postpone its executions by 10 sec.
#exectime = time.time() + 10   # execute in 10 seconds
#msg1 = oscbuildparse.OSCMessage("/sound/levels", None, [1, 5, 3])
#msg2 = oscbuildparse.OSCMessage("/sound/bits", None, [32])
#msg3 = oscbuildparse.OSCMessage("/sound/freq", None, [42000])
#bun = oscbuildparse.OSCBundle(oscbuildparse.unixtime2timetag(exectime),
#                    [msg1, msg2, msg3])
#osc_send(bun, "pd_comms")

def handlerfunction(s, x, y):
    # Will receive message data unpacked in s, x, y
    text = "OSC message received: %s, %s, %s" % (str(s), str(x), str(y))
    print(text)

#def handlerfunction2(address, s, x, y):
    # Will receive message address, and message data flattened in s, x, y
    #text = "OSC message received: %s, %s, %s" % (s, x, y)
    #print(text)

# Make server channels to receive packets.
osc_udp_server("localhost", 9001, "pd_receive")



# Associate Python functions with message address patterns, using default
# argument scheme OSCARG_DATAUNPACK.
# Too, but request the message address pattern before in argscheme
#osc_method("/test/*", handlerfunction2, argscheme=osm.OSCARG_ADDRESS + osm.OSCARG_DATAUNPACK)

# Periodically call osc4py3 processing method in your event loop.
finished = False
while not finished:
    # You can send OSC messages from your event loop too
    #
    osc_method("/test/*", handlerfunction)
    osc_process()
    #
    finished = True

# Properly close the system.
osc_terminate()
print('osc_done')
