#! /usr/bin/python
# Modified from Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading

import logging
import datetime
from logging.handlers import RotatingFileHandler

gpsd = None #seting the global variable

path = "/home/pi/kyle/log/gps.log"

os.system('clear') #clear the terminal (optional)
 
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(path, maxBytes=1000, backupCount=5)
logger.addHandler(handler)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
      #It may take a second or two to get good data
 
      os.system('clear')
      print "Time: ",gpsd.fix.time,"Latitude: ",gpsd.fix.latitude,"Longitude: ",gpsd.fix.longitude,"Altitude(m): ",gpsd.fix.altitude,"Speed(m/s): ",gpsd.fix.speed,"climb: ",gpsd.fix.climb,"Speed Error(m/s): ",gpsd.fix.eps,"Long Error(m): ",gpsd.fix.epx,"Vert Error(m): ",gpsd.fix.epv,"Course: ",gpsd.fix.track

      #logger.info(gpsd.fix.latitude)
      logger.info("time: %s Latitude: %f Longitude: %f Altitude(m): %f Speed(m/s): %f climb: %f Speed Error(m/s): %f Long Error(m): %f Vert Error(m): %f Course: %f",gpsd.fix.time,gpsd.fix.latitude,gpsd.fix.longitude,gpsd.fix.altitude,gpsd.fix.speed,gpsd.fix.climb,gpsd.fix.eps,gpsd.fix.epx,gpsd.fix.epv,gpsd.fix.track)

      time.sleep(5) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
