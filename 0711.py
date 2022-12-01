#0711.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

#1
src = cv2.imread('./data/circles2.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

dist = cv2.distanceTransform(bImage, cv2.DIST_L1, 3)
dist8 = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX, dtype= cv2.CV_8U)

cv2.imshow('bImage', bImage)
cv2.imshow('dist8', dist8)

#2
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
print('dist:', minVal, maxVal, minLoc, maxLoc)

# print('test:', dist > maxVal * 0.5)
# mat = (dist > maxVal * 0.5).astype(np.uint8)
# print(cv2.minMaxLoc(mat))

# for y, cols in enumerate(mat):
#     print(cols)

np.ones(dist.shape[:2], np.uint8) * 255

# dist 내에 원소가 maxVal * 0.5 보다 크면 True 아니면 False 구성된 행렬을 반환하고,
# 해당 행렬을 astype(np.uint8)로 변환시 True는 1로 False는 0으로 구성된 행렬된다.
# 해당 행렬에 * 255를 하면 0과 1로 구성된 원소들에 모두 255를 곱한 행렬을 반환한다.

#case1
mask = (dist > maxVal * 0.5).astype(np.uint8) * 255    #이진화, threshold
#case2
mask = np.zeros(dist.shape[:2], np.uint8)
mask[dist > maxVal * 0.5] = 255
#case3
# mask = np.zeros(dist.shape[:2], np.uint8)
# for y, cols in enumerate(dist):
#     for x, col in enumerate(cols):
#         if col > maxVal * 0.5:
#             mask[y,x] = 255


cv2.imshow('mask', mask)

#3
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(mask, mode, method)
print('len(contours)=', len(contours))

markers = np.zeros(shape=src.shape[:2], dtype=np.int32)
for i, cnt in enumerate(contours):
    cv2.drawContours(markers, [cnt], 0, i+1, -1)


#4
dst = src.copy()
cv2.watershed(src, markers)

dst[markers == -1] = [0,0,255]     #경계선
for i in range(len(contours)):
    r = np.random.randint(256)
    g = np.random.randint(256)
    b = np.random.randint(256)
    dst[markers == i+1] = [b,g,r]

dst = cv2.addWeighted(src, 0.4, dst, 0.6, 0)  #합성

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()