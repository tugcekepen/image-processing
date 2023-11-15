import numpy as np 
import cv2 
from sklearn import preprocessing as p
import matplotlib.pyplot as plt

img = cv2.imread("yatLimani.JPEG")
img = cv2.resize(img, (300, 500)) #Boyutlandırma
cv2.imshow('Orijinal',img)


'''KONTRAST GERME'''
# mn = np.min(img)
# mx = np.max(img)
# im1 = (img-mn)/(mx-mn)
# cv2.imshow("Kontrast Germe-1",im1)

def rescale(foto):
    foto.astype(float)
    foto -= np.min(foto)
    foto /= np.max(foto)
    return (255*foto).astype(np.uint8)


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

def log_donusumu(r, c):
    r = r.astype(float)
    s = c * np.log(1 + r)
    s = rescale(s)
    return s

# log_foto1 = log_donusumu(img, 1)
# log_foto2 = log_donusumu(img, 5)

# yan_yana_gosterim = np.hstack((log_foto1, log_foto2))

# cv2.imshow("Log", yan_yana_gosterim)

# print(np.max(img[700:750,50:100]))
# print(np.min(img[700:750,50:100]))
# print(np.max(log_foto1[700:750,50:100]))
# print(np.min(log_foto1[700:750,50:100]))


'''GAMMA DÜZELTME'''  # 𝑠 = c × 𝑟^𝛾
'''
• Gama < 1 ise: daha parlak çıktı değerlerine göre ağırlıklandırılır.
• Gama = 1 ise (varsayılan): eşleme doğrusaldır.
• Gama > 1 ise: daha koyu çıktı değerlerine göre ağırlıklandırılır.
'''
# gamma = 2
# gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8')
# cv2.imshow('log_image-3', gamma_corrected)

def kuvvet_donusumu(r, c, gamma):
    r = r.astype(float)
    s = c * (r ** gamma)
    s = rescale(s)
    return s

# gamma_degerleri = [1, 0.6, 0.2]
# kuvvet_fotograflari = []

# for gamma in gamma_degerleri:
#     kuvvet_fotograflari.append(kuvvet_donusumu(img, 1, gamma))

# satir1 = np.hstack((img, kuvvet_fotograflari[0]))
# satir2 = np.hstack((kuvvet_fotograflari[1], kuvvet_fotograflari[2]))
# yan_yana_gosterim = np.vstack((satir1, satir2))

# cv2.imshow("KUVVET", yan_yana_gosterim)


'''BİT DÜZELTME''' # 𝑠 = 𝑟 / 2^𝑏
# b = 2
# bit_img = img >> b
# bit_img = bit_img.astype(np.uint8)
# cv2.imshow("Bit Duzeltme",bit_img)

cv2.waitKey(0)