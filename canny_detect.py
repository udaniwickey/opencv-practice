import cv2
import numpy as np
from scipy import ndimage
import sys


def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size + 1, -size:size + 1]
    normal = 1 / (2.0 * np.pi * sigma ** 2)
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma * 2))) * normal
    return g


def sobel_filters(img):
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    ix = ndimage.convolve(img, kx)
    iy = ndimage.convolve(img, ky)

    g = np.hypot(ix, iy)
    g = (g / g.max() * 255).astype(np.uint8)
    theta = np.arctan2(iy, ix)

    return g, theta


def non_max_suppression(img, d):
    m, n = img.shape
    z = np.zeros((m, n), dtype=np.uint8)  # Change data type to uint8
    angle = d * 180. / np.pi
    angle[angle < 0] += 180

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            try:
                q = 255
                r = 255

                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = img[i, j + 1]
                    r = img[i, j - 1]
                elif 22.5 <= angle[i, j] < 67.5:
                    q = img[i + 1, j - 1]
                    r = img[i - 1, j + 1]
                elif 67.5 <= angle[i, j] < 112.5:
                    q = img[i + 1, j]
                    r = img[i - 1, j]
                elif 112.5 <= angle[i, j] < 157.5:
                    q = img[i - 1, j - 1]
                    r = img[i + 1, j + 1]

                if (img[i, j] >= q) and (img[i, j] >= r):
                    z[i, j] = img[i, j]
                else:
                    z[i, j] = 0
            except IndexError:
                pass

    return z


def threshold(img, low_threshold_ratio=0.05, high_threshold_ratio=0.09):
    high_threshold = img.max() * high_threshold_ratio
    low_threshold = high_threshold * low_threshold_ratio
    m, n = img.shape
    res = np.zeros((m, n), dtype=np.uint8)  # Change data type to uint8
    weak = np.uint8(25)  # Change data type to uint8
    strong = np.uint8(255)  # Change data type to uint8

    strong_i, strong_j = np.where(img >= high_threshold)
    _, zeros_j = np.where(img < low_threshold)
    weak_i, weak_j = np.where((img <= high_threshold) & (img >= low_threshold))

    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak

    return res, weak, strong


def hysteresis(img, weak, strong=255):
    m, n = img.shape
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if img[i, j] == weak:
                try:
                    if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong) or
                            (img[i, j - 1] == strong) or (img[i, j + 1] == strong) or
                            (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                    img[i - 1, j + 1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError:
                    pass
    return img


def canny_edge_detect(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if image is None:
            print("Error: Unable to load the image.")
            return

        # Step 1: Noise Reduction
        blurred = cv2.GaussianBlur(image, (5, 5), 0)

        # Step 2: Gradient Calculation
        gradient_magnitude, gradient_direction = sobel_filters(blurred)

        # Step 3: Non-Maximum Suppression
        suppressed = non_max_suppression(gradient_magnitude, gradient_direction)

        # Step 4: Double Thresholding
        threshold_image, weak, strong = threshold(suppressed)

        # Step 5: Edge Tracking by Hysteresis
        final_edge_image = hysteresis(threshold_image, weak)

        # Display the images
        cv2.imshow("Original Image", image)
        cv2.imshow("Gaussian Blur", blurred)
        cv2.imshow("Gradient Magnitude", gradient_magnitude)
        cv2.imshow("Non-Maximum Suppression", suppressed)
        cv2.imshow("Threshold Image", threshold_image)
        cv2.imshow("Final Edge Image", final_edge_image)

        # Wait for a key press and then close all windows
        cv2.waitKey(0)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: canny_edge_detection.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        canny_edge_detect(image_path)
