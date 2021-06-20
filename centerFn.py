import cv2
import numpy as np

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
    (cnts, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        area = cv2.contourArea(c)
        if (area > 300):
            # Obtain bounding box coordinates and draw rectangle
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Find center coordinate and draw center point
            M = cv2.moments(c)
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img, (cx, cy), 2, (255, 0, 0), -1)
            print('Center: ({}, {})'.format(cx, cy))
            # max x-cam is 640 & max y-cam is 480
            if cx < 320 and cy > 240:
                print("bottom-left")
            if cx < 320 and cy < 240:
                print("top-left")
            if cx > 320 and cy > 240:
                print("Bottom-right")
            if cx > 320 and cy < 240:
                print("Top-right")
    cv2.imshow('image', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
