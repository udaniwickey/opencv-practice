import cv2 as cv
import numpy as np

img = cv.imread("Resources/blob.jpg")
ret,img = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

kernel = np.ones((3,3),np.uint8)
eroded = cv.erode(img, kernel, iterations=1)

inner_edge = img - eroded
res = np.hstack((img, eroded, inner_edge))
cv.imshow("Boundary", res)
cv.moveWindow("Boundary", 1000, 0)
cv.waitKey(0)

#outer boundary
dilated = cv.dilate(img, kernel, iterations=1)
# inner edge extraction
dilated_edge = dilated - img
# display
res = np.hstack((img, eroded, inner_edge, dilated, dilated_edge))
cv.imshow("Boundary", res)
cv.moveWindow("Boundary", 1000, 0)
cv.waitKey(0)