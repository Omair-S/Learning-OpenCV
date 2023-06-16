import cv2
import numpy as np
import myUtliity


def empty(a):
    pass


def getContours_v1(input_img, output_img):
    contours, hierarchy = cv2.findContours(input_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(output_img, contours, -1, (255, 0, 0), 3)


def getContours_v2(input_img, output_img):
    # Draws contours only if area of contour is greater than 1000
    contours, hierarchy = cv2.findContours(input_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(output_img, cnt, -1, (255, 0, 0), 3)


def getContours_v3(input_img, output_img):
    # Draw contours while also counting corner points, labels included
    contours, hierarchy = cv2.findContours(input_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > cv2.getTrackbarPos("MinArea", "Parameters"):
            cv2.drawContours(output_img, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            labelPoint = "Points:" + str(len(approx))
            labelArea = "Area: " + str(area)

            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(output_img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(output_img, labelPoint, (x, y+h+30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            cv2.putText(output_img, labelArea, (x, y + h + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)


# Setting up Trackbar
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 540, 120)

cv2.createTrackbar("Parameter1", "Parameters", 150, 255, empty)
cv2.createTrackbar("Parameter2", "Parameters", 255, 255, empty)
cv2.createTrackbar("MinArea", "Parameters", 1500, 10000, empty)

# Initializing Webcam
cap = cv2.VideoCapture(1)
frameWidth, frameHeight = 640, 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    imgBlur = cv2.GaussianBlur(img, (11, 11), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Parameter1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Parameter2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)

    kernel = np.ones((5, 5))
    imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)         # Edge detection on this image
    blank = np.zeros((200, 200), np.uint8)

    imgContour = img.copy()
    getContours_v3(imgDilated, imgContour)
    hstack = myUtliity.stackImages(0.6, [[img, imgDilated], [imgContour, imgCanny]])
    cv2.imshow("Result", hstack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
