from cv2 import  *
import numpy as np

I = imread('../trump.jpg')
J = imread('../silicon_valley.jpg')
K = np.zeros((I.shape),dtype='uint8')
for it in range(3):
    I_cdf = calcHist([I],[it],None,[256],[0,256])
    J_cdf = calcHist([J],[it],None,[256],[0,256])
    I_cumsum = np.cumsum(I_cdf)
    J_cumsum = np.cumsum(J_cdf)
    I_cumsum /= I_cumsum[-1]
    J_cumsum /= J_cumsum[-1]
    LUT = np.zeros((256),dtype='uint8')
    for c in range(255):
        G_J = 0 
        while(J_cumsum[G_J + 1] < I_cumsum[c + 1] and G_J < 255):G_J+=1
        LUT[c] = G_J
    for h in range(I.shape[0]):
        for w in range(I.shape[1]):
            K[h,w,it] = LUT[I[h,w,it]]
imshow('K',K)
waitKey(0)
