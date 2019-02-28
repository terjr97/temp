
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
import os

#Assign gpio pins
tempPin = 17
redPin = 27
greenPin = 22
count = 0
#initialize the gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)

#temp and humidity sensor
tempSensor = Adafruit_DHT.DHT11

while True:
        humidity, temperature = Adafruit_DHT.read_retry(tempSensor,
tempPin)
        temperature = temperature * 9/5.0 +32
        if humidity is not None and temperature is not None:
#               tempFahr = '{0:0/1f}*F'.format(temperature)
                print('Temperature = {0:0.1f}*F'.format(temperature, humidity))
        else:
                print('Failed to get reading. Try again!')
	if temperature > 70  and temperature < 80:
		GPIO.output(22,True)
		time.sleep(60)
		GPIO.output(22,False)
	else:
		count = 60
		while count > 0:
			GPIO.output(27,True)
			time.sleep(.5)
			GPIO.output(27,False)
			time.sleep(.5)
			count = count-1
	count = 0
	GPIO.output(22,False)
	GPIO.output(27,False)

