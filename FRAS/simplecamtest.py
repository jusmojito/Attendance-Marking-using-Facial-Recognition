import numpy as np
import cv2
url = 'http://192.168.0.102:8080/video'

cap = cv2.VideoCapture(url)
 
while(True):
    ret, frame = cap.read()
    #frame = cv2.flip(frame, 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
