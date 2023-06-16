import cv2          # open source computer vision library
import numpy
print("Version: ", cv2.__version__)

# IMAGE READING
img = cv2.imread("Resources/tomioka - copy.jpg")    # read image
img = cv2.resize(img, (640, 480))
cv2.imshow("Window", img)                            # show image
cv2.waitKey(2000)
# waitKey() takes in time in ms. 0 is considered as inf.

# VIDEO READING
# 640x480 seems to be the standard for webcam and videos :)
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/SampleVideo - Copy.mp4")
#
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

# cv2.VideoCapture(0) plays video 0 from default camera, i.e., webcam
while True:
    success, inst_img = cap.read()
    inst_img = cv2.resize(inst_img, (frameWidth, frameHeight))      # resize each frame
    cv2.imshow("Window", inst_img)

    if cv2.waitKey(2) & 0xFF == ord('q'):                   # quit the video when key 'q' is pressed or when the video ends
        break
    # waitKey(1) for a 30fps video and waitKey(2) for 60fps one.
    # waitKey(1) for better webcam frame rate.
