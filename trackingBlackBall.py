import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    aaa, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    black_lower = np.array([0, 0, 0])  # HSV
    black_upper = np.array([179, 95, 89])
    black = cv2.inRange(hsv, black_lower, black_upper)
    kernal = np.ones((5, 5), "uint8")
    black = cv2.dilate(black, kernal)
    cv2.imshow("mask", black)
    res3 = cv2.bitwise_and(img, img, mask=black)
    (contours, hierarchy) = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 300):
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(contour)
            print(x, y, w, h)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
            cv2.putText(img, "Points: " + str(len(approx)), (x + w + 20, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 0, 0), 2)
            cv2.putText(img, "area: " + str(int(area)), (x + w + 20, y + h - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (255, 0, 0), 2)
            if len(approx) != 4 and len(approx) != 3:
                cv2.putText(img, "circle", (x + w + 20, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)
                # Serialfn("blue circle")
    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
