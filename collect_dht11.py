import logging
import time
import RPi.GPIO as GPIO
import dht11
import datetime
 
from logging.handlers import RotatingFileHandler

# intialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

#read data using pin 4
instance = dht11.DHT11(pin=4)

#set path and name for log files
path = "/home/pi/Desktop/log/dht11.log"

#create rotating log and set level
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

#specify the log size and log file count. 200 bytes will allow 3 logs per file
handler = RotatingFileHandler(path, maxBytes=200, backupCount=5)
logger.addHandler(handler)

#run by default

try:
        while True:
            result = instance.read()
            if result.is_valid():
                #send output to log file
                logger.info("Time " + str(datetime.datetime.now()) + " Temperature: %d F " % ((result.temperature*9/5)+32) + "Humidity: %-3.1f%%"% (result.humidity))
                #send output to shell
                print("Time " + str(datetime.datetime.now()) + " Temperature: %d F " % ((result.temperature*9/5)+32) + "Humidity: %-3.1f%%"% (result.humidity))
                        
            time.sleep(1)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
                        
                        
                        
                        
                        
