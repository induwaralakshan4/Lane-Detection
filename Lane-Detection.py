import cv2
import numpy as np
video=cv2.VideoCapture('#Samples/road_drive.avi')
while True:
    rat,frame=video.read()
    if rat==False:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    kernel=np.array([[-1,0,1],
                [-2,0,2],
                [-1,0,1]])
    conv=cv2.filter2D(gray,-1,kernel)
    ret,thresh=cv2.threshold(conv,150,255,0)
    thresh[:130,:]=0
    contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>20:
            cv2.drawContours(frame,[cnt],-1,(255,255,255),2)
            rect=cv2.minAreaRect(cnt)
            box=cv2.boxPoints(rect)
            box=np.int64(box)
            cv2.drawContours(frame,[box],-1,(0,0,255),2)
    cv2.imshow('live',frame)
    x=cv2.waitKey(10)
    if x==113:
        break
cv2.destroyAllWindows()
    
