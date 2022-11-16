import cv2
import numpy as np

# [[9.] # 0과 1의 갯수
#  [3.] # 2와 3의 갯수
#  [2.] # 4와 5의 갯수
#  [2.]] # 6과 7의 갯수

src = np.array([[0, 0, 0, 0],
                [1, 1, 3, 5],
                [6, 1, 1, 3],
                [4, 3, 1, 7]
                ], dtype=np.uint8)

hist = cv2.calcHist(images=[src], channels=[0], mask=None, histSize=[4], ranges=[0,8])
print('hist = ', hist)

backp = cv2.calcBackProject([src], [0], hist, [0,8], scale=1)
print('backp = ', backp)