import cv2
rgb_img = cv2.imread('5.jpg')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print rgb_img.shape
gray_image = cv2.cvtColor(rgb_img,cv2.COLOR_BGR2GRAY)
gray_image1 = gray_image


face_rects = face_cascade.detectMultiScale(gray_image)
#print face_rects

for (i,j,k,l) in face_rects:
    print i,j,k,l
    cv2.rectangle(gray_image1,(i,j),(i+k,j+l),(255,0,0),2)
    roi_gray = gray_image[j:j+l, i:i+k]
    cv2.imshow('face',roi_gray)

eye_rects = eye_cascade.detectMultiScale(gray_image)
for (x,y,w,h) in eye_rects:
    print x,y,w,h
    cv2.rectangle(gray_image1,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray_image[y:y+h, x:x+w]
    cv2.imshow('eye',roi_gray)

nose_rects = nose_cascade.detectMultiScale(gray_image)
#print nose_rects
for (a,b,c,d) in nose_rects:
    print a,b,c,d
    if(b<y):
        cv2.rectangle(gray_image1,(a,b),(a+c,b+d),(255,0,0),2)
        roi_gray = gray_image[b:b+d, a:a+c]
        cv2.imshow('nose',roi_gray)

mouth_rects = mouth_cascade.detectMultiScale(gray_image, 1.3, 11)
for (p,q,r,s) in mouth_rects:
    print p,q,r,s
    if(q<y):
        cv2.rectangle(gray_image1,(p,q),(p+r,q+s),(255,0,0),2)
        roi_gray = gray_image[q:q+s, p:p+r]
        cv2.imshow('mouth',roi_gray)

cv2.imshow('figure',gray_image)

cv2.waitKey(0)