# 0404-0405.py

import cv2
import numpy as np

# cv2.IMREAD_UNCHANGED == -1, 
# cv2.IMREAD_GRAYSCALE == 0, 
# cv2.IMREAD_COLOR == 1
img = cv2.imread('./data/lena.jpg')
img[100,200] = [255,0,0] # 컬러(BGR)변경

cv2.imshow('img', img)
# cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindows()