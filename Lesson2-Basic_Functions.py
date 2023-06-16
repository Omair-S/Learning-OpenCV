import cv2
import numpy as np
# 1.1 Grayscale - Method1: Directly read a grayscaled image and show it
imgGray = cv2.imread("Resources/tomioka - Copy.jpg", cv2.IMREAD_GRAYSCALE)
imgGray = cv2.resize(imgGray, (640, 360))
cv2.imshow("Window", imgGray)
cv2.waitKey(1)

# 1.2 Grayscale - Method2: Read a colored image, and get a grayscaled image from it
img = cv2.imread("Resources/tomioka - Copy.jpg")
img = cv2.resize(img, (640, 360))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Window", img_gray)
cv2.waitKey(1)
# cv2.destroyWindow("Window")      #closes window

# img = cv2.imread("Resources/tomioka - Copy.jpg")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Window", img)
cv2.waitKey(1)
cv2.destroyWindow("Window")
'''
# 2. Blur
for i in range(20):
    imgBlur = cv2.GaussianBlur(img, (2*i+1, 2*i+1), 0)
    # (2*i+1, 2*i+1) is the kernel size. Should be odd numbers. This shows magnitude of blurriness.
    cv2.waitKey(100)
    cv2.imshow("Window", imgBlur)
'''
# 3. Edge Detection (Outline)
imgCanny = cv2.Canny(img, 300, 300)
cv2.imshow("NewWindow", imgCanny)
cv2.waitKey(10)

# 4. Dilation (Thickening of lines)
kernel = np.ones((3, 3), np.uint8)
imgDilated = cv2.dilate(img, kernel, iterations = 2)
cv2.imshow("DilatedWindow", imgDilated)
cv2.waitKey(10)

# 5. Erosion (Thinning of lines)
imgEroded = cv2.erode(img, kernel, iterations = 4)
cv2.imshow("Eroded", imgEroded)
cv2.waitKey(0)

'''
Dilation and Erosion are opposites of each other but may not completely cancel the effect of each other
'''
