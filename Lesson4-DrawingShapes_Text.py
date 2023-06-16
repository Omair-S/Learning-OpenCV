import cv2
import numpy as np

'''
image.shape[0] is height
image.shape[1] is width
image.shape[2] is # of channels


img = np.zeros((512,512)) creates a black image
img = np.ones((512,512)) creates a white image

img = np.zeros((512,512,3)) creates a black image which can be altered to different colors
This creates a matrix of float values. But we only need integer values from 0-255, so we need
unsigned int type of 8 bits. So,
img = np.zeros((512,512,3), np.uint8)
seems to be a good way to initialize a blank image
'''

height, width = 720, 1024
img = np.zeros((height, width, 3), np.uint8)            # black image
img[:] = 112, 53, 10        # change the color of whole image
img[30:690, 30:996] = 112, 73, 0        # change the color of a box inside

# Drawing a line:
'''
Syntax:
    cv2.line(image on which to draw a line, starting point, terminal point, color(BGR), line thickness)
'''
cv2.line(img, (30, 30), (img.shape[1]-30, img.shape[0]-30), (27, 93, 51), 2)
cv2.line(img, (img.shape[1]-30, 30), (30, img.shape[0]-30), (27, 93, 51), 2)

# Drawing a Rectangle:
'''
Syntax:
    cv2.rectangle(image on which to draw a rectangle, top-left corner, bottom-right corner, color(BGR) of outline, outline thickness)
'''
cv2.rectangle(img, (460, 120), (550, 200), (200, 180, 200), 3)
# if instead of a hollow rectangle u need a filled one, replace outline thickness with cv2.FILLED
cv2.rectangle(img, (460, 470), (550, 550), (180, 160, 180), cv2.FILLED)

# Drawing a Circle:
'''
Syntax:
    cv2.circle(image on which to draw a circle, center, radius, color(BGR) of outline, outline thickness)
'''
cv2.circle(img, (512, 360), 75, (14, 62, 144), 3)
cv2.circle(img, (100, 360), 50, (14, 62, 144), cv2.FILLED)

# Adding Text:
'''
Syntax:
    cv2.putText(image on which text is to be added, origin point, font style, font scale, color(BGR), thickness)
'''
cv2.putText(img, "Lesson4-DrawingShapes", (250, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow("ColorImage", img)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.imshow("ColorImage", img)
