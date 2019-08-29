import cv2

image1 = cv2.imread('messi.jpg')
image2 = cv2.imread('ronaldo.jpg')
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# image = cv2.add(image1, image2)

# image blending
blending = cv2.addWeighted(image1, 0.3, image2, 0.7, 0)
cv2.imshow('image', blending)
cv2.waitKey(0)