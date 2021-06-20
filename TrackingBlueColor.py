import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    aaa, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # blue_lower = np.array([99, 115, 150], np.uint8)
    # blue_upper = np.array([110, 255, 255], np.uint8)
    blue_lower = np.array([105, 114, 0])  # HSV
    blue_upper = np.array([142, 255, 255])
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    kernal = np.ones((5, 5), "uint8")
    blue = cv2.dilate(blue, kernal)
    cv2.imshow("mask",blue)
    res3 = cv2.bitwise_and(img, img, mask=blue)
    (contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            #img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
            cv2.putText(img, "Blue color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))


    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
