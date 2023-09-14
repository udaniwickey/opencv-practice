import cv2 as cv
import numpy as np

img = cv.imread('Resources/traffic.jpg',0)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
cv.imshow("Binary", th1)
cv.moveWindow("Binary", 1000, 0)
cv.waitKey(0)

# blur and remove noise
blur = cv.medianBlur(img,5)
# inversion
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
blur = cv.medianBlur(img,5)
ret,th2 = cv.threshold(blur,127,255,cv.THRESH_BINARY_INV)
res = np.hstack((img, blur, th1, th2))
cv.imshow("Binary", res)
cv.moveWindow("Binary", 1000, 0)
cv.waitKey(0)

# Experiment with others
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
res = np.hstack((img, th1, th2))
cv.imshow("Threshold", res)
cv.moveWindow("Threshold", 1000, 0)
cv.waitKey(0)

# equalization
equ = cv.equalizeHist(img)
ret,th1 = cv.threshold(equ,127,255,cv.THRESH_BINARY_INV)
res = np.hstack((img, equ, th1))
cv.imshow("Binary", res)
cv.moveWindow("Binary", 1000, 0)
cv.waitKey(0)

# Experiment with others
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
res = np.hstack((img, th1, th2))
cv.imshow("Threshold", res)
cv.moveWindow("Threshold", 1000, 0)
cv.waitKey(0)

# equalization
equ = cv.equalizeHist(img)
ret,th1 = cv.threshold(equ,127,255,cv.THRESH_BINARY_INV)
res = np.hstack((img, equ, th1))
cv.imshow("Binary", res)
cv.moveWindow("Binary", 1000, 0)
cv.waitKey(0)