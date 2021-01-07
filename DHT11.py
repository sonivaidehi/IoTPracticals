import sqlite3
import time
import board
import adafruit_dht
import Adafruit_BBIO.GPIO as GPIO
dhtDevice=adafruit_dht.DHT11(board.D22)
#gpio=17

while True:
    try:
        
        temp_c=dhtDevice.temperature
        temp_f=temp_c * (9 / 5) + 32
        humidity=dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C Humidity: {}%".format(temp_f, temp_c, humidity))
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(5)

