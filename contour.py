import cv2 as cv
img = cv.imread('photos/cats.jpg')

cv.imshow('Cats' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

canny = cv.Canny(gray , 125 , 175)
cv.imshow('Canny' , canny)\

contours , heiarchy = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)

cv.waitKey(0)