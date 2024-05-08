import cv2 as cv

img = cv.imread('photos/cat.jpg')
#converting into grayScale

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

blur = cv.GaussianBlur(gray , (5 , 5) , cv.BORDER_DEFAULT)
cv.imshow('Blur' , blur)

#edge Cascade

canny = cv.Canny(blur , 125 , 175)
cv.imshow('Canny' , canny)

#dilating the image
dilated = cv.dilate(canny , (3 , 3) , iterations = 3)
cv.imshow('Dilated' , dilated)

#eroding
eroding = cv.erode(dilated , (3 , 3) , iterations = 3)
cv.imshow('Eroded' , eroding)

#resize
resize = cv.resize(img , (500 , 500) , interpolation = cv.INTER_CUBIC)

#cropping
crop = img[50:200 , 200:400]


cv.waitKey(0) 