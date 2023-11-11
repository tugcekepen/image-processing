import numpy as np
import cv2

'''RENK UZAYI VE DÖNÜŞÜMLERİ'''

img = cv2.imread("sahil.JPEG",0)
img = cv2.resize(img, (500, 750)) #Boyutlandırma  # dsize = (sütun, satır)
cv2.imshow('Orijinal',img)

print(img.shape) # (satır, sütun) çıktısı veriyor
print(img.size)
print(img.dtype)


'''ROTATION : Temelde bir görüntünün belirlenen bir açı kadar döndürülmesi işlemidir.'''
rows,cols = img.shape #(750,500)
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)       # -- 
rot = cv2.warpAffine(img,M,(cols, rows))
cv2.imshow('rotation', rot)


'''FLIP : Bir görüntünün yatay veya dikey olarak çevrilmesi işlemidir. Yatay ve Dikey Çevirme İşlemleri'''
# imgFlip = cv2.flip(img,-1)
# cv2.imshow('Cevirme',imgFlip)
# - Görüntüyü X ekseni çevresinde çevirmek için: 0 (Sıfır) - (dikey çevirme)
# - Y ekseni çevresinde döndürme için: 1 - (yatay çevirme)
# - Her iki eksenin etrafında döndürmek için: -1


'''TRANSLATION : Bir görüntünün belirli bir oranda kaydırılması işlemidir. (x,y) düzleminde görüntünün (a,b) değerleri ile ötelenmesidir.'''
# rows,cols = img.shape
# M = np.float32([[1,0,100],[0,1,50]])
# trans = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('rotation', trans)


'''PERSPEKTİF DÖNÜŞÜMÜ'''
# rows,cols,ch = img.shape

# pts1 = np.float32([[40,26],[425,30],[9,445],[475,441]]) # Perspektifi alınacak çerçevenin noktaları
# pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) # Perspektif ile taşınacak noktalar

# M = cv2.getPerspectiveTransform(pts1,pts2)

# per = cv2.warpPerspective(img,M,(300,300))

# plt.subplot(121),plt.imshow(img),plt.title('input')
# plt.subplot(122),plt.imshow(per),plt.title('output')
# plt.show()


# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 =np.float32([[10,100],[200,50],[100,250]])

# M = cv2.getAffineTransform(pts1,pts2)

# per = cv2.warpAffine(img,M,(cols,rows))

# plt.subplot(121),plt.imshow(img),plt.title('input')
# plt.subplot(122),plt.imshow(per),plt.title('output')
# plt.show()


'''RESİM KIRPMA'''
# imgCrop1 = img[0:200, 200:500] #[satırStart:satırEnd, sütunStart:sütunEnd]
# cv2.imshow('Cropped 1',imgCrop1)

# imgCrop2=img[:100,:300]
# cv2.imshow('Cropped 2',imgCrop2)


'''CIE'''
'''
Avusturya, Viyana'da 1913 yılında kurulan CIE Uluslararası Aydınlatma Komisyonu (International Commission on Illumination)
-genellikle Fransızca ismi olan 'Commission internationale de l'éclairage' adının ilk harfleri CIE şeklinde kullanılır-
ışık, aydınlatma, renk ve renk uzayları konusunda uluslararası tek otoritedir.

CIE 1931 renk uzayları;
elektromanyetik görünür spektrumda, fiziksel saf renkler (dalgaboyları) ile insan renk görüşünde fiziksel algılanan renkler arasında tanımlanmış ilk sayısal oluşumdur.
'''


'''HSV RENK UZAYI : Hue, Saturation ve Value'''
# hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# cv2.imshow("HSV Goruntu", hsv_img)
# H = hsv_img[:,:,1]
# S = hsv_img[:,1,:]
# V = hsv_img[1,:,:]
# cv2.imshow("H Goruntu", H)
# cv2.imshow("S Goruntu", S)
# cv2.imshow("V Goruntu", V)

'''DİĞER RENK UZAYLARI'''
# xyz_img = cv2.cvtColor(img,cv2.COLOR_RGB2XYZ) #Diğer bütün renk evrenlerinin temel yapısını oluşturan modeldir.
# lab_img = cv2.cvtColor(img,cv2.COLOR_RGB2LAB) #LAB dijital ortam için renklere bir dil vermek adına geliştirilen uluslararası bir standart türüdür. L aydınlık (Lightness) A ile B ise renk bileşenlerini temsil eder.
# ycbcr_img = cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb)
# X = xyz_img[:,:,1]
# Y = xyz_img[:,1,:]
# Z = xyz_img[1,:,:]
# L = lab_img[:,:,1]
# A = lab_img[:,1,:]
# B = lab_img[1,:,:]

# cv2.imshow("xyz",xyz_img)
# cv2.imshow("lab",lab_img)
# cv2.imshow("ycbcr",ycbcr_img)
# cv2.imshow("X",X)
# cv2.imshow("Y",Y)
# cv2.imshow("Z",Z)
# cv2.imshow("l",L)
# cv2.imshow("A",A)
# cv2.imshow("B",B)


cv2.waitKey(0)