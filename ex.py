import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def hist(img, levels=8):
	hist,bins = np.histogram(img.flatten(), levels,[0, levels])
	plt.hist(img.flatten(), levels,[0, levels], color = 'r')
	plt.xlim([0, levels])
	plt.show()

if __name__ == "__main__":
    img = cv.imread("Resources/wiki.jpg", 0)

    if img is None:
        print("Error: Image not found. Please check the path.")
    else:
        hist(img)

# declare array directly using numpy
arr = np.array([[4,4,4,4,4], [3,4,5,4,3], [3,5,5,5,3],[3,4,5,4,3],[4,4,4,4,4]])
flat = arr.flatten()

levels = 2 ** len(str(bin(np.max(flat)))[2:])