import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

import cv2, picamera

reader = SimpleMFRC522()



led = 7
touch = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led,GPIO.LOW)

GPIO.setup(touch, GPIO.IN)

camera = picamera.PiCamera()
try:
    #Reader.write("Ansh Chawla")
    id , text = reader.read()
    print(id)
    print(text)


    while True:

        if not GPIO.input(touch):
            GPIO.output(led,GPIO.HIGH)
            image_path = "image.jpg"  #address and name of image
            camera.capture(image_path) 

            image = cv2.imread(image_path)
            cv2.imshow("captured",image)
            GPIO.output(led,GPIO.LOW)
            if cv2.waitKey(0) == ord('s'):
                break

finally:
    GPIO.cleanup()