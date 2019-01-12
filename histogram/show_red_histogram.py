from cv2 import  *
import numpy as np
import matplotlib.pyplot as plt 


I =  imread('../trump.jpg')
J =  imread('../silicon_valley.jpg')

red_I = calcHist([I],[2],None,[256],[0,256])
red_J = calcHist([J],[2],None,[256],[0,256])

plt.subplot(1,2,1)
plt.plot(red_I,color = 'r')
plt.title('histogram I')
plt.xlim([0,256])

plt.subplot(1,2,2)
plt.plot(red_J,color = 'r')
plt.title('histogram J')
plt.xlim([0,256])

plt.show()