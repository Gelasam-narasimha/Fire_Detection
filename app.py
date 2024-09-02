import cv2
import numpy as np
import streamlit as st


fire_lower=np.array([0,50,50])
fire_upper=np.array([35,255,255])


smoke_lower=np.array([0,50,50])
smoke_upper=np.array([180,50,200])


def detect_fire_and_smoke(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    fire_mask = cv2.inRange(hsv,fire_lower,fire_upper)
    smoke_mask = cv2.inRange(hsv,smoke_lower,smoke_upper)
    contours,_=cv2.findContours(smoke_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    
    contours,_=cv2.findContours(fire_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area=cv2.contourArea(contour)
        if area>500:
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


    contours,_=cv2.findContours(smoke_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area=cv2.contourArea(contour)
        if area>500:
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    return img

st.title("Fire and Smoke Detection")

uploaded_file=st.file_uploader("upload an image")

if uploaded_file is not None:
    file_bytes=np.asarray(bytearray(uploaded_file.read()),dtype=np.uint8)
    img=cv2.imdecode(file_bytes,cv2.IMREAD_COLOR)
    if img is not None:
        detected_image=detect_fire_and_smoke(img)
        st.image(cv2.cvtColor(detected_image,cv2.COLOR_BGR2RGB),caption="detected_fire_and_smoke")
    else:
        st.error("error occured")
        