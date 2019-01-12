from  cv2 import  *
import numpy as np
I = imread('../trump.jpg')
J = imread('../test.jpg')
J = resize(J,(I.shape[1],I.shape[0]))
k = 120 
b,g,r = split(I)
thresh1 = np.zeros((I.shape[:2]),np.uint8)
thresh2 = np.zeros((I.shape[:2]),np.uint8)
thresh3 = np.zeros((I.shape[:2]),np.uint8)
M = np.zeros((I.shape[:2]),np.uint8)
thresh1[b > k] = 255
thresh2[g > k] = 255
thresh3[r > k] = 255
M = thresh1*thresh2*thresh3
N = bitwise_not(M)
N = N.astype(np.uint8)
K = np.zeros((I.shape),np.uint8)
for it in range(3):
    K[:,:,it] = M*J[:,:,it] + N*I[:,:,it]
imshow('K',K)
waitKey(0)