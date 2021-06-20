# ti
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    # Take each frame
    rVal, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of green color in HSV
    lower_color = np.array([25, 52, 72])
    upper_color = np.array([102, 255, 200])
    # Threshold the HSV image to get only defined colors
    green = cv2.inRange(hsv, lower_color, upper_color)
    # cv2.imshow('mask', mask)
    kernal = np.ones((5, 5), "uint8")
    green = cv2.dilate(green, kernal)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=green)
    cv2.imshow('frame', frame)
    # cv2.imshow('res', res)
    (contours, hierarchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            print(x,y,w,h)
            #frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
            cv2.putText(frame, "Green color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    cv2.imshow("Color Tracking", frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
