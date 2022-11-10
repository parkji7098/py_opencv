# 0407.py

import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(src)
print('roi =', roi)


N = 64  #8, 32, 64
height, width = src.shape[0:2]

# 512/64 = 8
bh = height // N
bw = width // N


def mosaic(src, roi, bh, bw, flag=cv2.IMREAD_COLOR):
    img = src.copy()

    # roi = (x축, y축, 넓이, 높이)
    if roi != (0,0,0,0):
        roiX, roiY, roiW, roiH = roi

        # 화소, 픽셀 의 시작위치, 끝 위치, 모자이크 블럭의 크기
        for y in range(roiY, roiY + roiH, bh): #range(start, stop, step)
            for x in range(roiX, roiX + roiW, bw):

                # print(f'y,x ({y},{x})')
                blockROI = src[y:y + bh, x:x + bw] #매트릭스, 행렬
                # print('blockROI: ', blockROI)

                # 1,1,1              2,2,2
                # 2,2,2  =  평균 2 = 2,2,2
                # 3,3,3              2,2,2
                if flag == cv2.IMREAD_GRAYSCALE:
                    img[y:y + bh, x:x + bw] = cv2.mean(blockROI)[0] # gray
                else:
                    img[y:y + bh, x:x + bw] = cv2.mean(blockROI)[0:3] # [B,G,R]

    return img



if roi != (0,0,0,0):
    roiX, roiY, roiW, roiH = roi

    img = mosaic(src, roi, bh, bw, cv2.IMREAD_GRAYSCALE)
#     # cv2.blur()

#     # 관심영역을 축소 -> 관심영역을 본래사이즈로 확대 (resize() 사용)
#     roiMat = src[roiY:roiY + roiH, roiX:roiX + roiW]
#     roiMat = cv2.resize(roiMat, (0, 0), fx=0.1, fy=0.1)
#     roiMat = cv2.resize(roiMat, (roiW, roiH))

#     img = src.copy()
#     img[roiY:roiY + roiH, roiX:roiX + roiW] = roiMat


    cv2.imshow('img', img)
    cv2.waitKey()

cv2.destroyAllWindows()