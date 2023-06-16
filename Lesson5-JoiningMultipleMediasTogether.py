import cv2
import numpy as np
import myUtliity

# Different image instances copied from Lesson2
'''
imgGray = cv2.imread("Resources/tomioka - Copy.jpg", cv2.IMREAD_GRAYSCALE)
imgGray = cv2.resize(imgGray, (640, 360))
img = cv2.imread("Resources/tomioka - Copy.jpg")
img = cv2.resize(img, (600, 360))
imgBlur = cv2.GaussianBlur(img, (37, 37), 0)
imgCanny = cv2.Canny(img, 300, 300)
kernel = np.ones((3, 3), np.uint8)
imgDilated = cv2.dilate(img, kernel, iterations=2)
imgEroded = cv2.erode(img, kernel, iterations=4)
blank = np.zeros((200, 200), np.uint8)

# Stacked Image
img_array = [[img, imgGray, imgBlur], [imgCanny, imgDilated, imgEroded]]
stacked = myUtliity.stackImages(0.8, img_array)
cv2.imshow("StackedImages", stacked)
cv2.waitKey(0)
'''

# Stacked Webcams
frameWidth = 480
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
video = cv2.VideoCapture("Resources/SampleVideo - Copy.mp4")
video.set(3, frameWidth)
video.set(4, frameHeight)
while True:
    success, inst_img = cap.read()
    flag, inst_vid_img = video.read()
    # DEFINE ALL VERSIONS OF LIVE IMAGES
    # imgGray = cv2.cvtColor(inst_img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(inst_img, (29, 29), 0)
    vidBlur = cv2.GaussianBlur(inst_vid_img, (29, 29), 0)
    imgCanny = cv2.Canny(inst_img, 100, 100)
    vidCanny = cv2.Canny(inst_vid_img, 100, 100)
    kernel = np.ones((3, 3), np.uint8)
    imgDilated = cv2.dilate(inst_img, kernel, iterations=3)
    vidDilated = cv2.dilate(inst_vid_img, kernel, iterations=3)
    imgEroded = cv2.erode(inst_img, kernel, iterations=2)
    blank = np.zeros((200, 200), np.uint8)
    # STACK THESE VERSIONS

    img_array = [[inst_img, imgBlur, imgCanny, imgDilated], [inst_vid_img, vidBlur, vidCanny, vidDilated]]
    stacked = myUtliity.stackImages(0.6, img_array)

    cv2.imshow("StackedWebcam", stacked)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
