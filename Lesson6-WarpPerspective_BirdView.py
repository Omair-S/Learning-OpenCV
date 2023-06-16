import cv2
import numpy as np

# Objective: From an image of cards, we need to extract a 2D bird view of one of the cards, top one to be specific.

cards_img = cv2.imread("Resources/kings cards.png")
width, height = 500, 700

# Open the image in paint, hover over the corner points of the card and note them down. Then, make an array of these points.
pts1 = np.float32([[680, 234], [1003, 279], [615, 688], [937, 734]])

# Next, make another array specifying the order of points in previous array.
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Perform transformation
matrix = cv2.getPerspectiveTransform(pts1, pts2)
transformed_img = cv2.warpPerspective(cards_img, matrix, (width, height))

cv2.imshow("Cards", cards_img)
cv2.imshow("Perspective", transformed_img)

cv2.waitKey(0)
