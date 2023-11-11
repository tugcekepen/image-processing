import numpy as np
import cv2

A=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print("A'nın birinci satır:",A[1])
print("2.satırın 1.elemanı:",A[2][1])

print("-"*50)

A=np.array(range(9))
B=np.array(range(9)).reshape(3,3)
C=np.zeros((6,6),dtype="int")
print(A)
print(B)
print(C)
print(C.shape)

print("-"*50)

A=np.random.randint(5,size=(4,3))
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        print("A[{:},{:}] = {:}".format(i, j, A[i,j]))

print("-"*50)

A=np.array(range(12)).reshape(4,3)
B=A.T #TRANSPOSE
print(A)
print(B)

print("-"*50)

A=np.array(range(12)).reshape(4,3)
B=np.zeros((3,4),dtype="int")
for i in range(len(A)):
    for j in range(len(A[0])):
        B[j][i]=A[i][j]
print(A)
print(len(A))
print(len(A[0]))
print(B)

print("-"*50)

A=np.random.randint(5,size=(4,3))
B=np.random.randint(10,size=(4,3))
toplam=A+B
fark=A-B
print(A)
print(B)
print(toplam)
print(fark)

print("-"*50)

A=np.random.randint(5,size=(4,3))
B=np.random.randint(10,size=(4,3))
carp=A*10
print(A)
print(B)
print(carp)

print("-"*50)

A=np.random.randint(5,size=(4,3))
B=np.random.randint(4,size=(3,4))
A=np.mat(A)
B=np.mat(B)
print(A*B)

print("-"*50)

A=np.random.randint(5,size=(4,3))
B=np.random.randint(4,size=(3,4))
result=np.zeros((5,4),dtype="int")
for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(B.shape[0]):
            result[i][j]+=A[i,k]*B[k,j]
print(A)
print(B)
print(result)

print("-"*50)

A=np.random.randint(10,size=(3,3))
result=0
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        if i==j:
            result+=A[i,j]
print(A)
print(result)

print("-"*50)

img = cv2.imread("t-a.JPEG")
img = cv2.resize(img, (500, 750)) #Boyutlandırma
cv2.imshow("Orijinal", img)

cv2.waitKey(0)

# img_gri1 = cv2.imread("t-a.JPEG", 0)
# cv2.imshow("Gri Goruntu 1", img_gri1)

# img_gri2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gri Goruntu 2", img_gri2)

en,boy,katman = np.shape(img)
gri_img = np.zeros((en,boy,katman),dtype=np.uint8)
for i in range(en):
    for j in range(boy):
        gri_img[i:,j] = img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114
cv2.imshow("Gri Ton",gri_img)

# img_gri3 = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
# cv2.imshow("Terse Benzer Goruntu 3", img_gri3)

''' RGB bantlarıyla renklendirme '''
# r=img[:,:,0]
# g=img[:,:,1]
# b=img[:,:,2]

# gbr_img = cv2.merge((g,b,r))
# #!!!!!!!!!!!!!!!!!!!!!

# cv2.imshow('GBR channel', gbr_img)

cv2.waitKey(0)