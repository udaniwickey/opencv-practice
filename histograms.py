import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def hist(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.show()

def hist_with_levels(img, levels=8):
    hist, bins = np.histogram(img.flatten(), levels, [0, levels])
    plt.hist(img.flatten(), levels, [0, levels], color='r')
    plt.xlim([0, levels])
    plt.show()

# declare array directly using numpy
arr = np.array([[4,4,4,4,4], [3,4,5,4,3], [3,5,5,5,3],[3,4,5,4,3],[4,4,4,4,4]])
flat = arr.flatten()

levels = 2 ** len(str(bin(np.max(flat)))[2:])

# back to basics
hist = np.zeros(levels, np.int8)
# compute bins
for i in flat:
    hist[i] += 1

bins = hist # The bins should now contain the frequency of each intensity value in the image

print(bins)
