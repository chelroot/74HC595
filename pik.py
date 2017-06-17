#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT)
#GPIO.setup(9, GPIO.OUT)

while True :
 GPIO.output(8,True),
 time.sleep(0.5)
 GPIO.output(8,False),
 #GPIO.output(9,True),
 time.sleep(1)
 #GPIO.output(9,False),
