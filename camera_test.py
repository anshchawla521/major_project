import cv2 
import RPi.GPIO as GPIO
import numpy as np

led = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led,GPIO.HIGH)

cap = cv2.VideoCapture(0)

i = 0
j = 0
try:
    while True:
        success , img = cap.read()
        cv2.imshow("video",img)
        key = cv2.waitKey(1)

        if key == ord('s'):
            break
        if key == ord('i'):
            i = 0
            j = j+1
        if key == ord('c'):
            #cv2.imwrite(f"images/cap_orginal_finger{j}_image{i}.jpg",img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = abs(140-img)
            img = img[90:310, 170:480]
            kernel = np.array([[0, -1, 0],
                            [-1, 6, -1],
                            [0, -1, 0]])
            # kernel = np.array([[-1, -1, -1],
            #                [-1, 9,-1],
            #                [-1, -1, -1]])

            img_gray = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
            
            
    
            cv2.imwrite(f"images/cap_orginal_finger{j}_image{i}_grayscale.jpg",img_gray)
            print(f"images/cap_orginal_finger{j}_image{i}_grayscale.jpg")
            i = i+1
finally:

    GPIO.cleanup()