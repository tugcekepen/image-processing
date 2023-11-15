import numpy as np
import cv2

img = np.array([
    [94, 60, 31, 91, 23, 61],
    [41, 18, 57, 54, 66, 56],
    [46, 47, 36, 53, 39, 73],
    [71, 85,  7, 20, 33, 60],
    [24, 30, 78, 43, 60, 52],
    [27, 50, 80, 39, 88,  4]
])

img = img.astype(np.uint8)
print(img)

img2 = np.array([
    [255, 180, 63, 242, 35, 187],
    [97, 21, 159, 145, 194, 152],
    [111, 117, 77, 138, 91, 207],
    [200, 228, 14, 28, 69, 180],
    [42, 56, 214, 104, 180, 131],
    [49, 124, 222, 91, 236, 7],
])
img2 = img2.astype(np.uint8)
print(img2)


cv2.imshow('Orijinal',img)
cv2.imshow("Kendi Histim", img2)
img_hist = cv2.equalizeHist(img)
print(img_hist)
cv2.imshow("Hist", img_hist)







cv2.waitKey(0)