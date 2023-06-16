import cv2
import numpy as np
import myUtliity

# TRACKBARS
def empty(a):
   pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Blue Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Green Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Red Min", "Trackbars", 0, 255, empty)
# Initializing Webcam
frameWidth, frameHeight = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, inst_img = cap.read()

    blue_min = cv2.getTrackbarPos("Blue Min", "Trackbars")
    blue_max = 255
    green_min = cv2.getTrackbarPos("Green Min", "Trackbars")
    green_max = 255
    red_min = cv2.getTrackbarPos("Red Min", "Trackbars")
    red_max = 255

    lower = np.array([blue_min, green_min, red_min])
    upper = np.array([blue_max, green_max, red_max])

    mask = cv2.inRange(inst_img, lower, upper)
    result = cv2.bitwise_and(inst_img, inst_img, mask=mask)
    stack = myUtliity.stackImages(0.8, [[inst_img, mask, result]])
    cv2.imshow("Original", stack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
