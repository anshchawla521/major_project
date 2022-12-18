import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import datetime

mapping = {"time":"A",
            "uid":"B",
            "name":"C",
            "sid":"D",
            "phone":"E",
            "direction":"F",
            "remarks":"G"}


import cv2, picamera

reader = SimpleMFRC522()

GOINGOUT = True
GOINGIN = False

workbook = load_workbook(filename="attendance.xlsx")
sheet = workbook["Sheet1"]


direction = GOINGIN

led = 7
touch = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led,GPIO.LOW)

GPIO.setup(touch, GPIO.IN)

camera = picamera.PiCamera()

def getinfo(uid)-> dict:
    return{"name" :"ansh",
            "sid" :"19105031",
            "uid" :"0",
            "phone":"7696046760" }


def match_finger(image)->bool:
    return True







try:
    #Reader.write("Ansh Chawla")
    id , text = reader.read()
    print(id)
    print(text)
    row = workbook.max_row

    person = getinfo(id)
    
    if(person == None):
        raise IndexError("person not found invalid uid")
    else:
        #print(sheet[f'A{row}:F{row}'][0][1].value)
        sheet[f'{mapping["time"]}{row}']= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sheet[f'{mapping["name"]}{row}']= person["name"]
        sheet[f'{mapping["sid"]}{row}']= person["sid"]
        sheet[f'{mapping["uid"]}{row}']= id

        if direction == GOINGOUT:
            sheet[f'{mapping["direction"]}{row}'] = "EXIT" # print name
        elif direction == GOINGIN:
            sheet[f'{mapping["direction"]}{row}'] = "ENTRY" 
            
    matched = False
    if(direction == GOINGIN):
        while not matched:
            if not GPIO.input(touch):
                GPIO.output(led,GPIO.HIGH)
                image_path = "image.jpg"  #address and name of image
                camera.capture(image_path) 

                image = cv2.imread(image_path)
                cv2.imshow("captured",image)
                # call image_check

                GPIO.output(led,GPIO.LOW)
                matched = match_finger(image)
                if cv2.waitKey(0) == ord('s'):
                    break
            
                
    else:
        # open the gate
        pass

finally:
    GPIO.cleanup()