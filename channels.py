import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats' , img)

average = cv.blur(img , (3 , 3))
cv.imshow('Average Blur' , average)
cv.waitKey(0)