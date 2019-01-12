from cv2 import  *
import numpy as np 

img = imread('../trump.jpg',0)
g = np.zeros((img.shape),dtype='uint8')
g[img > 70] = 255

SE = getStructuringElement(MORPH_RECT,(17,17))
open = morphologyEx(g,MORPH_OPEN,SE)
imshow('test',open)
waitKey(0)