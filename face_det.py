##test
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (255,255,255), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print(faces)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ix,iy,iw,ih) in eyes:
            cv2.rectangle(roi_color, (ix,iy),(ix+iw,iy+ih), (0,255,255), 2) 
            print(eyes)
        
    cv2.imshow('Image',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
