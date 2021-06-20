import cv2
import numpy as np

# capturing video through pi camera
cap = cv2.VideoCapture(0)
while True:
    temp,img = cap.read()
    img=cv2.resize(img,(480,240))
    cv2.imshow('img',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break