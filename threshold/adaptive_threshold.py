import cv2
import numpy as np

def adaptive_thresh_mean(image):
    img = cv.imread(image)
    img = cv.medianBlur(img, 5)
    thresh_am = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)

    return thresh_am


def adaptive_thresh_gaussian(image):
    img = cv.imread(image)
    img = cv.medianBlur(img, 5)
    thresh_ag = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

    return thresh_ag

