import cv2
import numpy as np 
import matplotlib.pyplot as plt 


I = cv2.imread('trump.jpg')
J = cv2.imread('silicon_valley.jpg')

hist_r_I = cv2.calcHist([I],[2],None,[256],[0,256])
hist_r_J = cv2.calcHist([J],[2],None,[256],[0,256])
plt.subplot(3,3,1)
plt.plot(hist_r_I,color='r')
plt.title('Red I')
plt.subplot(3,3,2)
plt.plot(hist_r_J,color='r')
plt.title('Red J')
K = np.zeros((I.shape),np.uint8)
for c in range(3):
    hist_r_I = cv2.calcHist([I],[c],None,[256],[0,256])
    hist_r_J = cv2.calcHist([J],[c],None,[256],[0,256])
    cumsum_I = np.cumsum(hist_r_I)
    cumsum_J = np.cumsum(hist_r_J)
    cumsum_I /= cumsum_I[255]
    cumsum_J /= cumsum_J[255]
    LUT = np.zeros((256),np.uint8)
    for it in range(255):
        g = 0
        while (cumsum_J[g + 1] < cumsum_I[it +1] and g < 254): g += 1
        LUT[it] = g
    for h in range(I.shape[0]):
        for w in range(I.shape[1]):
            K[h,w,c] = LUT[I[h,w,c]]
"""
plt.subplot(3,3,3)
plt.imshow(I)
plt.title('I')
plt.subplot(3,3,4)
plt.imshow(J)
plt.title('J')
plt.subplot(3,3,5)
plt.imshow(K)
plt.title('K')
"""
cv2.imshow('K',K)
#plt.show()
cv2.waitKey(0)
