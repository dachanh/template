import cv2
import numpy as np 
import matplotlib.pyplot as plt


kernel = np.array([[0,1,1,1,0],
                    [1,2,2,2,1],
                    [1,1,5,1,1],
                    [1,2,2,2,1],
                    [0,1,1,1,0]],dtype='uint8')

sum = np.einsum()


cv2.imshow()
cv2.waitkey(0)