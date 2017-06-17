#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os
from datetime import datetime

###http://www.bristolwatch.com/ele2/74HC595_cylon.htm # там лежит оригинал

#!/usr/bin/env python
# File rpi_74HC595_cylon.py
# Use left and right shift resister functions.
# 8 LEDs connected to 74HC595
# http://www.bristolwatch.com/index.htm
# by Lewis Loflin lewis@sullivan-county.com

# access to GPIO must be through root
###import RPi.GPIO as GPIO
####import time


LATCH = 11 # Pin 12 Latch clock
CLK = 12 # Pin 11 shift clock
dataBit = 7 # Pin 14 A

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(LATCH, GPIO.OUT) # P0 
GPIO.setup(CLK, GPIO.OUT) # P1 
GPIO.setup(dataBit, GPIO.OUT) # P7 

##GPIO.output(LATCH,False),
##GPIO.output(CLK,False),
##GPIO.output(dataBit,False),

# Setup IO
GPIO.output(11, 0)
GPIO.output(CLK, 0)




def pulseCLK():
    GPIO.output(CLK, 1)
   # time.sleep(.01) 
    GPIO.output(CLK, 0)
    return

def serLatch():
    GPIO.output(LATCH, 1)
   # time.sleep(.01)
    GPIO.output(LATCH, 0)
    return

# MSB out first!
def ssrWrite(value):
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           GPIO.output(dataBit, 1) # data bit HIGH
        else:
           GPIO.output(dataBit, 0) # data bit LOW
        pulseCLK()        
        value = value << 0x01 # shift left
    serLatch() # output byte
    return 

    



# convert an 8-bit number to a binary string
def convBinary(value):
    binaryValue = '0b'
    for  x in range(0,8):
        temp = value & 0x80
        if temp == 0x80:
           binaryValue = binaryValue + '1'
        else:
            binaryValue = binaryValue + '0'
        value = value << 1
    return binaryValue


while 1:
    temp = 1
    for j in range(0, 8 ):
        ssrWrite(temp)
        temp = temp << 1
        time.sleep(.2)

    for j in range(0, 8 ):
        temp = temp >> 1
        ssrWrite(temp)
        time.sleep(.2)  

print "Good by!"
exit
