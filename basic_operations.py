import cv2

# accessing
image = cv2.imread('ronaldo.jpg')
px = image[0, 0]
# print(px)
# accessing just one blue
blue = image[0, 0, 0]
print(blue)
# accessing RED value
red = image.item(10, 10, 2)
print(red)
# modifying RED value
image.itemset((10, 10, 2), 100)
print(image.item(10, 10, 2))
# accessing image properties
# shape
print(image.shape)
# size
print(image.size)
# type
print(image.dtype)
# splitting
b, g, r = cv2.split(image)
image = cv2.merge((b, g, r))