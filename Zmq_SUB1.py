import zmq  
import time  
import sys  

  
#port = "5556"  
port = "5555"  
  
# Socket to talk to server  
context = zmq.Context()  
socket = context.socket(zmq.SUB)  
  
print "Collecting updates from weather server..."  
socket.connect ("tcp://127.0.0.1:5555")  
#socket.bind ("tcp://localhost:%s" % port)
socket.setsockopt(zmq.SUBSCRIBE, "IBEO.LUX4 ")  

#for update_nbr in range (100):
while True:
    string = socket.recv()  
    #topic, messagedata,pub_server_name = string.split()  
    #print topic, messagedata,pub_server_name  
    #szMsg = string.split()
    #print szMsg
    #message = socket.recv()
    #print 'received ',update_nbr,'[',message,']'
    print(string)
