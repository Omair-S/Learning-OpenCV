import cv2
import numpy as np

# circles for corner points enclosing a rectangle
circles = np.zeros((4, 2), np.int32)
counter = 0
# Mouse call back function
def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print((x, y))
        circles[counter] = x, y
        counter = counter + 1

webcam = cv2.VideoCapture(1)
# cards_img = cv2.imread("Resources/kings cards.png")
while True:
    success, cards_img = webcam.read()
    if counter == 4:            # if all 4 points are selected, then:
        width, height = 1280, 720
        # Array of clicked corner points
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        # Array specifying the order of points in previous array
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        # Perform transformation
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        transformed_img = cv2.warpPerspective(cards_img, matrix, (width, height))

        cv2.imshow("Perspective", transformed_img)

    for i in range(4):              # print circles where left-clicked on "Cards" image.
        cv2.circle(cards_img, (circles[i][0], circles[i][1]), 2, (0, 255, 0), 5, cv2.FILLED)
    cv2.imshow("Cards", cards_img)
    cv2.setMouseCallback("Cards", mousePoints)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
