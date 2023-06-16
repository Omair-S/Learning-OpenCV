import cv2
import numpy as np
import myUtliity
'''
HSV - Hue Saturation Value

'''
# TRACKBARS
def empty(a):
   pass


cv2.namedWindow("Trackbars")        # Creating a window named "Trackbars"
cv2.resizeWindow("Trackbars", 640, 240)         # Resize the "Trackbars" window
# Creating Trackbars inside the window
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("SAT Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Value Min", "Trackbars", 0, 255, empty)

# Initializing Webcam
frameWidth, frameHeight = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
while True:
    success, inst_img = cap.read()
    inst_img_HSV = cv2.cvtColor(inst_img, cv2.COLOR_BGR2HSV)        # Generating a corresponding HSV image

    # Assigning values from trackbars to different variables
    hue_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    hue_max = 179
    SAT_min = cv2.getTrackbarPos("SAT Min", "Trackbars")
    SAT_max = 255
    Value_min = cv2.getTrackbarPos("Value Min", "Trackbars")
    Value_max = 255

    lower = np.array([hue_min, SAT_min, Value_min])
    upper = np.array([hue_max, SAT_max, Value_max])

    # Create a mask image
    mask = cv2.inRange(inst_img_HSV, lower, upper)

    result = cv2.bitwise_and(inst_img, inst_img, mask=mask)
    stack = myUtliity.stackImages(0.8, [[inst_img, mask, result]])
    cv2.imshow("Original", stack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
