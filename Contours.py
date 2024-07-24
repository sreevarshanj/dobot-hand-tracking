import cv2
import numpy as np
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    _,image=cap.read()
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_color=np.array([100,150,150])
    upper_color=np.array([140,255,255])
    mask=cv2.inRange(hsv,lower_color,upper_color)
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        M=cv2.moments(contour)
        if M["m00"]!=0:
            cX=int(M["m10"]/M["m00"])
            cY=int(M["m01"]/M["m00"])
        else:
            cX,cY=0,0
        cv2.circle(image,(cX,cY),5,(0,0,255),-1)
        print(cX,cY)

    cv2.drawContours(image,contours,-1,(0,255,0),3)
    cv2.imshow("Contours",image)
    cv2.waitKey(1)