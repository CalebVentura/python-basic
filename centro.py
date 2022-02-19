import cv2 as cv
import numpy as np

# Change it with your absiolute path for the image
image = cv.imread("clock2.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY_INV)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
blank = np.zeros(thresh.shape[:2], dtype='uint8')
cv.drawContours(blank, contours, -1, (255, 0, 0), 1)

for i in contours:
    M = cv.moments(i)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        # cv.drawContours(image, [i], -1, (0, 255, 0), 2)
        cv.circle(image, (cx, cy), 7, (0, 0, 255), -1)
        # cv.putText(image, "center", (cx - 20, cy - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    # print(f"x: {cx} y: {cy}")

# View original picture
cv.imshow('Original', image)
cv.imshow('Scale of grises', thresh)
cv.imshow('Black and white clock', blank)
cv.waitKey(0)
cv.destroyAllWindows()
