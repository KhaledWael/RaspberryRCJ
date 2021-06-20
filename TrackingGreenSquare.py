# This program was made to detect any green object and al the other colors will be black.
# By\ Khaled Wael
# 14/2/2020
# task01 for Line Follower 2020 RCJ

# importing modules
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    aaa, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102,255,200], np.uint8)
    green = cv2.inRange(hsv, green_lower, green_upper)
    kernal = np.ones((5, 5), "uint8")
    green = cv2.dilate(green, kernal)
    res3 = cv2.bitwise_and(img, img, mask=green)
    (contours, hierarchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        # if (area > 300):
        #   x, y, w, h = cv2.boundingRect(contour)
        #  img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.putText(img, "Green  color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
            #cv2.drawContours(img, [approx], 0, 0, 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            if len(approx) == 4 and (area > 300):
                a, b, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (a, b), (a + w, b + h), (0, 255, 0), 2)
                cv2.putText(img, "green square", (a, b), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break