import zmq  
import sys 
import random
import time

port = '5555'  
pub_server_name = 'pub-server01'  
context = zmq.Context()  
socket = context.socket(zmq.PUB)  
socket.bind('tcp://*:%s'%port)  
      
while True:  
   topic = random.randrange(9999,10005)  
   messagedata = random.randrange(1,215)-80  
   print ('topic:%s messagedata:%s'%(topic,messagedata))  
   socket.send_string('%d %d %s'%(topic,messagedata,pub_server_name))  
   time.sleep(1)  
