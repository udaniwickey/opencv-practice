import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpeg")
print(img.shape)

imgResize = cv2.resize(img,(600,1000))
print(imgResize.shape)

imgCropped = img[0:1000,1000:2000]

cv2.imshow("Image",img)
#cv2.imshow("Resize Image",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)