import cv2 as cv

# img = cv.imread('photos/cat_large.jpg')

# cv.imshow('Cat' , img)

# cv.waitKey(3000)

capture = cv.VideoCapture('videos/dog.mp4')

while True :
    isTrue , frame = capture.read()
    cv.imshow('Video' , frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
