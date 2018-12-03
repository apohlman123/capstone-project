#This code is to recieve OSC in Python
import time
osc_startup()

def handlerfunction(z, x, y):
    # Will receive message data unpacked in s, x, y
    text = "OSC message received: %s, %s, %s" % (str(z), str(x), str(y))
    print(text)

# Make server channels to receive packets.
osc_udp_server("localhost", 9001, "pd_receive")
i = 0

osc_method("/test/*", handlerfunction)
osc_process()

osc_terminate()
