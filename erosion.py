import cv2
import numpy as np

img = cv2.imread("Resources/dialation.png")
print(img.shape)
se = np.ones((5,5),np.uint8)

img_erosion = cv2.erode(img, se, iterations=1)
img_dilation = cv2.dilate(img, se, iterations=1)
res = np.hstack((img, img_erosion, img_dilation))
cv2.imshow("Results of the Erosion and Dilation",res)
cv2.waitKey(0)

img_open = cv2.erode(img_dilation, se,iterations=1)
img_close = cv2.dilate(img_erosion, se, iterations=1)
res = np.hstack((img, img_erosion, img_dilation, img_open, img_close))
cv2.imshow("Results of the Erosion,Dilation, Open and Close",res)
cv2.waitKey(0)