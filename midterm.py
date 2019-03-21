import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import os
import sqlite3 as mydb
import sys

con = None
try:
        con = mydb.connect('timeTemp')
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print "SQLITE version: %s" % data
except mydb.Error, e:

        print "Error %s:" %e.args[0]
        sys.exit(1)


#Assign gpio pins
camPin1 = 13
camPin2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(camPin1, GPIO.IN)
GPIO.setup(camPin2, GPIO.IN)



except KeyboardInterrupt:
        GPIO.cleanup()
        con.close()
        print('End Sensor Gathering')

