#importing the necesarry data
import time
import RPi.GPIO as GPIO
import os
import sqlite3 as mydb
import sys

con = None
try:
        con = mydb.connect('room.db')
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        data = cur.fetchone()
        print "SQLITE version: %s" % data
except mydb.Error, e:

        print "Error %s:" %e.args[0]
        sys.exit(1)

#Assign gpio pins. 13 is for entering. 26 is for leaving.
camPin1 = 13
camPin2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(camPin1, GPIO.IN)
GPIO.setup(camPin2, GPIO.IN)
#let the camera have time to set up
time.sleep(10)
print "test starting now"
people = 0
try:
	while True:
		current = people
                if GPIO.input(camPin1):
			people = people + 1
			time.sleep(4)
			print current
		if GPIO.input(camPin2):
			people = people - 1
			time.sleep(4)
			print current
		#decrease in room population
		if current > people:
			current = current
                        con.execute("INSERT INTO room VALUES ('now', 'leaving' , people);")

		#increase in room population
		if current < people:
			con.execute("INSERT INTO room VALUES ('now', 'entering' , 'people');")
                        con.commit()


except KeyboardInterrupt:
        GPIO.cleanup()
        con.close()
        print('End Sensor Gathering')

