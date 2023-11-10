import numpy as np
import cv2

img = cv2.imread("t-a.JPEG")
cv2.imshow("Orijinal", img)

# img_gri1 = cv2.imread("t-a.JPEG", 0)
# cv2.imshow("Gri Goruntu 1", img_gri1)

# img_gri2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gri Goruntu 2", img_gri2)

# img_gri3 = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
# cv2.imshow("Terse Benzer Goruntu 3", img_gri3)

# #!!!!!!!!!!!!!!!!!!!!!
# r=img[:,:,0]
# g=img[:,:,1]
# b=img[:,:,2]

# gbr_img = cv2.merge((g,b,r))
# #!!!!!!!!!!!!!!!!!!!!!

# cv2.imshow('GBR channel', gbr_img) # RGB bantlarıyla renklendirme

cv2.waitKey(0)