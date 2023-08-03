import cv2
import numpy as np

# imports part of a package
from matplotlib import pyplot as plt

img = cv2.imread("Resources/lambo.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,bw_img = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(bw_img),plt.title('Binary')
plt.xticks([]), plt.yticks([])
plt.show()
