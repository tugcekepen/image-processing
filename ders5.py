import numpy as np 
import cv2 
from sklearn import preprocessing as p
import matplotlib.pyplot as plt

img = cv2.imread("cimen.JPEG")
img = cv2.resize(img, (500, 750)) #Boyutlandırma
cv2.imshow('Orijinal',img)


'''KONTRAST GERME'''
# mn = np.min(img)
# mx = np.max(img)
# im1 = (img-mn)/(mx-mn)
# cv2.imshow("Kontrast Germe-1",im1)



'''----YOĞUNLUK DÖNÜŞÜMLERİ----'''
'''
3 çeşit yoğun dönüşüm işlemi mevcuttur. Bunlar:
➢Linear dönüşümler,
➢Logaritmik dönüşümler,
➢Kuvvet dönüşümleri
'''

'''LINEAR DÖNÜŞÜM''' # 𝑠 = 𝑟 × 𝑎 + 𝑏
# a = 1.5
# b = 50
# lin_img = a*img + b
# lin_img = lin_img.astype(np.uint8)
# cv2.imshow("Linear Image",lin_img)


'''NEGATİF GÖRÜNTÜ''' #  𝑠 = 𝐿 − 1 − 𝑟
# mx = np.max(img)
# neg_img = mx-img  # veya 255-img
# cv2.imshow("Negatif Goruntu",neg_img)


'''LOG DÖNÜŞÜMÜ UYGULANMASI''' #  𝑠 = 𝑐 × 𝑙𝑜𝑔(1 + 𝑟)
# im1=img.astype(float)
# c = 255 / np.log(1 + np.max(im1))
# log_img=c*np.log(1+im1)
# log_img1=(log_img).astype(np.uint8)
# cv2.imshow("LOG Image-1",log_img1)


'''GAMMA DÜZELTME'''  # 𝑠 = 𝐿 − 1 × 𝑟^𝛾
'''
• Gama < 1 ise: daha parlak çıktı değerlerine göre ağırlıklandırılır.
• Gama = 1 ise (varsayılan): eşleme doğrusaldır.
• Gama > 1 ise: daha koyu çıktı değerlerine göre ağırlıklandırılır.
'''
# gamma = 2
# gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
# cv2.imshow('log_image-3', gamma_corrected)



'''BİT DÜZELTME''' # 𝑠 = 𝑟 / 2^𝑏
# b = 2
# bit_img = img >> b
# bit_img = bit_img.astype(np.uint8)
# cv2.imshow("Bit Duzeltme",bit_img)

cv2.waitKey(0)