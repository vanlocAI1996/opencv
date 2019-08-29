import cv2
import numpy as np

image = np.zeros((500, 500, 3)) + 255
cv2.ellipse(image, (255, 150), (30, 30), 120, 0, 300, (0, 0, 255), 15)
cv2.ellipse(image, (210, 220), (30, 30), 30, 0, 300, (0, 255, 0), 15)
cv2.ellipse(image, (290, 220), (30, 30), 300, 0, 300, (255, 0, 0), 15)
cv2.imshow('window', image)
cv2.waitKey(0)