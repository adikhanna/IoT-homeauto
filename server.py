#!/usr/bin/python
import socket

s = socket.socket() #makes socket
host = '192.168.2.120' #ip of raspberry pi
port = 43510 #port being used
s.bind((host, port)) #binds socket between server and client 

s.listen(5) #listening for connections

while True: #while connected to client
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('Thank you for connecting') #sends string from server to client
  c.close()
