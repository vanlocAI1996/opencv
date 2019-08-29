import cv2
import numpy as np

image = np.zeros((512, 512, 3))
# drawing lineb
cv2.line(image, (200, 200), (500, 500), (255, 0, 0), 5)
# drawing rectangle
cv2.rectangle(image, (10, 10), (50, 50), (255, 0, 0), 3)
# drawing circle
cv2.circle(image, (100, 100), 20, (255, 255, 0), 3)
# drawing ellipse
cv2.ellipse(image, (255, 255), (100, 50), 30, 30, 360, 10, 3)
# drawing text
cv2.putText(image, 'Loc is handsome', (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, 0)
cv2.imshow('frame', image)
cv2.waitKey(0)