import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    aaa, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red_lower = np.array([0, 120, 77])  # HSV
    red_upper = np.array([179, 255, 160])
    red = cv2.inRange(hsv, red_lower, red_upper)
    kernal = np.ones((5, 5), "uint8")
    red = cv2.dilate(red, kernal)
    cv2.imshow("mask",red)
    res3 = cv2.bitwise_and(img, img, mask=red)
    (contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            #img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
            cv2.putText(img, "Red color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))


    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()