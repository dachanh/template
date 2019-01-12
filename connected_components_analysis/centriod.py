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
print('contours : ',str(len(contours)))
for it , cnt in enumerate(contours):
    M = cv2.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    area = cv2.contourArea(cnt)
    print(str(it) + " cx = " + str(cx ) + " cy = " + str(cy) + " Area = " + str(area))
# eccentricity





