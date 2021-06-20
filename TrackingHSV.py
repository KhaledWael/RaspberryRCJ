import cv2
import numpy as np

#img = cv2.imread("D:/Khaled/images/greenSquare.png")
cap = cv2.VideoCapture(0)



def empty(img):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("Hue_min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue_max", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat_min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat_max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value_min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value_max", "HSV", 255, 255, empty)
while True:
    rVal, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # cv2.imshow("img", img)
    cv2.imshow("img_hsv", img_hsv)
    h_max = cv2.getTrackbarPos("Hue_max", "HSV")
    h_min = cv2.getTrackbarPos("Hue_min", "HSV")
    s_min = cv2.getTrackbarPos("Sat_min", "HSV")
    s_max = cv2.getTrackbarPos("Sat_max", "HSV")
    v_min = cv2.getTrackbarPos("Value_min", "HSV")
    v_max = cv2.getTrackbarPos("Value_max", "HSV")

    lower_color = np.array([h_min, s_min, v_min])
    upper_color = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower_color, upper_color)
    res = cv2.bitwise_and(img,img, mask=mask)

    cv2.imshow("mask", mask)
    cv2.imshow("res",res)
    (contours, hierarchy) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            #img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
            cv2.putText(img, "color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))

    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
