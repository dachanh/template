from cv2 import  *
import numpy as np 
import matplotlib.pyplot as plt

img = imread('../trump.jpg')
g = np.zeros((img.shape[:2]) , dtype='uint8')
for h in range(img.shape[0]):
    for w in range(img.shape[1]):
        g[h,w] = (1/2)*(np.amax([img[h,w,0],img[h,w,1],img[h,w,2]]) + np.amin([img[h,w,0],img[h,w,1],img[h,w,2]])) 
hist = calcHist([g],[0],None,[256],[50,100])
plt.subplot(1,2,1)
plt.plot(hist,color='r')
plt.title('hist')
plt.xlim([50,100])
plt.show()
imshow('img',g)
waitKey(0)

