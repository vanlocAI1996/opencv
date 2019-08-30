import cv2

image1 = cv2.imread('ronaldo.jpg')
image2 = cv2.imread('opencv_logo.png')

image1 = cv2.resize(image1, (300, 300))
image2 = cv2.resize(image2, (300, 300))
rows, cols, channels = image1.shape
roi = image1[0:rows, 0:cols]

img2gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(image2, image2, mask=mask)
dst = cv2.add(img1_bg, img2_fg)

cv2.imshow("Window", dst)
cv2.waitKey(0)




