import cv2

# Load image, grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread("D:/Khaled/images/code/detect_face02.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Find bounding box
x, y, w, h = cv2.boundingRect(thresh)
cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)

w_px = 2.54 / 110
w_cm = int(w * w_px)
h_px = 2.54 / 110
h_cm = int(h * h_px)
cv2.putText(image, "w={}cm,h={}cm".format(w_cm, h_cm), (x+25, y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 2)
cv2.imshow("thresh", thresh)
cv2.imshow("image", image)
cv2.waitKey()
