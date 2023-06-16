import cv2
import numpy as np

path = "Resources/tomioka - Copy.jpg"
image = cv2.imread(path)
print(image.shape)    # finding the size of image
'''
image.shape[0] is height
image.shape[1] is width
image.shape[2] is # of channels
'''
# RESIZING
width, height = 640, 360
imageResized = cv2.resize(image, (width, height))
cv2.imshow("Resized", imageResized)
cv2.waitKey(10)

# CROPPING
'''
image is actually a matrix of pixels, so to crop an image, 
we can define a range for the pixels which are to be shown.
Syntax:
    imageCropped = image[range for height, range for width]
'''
print(image.shape)
imageCropped = image[0:500, 0:900]
imageCropResize = cv2.resize(imageCropped, (image.shape[1], image.shape[0]))
cv2.imshow("Cropped", imageCropResize)
cv2.waitKey(0)
