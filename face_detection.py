#Face detection using haar cascades
import cv2 as cv
import numpy as np

#img = cv.imread("F:\sdcard\me\IMG-20201121-WA0018-01.jpeg")
capture = cv.VideoCapture(0)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#r_img = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

#cv.imshow('r_img',r_img)

while True:
    istrue, frame = capture.read()
    
    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=6)


    for(x,y,w,h) in faces_rect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    
    cv.imshow('video',frame)

    print("number of faces found = " + str(len(faces_rect)))

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()


#cv.imshow('detected_img',r_img)

cv.waitKey(0)
