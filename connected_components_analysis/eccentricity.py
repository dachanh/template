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
    ellipse = cv2.fitEllipse(cnt)
    (center , axes , orientation) = ellipse
    # eccentricity = sqrt( 1 - (ma/MA)^2) --- ma= minor axis --- MA= major axis
    eccentricity = np.sqrt(1 - (min(axes)/max(axes))**2)
    print("majoraxis lenghth", max(axes))
    print("minoraxis length", min(axes))
    print("orientation ", orientation)
    print("eccentricity",eccentricity)

# eccentricity





