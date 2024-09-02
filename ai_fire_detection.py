import cv2
import numpy as np
import streamlit as st


img = cv2.imread("Zaca3.jpg", flags=-1)

# print(img)

cv2.imshow("image",img)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("hsvimage",hsv)

fire_lower=np.array([0,50,50])
fire_upper=np.array([35,255,255])

fire_mask = cv2.inRange(hsv,fire_lower,fire_upper)

cv2.imshow("maskedimage",fire_mask)

# contours,_=cv2.findContours(fire_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# for contour in contours:
#     area=cv2.contourArea(contour)
#     if area>500:
#         x,y,w,h=cv2.boundingRect(contour)
#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# cv2.imshow('contours',img)


smoke_lower=np.array([0,50,50])
smoke_upper=np.array([180,50,200])


smoke_mask = cv2.inRange(hsv,smoke_lower,smoke_upper)


# smoke
contours,_=cv2.findContours(smoke_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area=cv2.contourArea(contour)
    if area>500:
        x,y,w,h=cv2.boundingRect(contour)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('smoke',img)




cv2.waitKey(0)

cv2.destroyAllWindows()

