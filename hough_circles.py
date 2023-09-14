import cv2 as cv
import numpy as np

img = cv.imread('Resources/blob.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)
cimg = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)

circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

res = np.hstack((img, cimg))
cv.imshow("HoughCircles", res)
cv.moveWindow("HoughCircles", 1000, 0)
cv.waitKey(0)