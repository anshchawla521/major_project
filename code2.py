import os
import numpy as np
import cv2
# import fingerprint_enhancer 


sample = cv2.imread( "./SOCOFing/cam/cap_orginal_finger1_image4_grayscale.jpg")

cv2.imshow("Wihout filter",sample)
cv2.waitKey(0)
cv2.destroyAllWindows()


# sample = cv2.imread( "./SOCOFing/Altered\Altered-Easy/1__M_Left_index_finger_Zcut.BMP")

sample = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)
sample=abs(140-sample)
sample=sample[90:310 , 170:480]
kernel = np.array([[0, -1, 0],
                   [-1, 6,-1],
                   [0, -1, 0]])
    # kernel = np.array([[-1, -1, -1],
    #                [-1, 9,-1],
    #                [-1, -1, -1]])
 
sample = cv2.filter2D(src=sample, ddepth=-1, kernel=kernel)



cv2.imshow("Original", cv2.resize(sample, None, fx=1, fy=1))
cv2.waitKey(0)
cv2.destroyAllWindows()

best_score = counter = 0
filename = image = kp1 = kp2 = mp = None
for file in os.listdir ("SOCOFing/updated"):
     fingerprint_img = cv2.imread("./SOCOFing/updated/" + file)
   #   fingerprint_img=abs(140-fingerprint_img)
   #   fingerprint_img=fingerprint_img[90:310 , 170:480]

     sift = ( cv2.SIFT_create() )
     keypoints_1, des1 = sift.detectAndCompute(sample, None)
     keypoints_2, des2 = sift.detectAndCompute(fingerprint_img, None)
   #   index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)

     matches = cv2.FlannBasedMatcher({"algorithm": 1, "trees": 10}, dict(checks=50)).knnMatch( des1, des2, k=2)
   #   print(matches)

     match_points = []
     for p, q in matches:
        if p.distance < 0.1 * q.distance:   # it is lowe's ratio test checks if two distances are sufficiently different
            match_points.append(p)

     keypoints = 0
     if len(keypoints_1) <= len(keypoints_2):
        keypoints = len(keypoints_1)
     else:
        keypoints = len(keypoints_2)

     if len(match_points) / keypoints * 100 > best_score:
        best_score = len(match_points) / keypoints * 100
        filename = file
        image = fingerprint_img
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points
      
     if best_score >60:  # I have taken 60 % matching to be sufficient to identify if iamge is present or not in db
         break
    

if best_score<40:
   print("Not matched")
else:
 print("Best match:  " + filename)
 print("Best score:  " + str(best_score))
 result = cv2.drawMatches(sample, kp1, image, kp2, mp, None)
 result = cv2.resize(result, None, fx=1, fy=1)
 cv2.imshow("Result", result)
 cv2.waitKey(0)
 cv2.destroyAllWindows()


# Now what we can do is take fingerprint of a person with different orientations and then store them in our db.
# we will store them with their sharpened image
# SO now when user is scanning their fingerprint then also we will apply the crop and sharpening effect and then match
# By doing so we are making sure that at least we get 60 % matching whatever the orientation.
