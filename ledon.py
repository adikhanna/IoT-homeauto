#!/usr/bin/python
import RPi.GPIO as GPIO  
import time    

def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return  
  
GPIO.setmode(GPIO.BOARD)    
GPIO.setup(18, GPIO.OUT)    

for i in range(0,10):  
        blink(18)  

GPIO.cleanup()
