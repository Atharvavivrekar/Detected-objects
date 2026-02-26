import cv2 
import numpy as np
image = cv2.imread("spiderman.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray,(3,3))
detected_objects = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT,1,20,param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
if detected_objects is not None:
    detected_objects = np.uint16(np.around(detected_objects))
    for i in detected_objects:
        x,y,r = i[0], i[1], i[2]
        print(i)
        cv2.circle(image,(x,y),r,(0,0,255),2)
        cv2.circle(image,(x,y),1,(255,0,0),3)
        cv2.imshow("detected circles", image)
        cv2.waitKey(0)
