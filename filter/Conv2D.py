from  cv2 import  *
import numpy as np 
import matplotlib.pyplot as plt
I = imread('../trump.jpg')
G = cvtColor(I,COLOR_BGR2GRAY)
M = np.ones((4,4),np.uint8)/16

J = filter2D(G,-1,M)


G = G.astype(np.float)
K = G -J 
U = 0.5 *K + J
U = U.astype(np.uint8)
hist = calcHist([U],[0],None,[256],[0,256])
plt.plot(hist)
plt.xlim([0,256])
plt.show()