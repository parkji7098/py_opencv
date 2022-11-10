# 0406.py

import cv2
import numpy as np

# cv2.IMREAD_UNCHANGED == -1, 
# cv2.IMREAD_GRAYSCALE == 0, 
# cv2.IMREAD_COLOR == 1
src = cv2.imread('./data/lena.jpg')
# src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
# dst = np.zeros(src.shape, src.dtype)
dst = src.copy()

# 512 x 512

N = 64  #8, 32, 64
# height, width = src.shape
# height, width, channel = src.shape
# height = src.shape[0]
# width = src.shape[1]
height, width = src.shape[0:2]

# 512/64
h = height // N
w = width // N

rect = [(200,200), 200, 200]

startY = rect[0][0] #200
startX = rect[0][1] #200 
endY = startY + rect[1] #400
endX = startX + rect[2] #400

for y in range(startY, endY, h): #range(start, stop, step)
    for x in range(startX, endX, w):
        roi = src[y:y + h, x:x + w]
        dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3] # [B,G,R]

# for i in range(N):
#     for j in range(N):
#         # y = i * h
#         # x = j * w
#         # y = startY + (i * h)
#         # x = startX + (j * w)
#         y = min(startY + (i * h), endY) #min(값1, 값2, ....) 제시된 인자들 중에 가장 작은값을 리턴, 최대값을 유지
#         x = min(startX + (j * w), endX)

#         # 오버헤드.. 필요이상의 부하를 줄때
    
#         # 400,400
#         # print('y: ', y)
#         # print('x: ', x)
#         # if y >= endY and x >= endX:
#         #     break

#         roi = src[y:y + h, x:x + w]
#         # dst[y:y + h, x:x + w] = cv2.mean(roi)[0] # C
#         dst[y:y + h, x:x + w] = cv2.mean(roi)[0:3] # [B,G,R]


cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()