# 0406.py

import cv2
import numpy as np

# cv2.IMREAD_UNCHANGED == -1, 
# cv2.IMREAD_GRAYSCALE == 0, 
# cv2.IMREAD_COLOR == 1
src = cv2.imread('./data/lena.jpg')
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = np.zeros(src.shape, src.dtype)

# 512 x 512

N = 64  #8, 32, 64
# height, width = src.shape
# height, width, channel = src.shape
# height = src.shape[0]
# width = src.shape[1]
height, width = src.shape[0:2]

h = height // N
w = width // N

for i in range(N):
    for j in range(N):
        y = i * h
        x = j * w
        roi = src[y:y + h, x:x + w]
        # dst[y:y + h, x:x + w] = cv2.mean(roi)[0] # C
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3] # [B,G,R]


cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()