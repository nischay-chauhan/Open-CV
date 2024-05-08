import cv2 as cv
import numpy as np
img = cv.imread('photos/park.jpg')

cv.imshow('Boston' , img)

#Trans;ation

def translate(img , x , y):
    transMat = np.float32([[1 , 0 , x] , [0 , 1 , y]])
    dimensions = (img.shape[1] , img.shape[0])
    return cv.warpAffine(img , transMat , dimensions)


translated = translate(img , 100 , -100)
cv.imshow('Translated' , translated)

#rotation 
def rotate(img , angle , rotPoint = None):
    (height , width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2 , height // 2)
    
    return cv.warpAffine(img , cv.getRotationMatrix2D(rotPoint , angle , 1.0) , (width , height))

rotated = rotate(img , -45)
cv.imshow('Rotated' , rotated)

#flip 
def flip(img , flipCode):
    return cv.flip(img , flipCode)

flipped = flip(img , 0)
cv.imshow('Flipped' , flipped)
cv.waitKey(0)