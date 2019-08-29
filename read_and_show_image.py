import cv2

img = cv2.imread('ronaldo.jpg', 0)
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()