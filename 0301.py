import cv2
import numpy as np

# white 배경 생성
img = np.zeros(shape = (512, 512, 3), dtype = np.uint8) + 255

# 사각형
pt1 = (100, 100)
pt2 = (400, 400)
# Openncv는 BGR 컬러
cv2.rectangle(img, pt1, pt2, (0, 255, 0), -1)

# 선 두개
cv2.line(img, (0, 0), (500, 0), (255, 0, 0), 5)
cv2.line(img, (0, 0), (0, 500), (0, 0, 255), 5)

# 윈도우에 표시
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
