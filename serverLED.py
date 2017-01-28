#!/usr/bin/python
import socket
import RPi.GPIO as GPIO

s = socket.socket()
host = '192.168.2.120'
port = 7001
s.bind((host, port))
s.listen(5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

while True:
	c, addr = s.accept()
	print ('Got connection from', addr)
	c.send('Thank you for connecting! Type 1 to turn LED on or 0 to turn LED off!')
	data1 = int(c.recv(1024))
	if data1 == 1:
		GPIO.output(18, GPIO.HIGH)
	data2 = int(c.recv(1024))
	if data2 == 0:
		GPIO.output(18, GPIO.LOW)
	GPIO.cleanup()		

