import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('photos/park.jpg')
cv.imshow('Cats' , img)

plt.imshow(img)
plt.show()

#BGR to GrayScale 

# gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
# cv.imshow('Gray' , gray)

# #BGR to HSV

# hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV)
# cv.imshow('HSV' , hsv)

# #BGR to L*a*b
# lab = cv.cvtColor(img , cv.COLOR_BGR2LAB)
# cv.imshow('L*a*b' , lab)

# cv.waitKey(0)
