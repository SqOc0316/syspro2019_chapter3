import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

i=0
while i<=10:
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(14, GPIO.LOW)
    time.sleep(0.5)
    i+=1


GPIO.cleanup()
