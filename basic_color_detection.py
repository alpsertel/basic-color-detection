import cv2
import numpy as np

image = cv2.imread('sample.png')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


#This program has been set for detecting RED COLOR ONLY now.
#Color values on the next 2 lines can be adjusted to detect the desired color range.

lower_red = np.array([178, 178, 0])
upper_red = np.array([255, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)

mask_inv = cv2.bitwise_not(mask)

final = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('foto', image)
cv2.imshow('detection', mask)
cv2.imshow('final', final)


cv2.waitKey(0)
cv2.destroyAllWindows()
