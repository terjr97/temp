#import libraries
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os

#assign pins
tempPin = 17

t = 1

#temp and humidity sensor
tempSensor = Adafruit_DHT.DHT11

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Error reading sensor')

	return tempFahr

try:
	with open("/log/templog.csv", "a") as log
		while t == 1:
			data = readF(tempPin)
			print (data)
			time.sleep(60)
			log.write("str(data)")

except KeyboardInterrupt:
	os.system('clear')
	print('thank you for using this temp device')
	GPIO.cleanup()
