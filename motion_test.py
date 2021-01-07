import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.IN)
GPIO.setup(24, GPIO.OUT)

while True:
    input_state = GPIO.input(15)
    if input_state == True:
        print("Motion Detected")
        GPIO.output(24,True)
        time.sleep(1)
        GPIO.output(24,False)
        time.sleep(4)
    else:
        print("No Motion Detected")
        
        