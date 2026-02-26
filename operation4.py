import cv2

image1 = cv2.imread("spiderman.png",cv2.IMREAD_COLOR)
image2 = cv2.imread("octopus.png",cv2.IMREAD_COLOR)
print(image1)

startpoint = (0,0)
endpoint = (300,300)
image = cv2.line(image1,startpoint,endpoint,(125,255,0),9)
cv2.imshow("start and end", image)
cv2.waitKey(0)

sp = (50,50)
ep = (600,600)
image = cv2.rectangle(image2,sp,ep,(0,0,0),-1)
cv2.imshow("rectangle", image)
cv2.waitKey(0)

image2 = cv2.imread("octopus.png",cv2.IMREAD_COLOR)
font = cv2.FONT_HERSHEY_SIMPLEX
origin = (50,50)
image = cv2.putText(image2,'OpenCV',origin,font,1,(0,0,255),2,cv2.LINE_AA)
cv2.imshow("text", image)

sp = (100,100)
image2 = cv2.imread("octopus.png",cv2.IMREAD_COLOR)
image = cv2.circle(image2,sp,100,(0,0,0),-1)
cv2.imshow("circle", image)
cv2.waitKey(0)
image2 = cv2.imread("octopus.png",cv2.IMREAD_COLOR)
image = cv2.circle(image2,sp,100,(0,0,0),10)
cv2.imshow("circle2", image)
cv2.waitKey(0)