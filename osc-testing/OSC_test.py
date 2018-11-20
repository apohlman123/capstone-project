#This code will test the OSC communication in python using the pyOSC library

import OSC

#Note: there is an open socket with these attributes on my computer RIP
#[57120].socket.close()
#'127.0.0.1'
client = OSC.OSCClient()
client.connect(('localhost', 9001) )

client.send(OSC.OSCMessage('/user/1', [1.0, 2.0, 3.0 ]))


def OSC_handler(addr, tags, data, client_address):
    text = "OSCMessage '%s' from %s: " % (addr, client_address)
    text += str(data)
    print(text)

if __name__ == '__main__':
    s = OSC.OSCServer(('localhost', 9001))  # listen on localhost, port 57120
    s.addMsgHandler('/user/1', OSC_handler)     # call handler() for OSC messages received with the /startup address

print('did it work yet')


#client.send( OSCMessage("/user/2", [2.0, 3.0, 4.0 ] ) )
#client.send( OSCMessage("/user/3", [2.0, 3.0, 3.1 ] ) )
#client.send( OSCMessage("/user/4", [3.2, 3.4, 6.0 ] ) )

#client.send( OSCMessage("/quit") )
