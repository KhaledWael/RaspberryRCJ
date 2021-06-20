# This program was made to detect any green object and al the other colors will be black.
# By\ Khaled Wael
# 14/2/2020
# task01 for Line Follower 2020 RCJ

# importing modules
import cv2
import numpy as np

# from serial_communication import *

cap = cv2.VideoCapture(0)
while True:
    aaa, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # blue_lower = np.array([99, 115, 150], np.uint8)  # RGB
    # blue_upper = np.array([110, 255, 255], np.uint8)  # RGB
    blue_lower = np.array([105, 114, 0])  # HSV
    blue_upper = np.array([142, 255, 255])
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    kernal = np.ones((5, 5), "uint8")
    blue = cv2.dilate(blue, kernal)
    res3 = cv2.bitwise_and(img, img, mask=blue)
    cv2.imshow("mask", res3)
    (contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > 300:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(contour)
            print(x,y,w,h)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            #cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
            cv2.putText(img, "Points: " + str(len(approx)), (x + w + 20, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 0, 0), 2)
            cv2.putText(img, "area: " + str(int(area)), (x + w + 20, y + h - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 0, 0), 2)
            if len(approx) == 4:
                cv2.putText(img, "rectangle/square", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                            (255, 0, 0), 2)
                print("square")
                # Serialfn("blue square")
            elif len(approx) == 3:
                cv2.putText(img, "Triangle ", (x + w + 20, y + h + 45), cv2.FONT_ITALIC, 0.7, (255, 0, 0), 2)
                print("Trinagle")
                # Serialfn("blue triangle")
            else:
                cv2.putText(img, "circle", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)
                # Serialfn("blue circle")
    cv2.imshow("shape Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
