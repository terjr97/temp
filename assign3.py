
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import os
import sqlite3 as mydb
import sys

con = None
try:
	con = mydb.connect('test.db')
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	data = cur.fetchone()
	print "SQLITE version: %s" % data 
except mydb.Error, e:

	print "Error %s:" %e.args[0]
	sys.exit(1)


#Assign gpio pins
tempPin = 17
redPin = 27
greenPin = 22
count = 0

#initialize the gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

def green(pin):
	GPIO.output(pin,True)
	time.sleep(60)
	GPIO.output(pin,False)

def red(pin):
	GPIO.output(pin,True)
	time.sleep(.5)
	GPIO.output(pin,False)
	time.sleep(.5)

#temp and humidity sensor
tempSensor = Adafruit_DHT.DHT11
try:
	while True:
        	humidity, temperature = Adafruit_DHT.read_retry(tempSensor,tempPin)
        	temperature = temperature * 9/5.0 +32
		c.execute('''$temp''')
        	if humidity is not None and temperature is not None:
#       	        tempFahr = '{0:0/1f}*F'.format(temperature)
        	        print('Temperature = {0:0.1f}*F'.format(temperature, humidity))
        	else:
        	        print('Failed to get reading. Try again!')
		if temperature > 68  and temperature < 78:
			green(22)
		else:
			for i in range(60):
				red(27)
		GPIO.output(redPin,False)
		GPIO.output(greenPin,False)
		clear()

except KeyboardInterrupt:
	if con:
		con.close()
	GPIO.cleanup()
	os.system('clear')
	print('End of Temperature gathering.')
