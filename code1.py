import RPi.GPIO as GPIO
import cv2, picamera
led = 3
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led, GPIO.OUT)
GPIO.output(led,0)

touch = 5

GPIO.setup(touch, GPIO.IN)

while touch:
    pass

if touch == 0:
    GPIO.output(led,1)
    camera = picamera.PiCamera()
    image_path = "image.jpg"  #address and name of image
    camera.capture(image_path) 

    image = cv2.imread(image_path)
    length_l, length_r, height_u, height_d = 0,0,0,0
    cropped_image = image[height_u:height_d,length_l:length_r]
    cv2.imwrite(image_path, cropped_image)
    GPIO.output(led,0)