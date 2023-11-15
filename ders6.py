import numpy as np
import cv2

img = cv2.imread("cimen.JPEG")
img = cv2.resize(img, (500, 750)) #Boyutlandırma
cv2.imshow('Orijinal',img)


'''HİSTOGRAM'''
'''
Bir görüntünün histogramı, o görüntü hakkında önemli bilgiler verir.
Bunlar:
• Koyu (Karanlık) bir görüntünün histogram grafiğinin düşük gri seviye bölgesine yığılacağı açıktır.
• Parlak (Açık renk) düzgün bir görüntünün histogram grafiğinin büyük gri seviye bölgesine yığılacağı açıktır.
• Eğer histogram bir bölgeye yığılmış ise ( yani gri seviye ekseninin belirli bir bölgesine) bu görüntünün kontrastı kötüdür denir.
• İyi kontraslı bir resmin histogram grafiği tüm gri seviye değerlerine eşit yayılmış olduğunu açıklar.
'''

'''HİSTOGRAM EŞİTLEME'''



cv2.waitKey(0)