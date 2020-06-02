import numpy as np
import cv2


cap = cv2.VideoCapture('F:\\Intro gratuite.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()


    
    cv2.imshow('APRIL', frame)

    if cv2.waitKey(14) & 0XFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
