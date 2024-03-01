import cv2

'''RENK UZAYI VE DÖNÜŞÜMLERİ'''

img = cv2.imread("sahil.JPEG",0)
img = cv2.resize(img, (500, 750)) #Boyutlandırma  # dsize = (sütun, satır)
cv2.imshow('Orijinal',img)


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


## -----------
# COLOR_RGB2HLS
# COLOR_RGB2YUV
# YIQ Renk Uzayı
# [[Y],
#  [I],
#  [Q]] = [[0.299, 0.587, 0.114],
#          [0.596, -0.274, -0.322],
#          [0.211, -0.523, 0.312]] * [[R],
#                                     [G],
#                                     [B]]
# [[R],
#  [G],
#  [B]] = [[1, 0.956, 0.621],
#          [1, -0.272, -0.647],
#          [1, -1.106, 1.703]] * [[Y],
#                                 [I],
#                                 [Q]]
# COLORMAP


cv2.waitKey(0)