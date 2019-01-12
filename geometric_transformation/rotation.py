from cv2 import  *
import numpy as np 
import imutils

img = imread('../trump.jpg')
rotated = imutils.rotate(img,angle=45,scale=0.5)
imshow('rotation',rotated)
waitKey(0)