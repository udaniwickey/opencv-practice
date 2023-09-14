import cv2 as cv
import numpy as np

img = cv.imread('Resources/tsukuba.jpg',0)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imshow("Hist", res)
cv.moveWindow("Hist", 1000, 0)
cv.waitKey(0)

equ = cv.equalizeHist(img)
# create a CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

res = np.hstack((img, equ , cl1))
cv.imshow("NEW", res)
cv.moveWindow("NEW", 1000, 0)
cv.waitKey(0)