import cv2 as cv

img = cv.imread('photos/cat_large.jpg')

cv.imshow('Cat' , img)

cv.waitKey(3000)
