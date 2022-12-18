import cv2 


cap = cv2.VideoCapture(0)

i = 0
j = 0

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
        cv2.imwrite(f"images/cap_orginal_finger{j}_image{i}.jpg",img)
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"images/cap_orginal_finger{j}_image{i}_grayscale.jpg",img_gray)
        print(f"images/cap_orginal_finger{j}_image{i}_grayscale.jpg")
        i = i+1
