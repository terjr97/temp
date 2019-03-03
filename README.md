How it is working!
See "for explanations"
<<<<<<< HEAD
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import os
import sqlite3 as mydb
import sys
"here we are importing the various data commands we will be needing to build our script "

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
"This is setting up the sqlite database and closing the program if it is not working correctly"

#Assign gpio pins
tempPin = 17
redPin = 27
greenPin = 22
count = 0
"Here we assign the pins for the gpio"

#initialize the gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)
"Here we are actually deciding what the GPIO pins do"

def green(pin):
        GPIO.output(pin,True)
        time.sleep(60)
        GPIO.output(pin,False)

def red(pin):
       GPIO.output(pin,True)
        time.sleep(.5)
        GPIO.output(pin,False)
        time.sleep(.5)
"we define two different outcomes based on the temperature data later so that the pins do different things, the green one simply stays on for 60 seconds while the red one is set to blink."

#temp and humidity sensor
tempSensor = Adafruit_DHT.DHT11
try:
        while True:
                humidity, temperature = Adafruit_DHT.read_retry(tempSensor,tempPi$
                temperature = temperature * 9/5.0 +32
                c.execute('''$temp''')
                if humidity is not None and temperature is not None:
#                       tempFahr = '{0:0/1f}*F'.format(temperature)
                        print('Temperature = {0:0.1f}*F'.format(temperature, humi$
                else:
                        print('Failed to get reading. Try again!')
"The above block of code collects the temperature data and formats it into fereighnheight while the bottom block interprets the data and if it is within the data values specified causes one of two scenarios to play out."
                if temperature > 68  and temperature < 78:
                        green(22)
                else:
                        for i in range(60):
                                red(27)
                GPIO.output(redPin,False)
                GPIO.output(greenPin,False)
 		clear()   

"This except clears everything and makes it as good as new when we decide to stop the program through the console command of ctrl+c"
except KeyboardInterrupt:
        if con:
                con.close()
        GPIO.cleanup()
        os.system('clear')
        print('End of Temperature gathering.')

>>>>>>> 67c7378e190e63e0b569c9b6eb6b5af977a07b92
