import zmq  
import time  
import sys  

  
#port = "5556"  
port = "5555"  
  
# Socket to talk to server 
print ("Collecting updates from weather server...") 
context = zmq.Context()  
socket = context.socket(zmq.SUB)  
#socket.connect ("tcp://localhost:5555")
socket.connect ("tcp://localhost:%s" % port)

topicfilter = "IBEO.LUX4 "  
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
#socket.setsockopt_string(zmq.SUBSCRIBE, 'IBEO')  

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
