# 0402.py

import cv2
import numpy as np

# cv2.IMREAD_UNCHANGED == -1, 
# cv2.IMREAD_GRAYSCALE == 0, 
# cv2.IMREAD_COLOR == 1
# img = cv2.imread('./data/lena.jpg')
img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./data/lena.jpg', 0)

# print('img: ', img)

print('img.shape =', img.shape)

img = img.flatten()
print('img.shape =', img.shape)

img = img.reshape(-1, 512, 512)
print('img.shape =', img.shape)

# print('img: ', img)
img = img[0]

# dsize를 절대값으로 넣을지, fx, fy를 이용해 상대값으로 넣을지 하나만..
# img = cv2.resize(img, (0, 0), fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()