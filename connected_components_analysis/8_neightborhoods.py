from skimage import measure
from skimage.filters import threshold_local
import matplotlib.pyplot as plt
import numpy as np
import  cv2
import random

img = cv2.imread('../shapes.png',0)
res = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
thresh = cv2.threshold(img, 50, 255, 0)[1]
_, contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(res, [cnt],0,(random.randint(0,255),random.randint(0,255) ,random.randint(0,255)),-1)
cv2.imshow('res',res)
cv2.waitKey(0)
