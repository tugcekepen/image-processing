## Morfolojik İşlemler

## Aşınma

# Yapısal eleman ile Orijinal görüntü, ve(and) mantığı ile işlenir. = Aşınma İşlemi Uygulanmış Görüntü

## Genleşme

# Yapısal eleman ile Orijinal görüntü, veya(or) mantığı ile işlenir. = Genleşme İşlemi Uygulanmış Görüntü

## Açma (Aşınma + Genleşme)

# İlk önce aşınma, sonra genleşme işlemi uygulanır

## Kapama (Genleşme + Aşınma)

# İlk önce genleşme, sonra aşınma işlemi uygulanır

# ---- yapısal elemanlar (3x1) veya (3x3) ----

########################################################
# import numpy as np
# import cv2

# imge = cv2.imread('bilardo_toplari.jpg')
# imge = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

# _, mask = cv2.threshold(imge, 230, 255, cv2.THRESH_BINARY_INV) # - görselin siyah beyaz maskesini çıkarır - eşikleme uygulanıyor

# kernel = np.ones((3,3), np.uint8)
# dilation = cv2.dilate(mask, kernel)
# erosion = cv2.erode(mask, kernel)
# opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel)

# cv2.imshow("original", imge)
# cv2.imshow("masked", mask)

# cv2.imshow("dilation", dilation)
# cv2.imshow("erosion", erosion)
# cv2.imshow("opening", opening)
# cv2.imshow("closing", closing)

# cv2.waitKey(0)
########################################################

########################################################
# import numpy as np
# import cv2

# imge = cv2.imread('yazi.jpg')
# imge = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

# kernel = np.ones((3,3), np.uint8)
# dilation = cv2.dilate(imge, kernel)
# erosion = cv2.erode(imge, kernel)

# cv2.imshow("original", imge)

# cv2.imshow("dilation", dilation)
# cv2.imshow("erosion", erosion)

# # Çıktılarda Dilation ile Erosion çıktılarının zıt, yani normalden ters çıkmasının sebebi, bu görselde beyaz üzerine yapısal eleman işlemi yapması
# # yukarıdaki örnekte görsel maskesi siyah arka plan üzerineydi. bu görsel de beyaz arkaplan üzerine

# cv2.waitKey(0)
########################################################

# Kenarları çizme - sınır eğrisi elde etme - türev işlemi - maskeden erozyon görselini çıkartma

########################################################
# import numpy as np
# import cv2

# imge = cv2.imread('muz.jpg')
# imge = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

# _, mask = cv2.threshold(imge, 220, 255, cv2.THRESH_BINARY_INV)

# kernel = np.ones((5,5), np.uint8)

# erosion = cv2.erode(mask, kernel)

# cv2.imshow("original", imge)
# cv2.imshow("masked", mask)

# cv2.imshow("erosion", erosion)

# cv2.imshow('sinir egrisi cizme', mask-erosion)

# cv2.waitKey(0)
########################################################

########################################################
# import numpy as np
# import cv2

# imge = cv2.imread('samsun.jpg')
# imge = cv2.cvtColor(imge, cv2.COLOR_BGR2GRAY)

# kernel = np.ones((3,3), np.uint8)
# dilation = cv2.dilate(imge, kernel)
# erosion = cv2.erode(imge, kernel)
# opening = cv2.morphologyEx(imge,cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(imge,cv2.MORPH_CLOSE, kernel)
# gradient = cv2.morphologyEx(imge, cv2.MORPH_GRADIENT, kernel)

# cv2.imshow("original", imge)

# cv2.imshow("dilation", dilation)
# cv2.imshow("erosion", erosion)
# cv2.imshow("opening", opening)
# cv2.imshow("closing", closing)
# cv2.imshow("gradient", gradient) # - sınır eğrisi

# cv2.waitKey(0)
########################################################

# sadece kırmızı şapkayı görmek istiyorum? sorularında HSV kullan

import cv2

# mavi renk aralığı HSV
blueLower = (75,100,100)
blueUpper = (130,255,255)

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 480)

while True:
    success, imgOriginal = cap.read()
    if success:
        # blur
        blurred = cv2.GaussianBlur(imgOriginal, (11,11), 0)
        # hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv Image", hsv)
        # mavi için maske oluştur
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask Image", mask)
        # maskenin etrafında kalan görüntüleri sil
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("Mask + erozyon ve genisleme", mask)

    cv2.imshow("Orijinal Tespit", imgOriginal)
    if cv2.waitKey(1) & 0xFF == ord("q"): break