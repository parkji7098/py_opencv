import cv2
import numpy as np

src= cv2.imread('./data/lena.jpg')

shape = src.shape[0], src.shape[1], 3
b = np.zeros(shape, dtype=np.uint8)
g = np.zeros(shape, dtype=np.uint8)
r = np.zeros(shape, dtype=np.uint8)

blue, green, red = cv2.split(src)
print(blue)
b[:,:,0] = blue
g[:,:,1] = green
r[:,:,2] = red


cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)
cv2.waitKey()
cv2.destroyAllWindows()