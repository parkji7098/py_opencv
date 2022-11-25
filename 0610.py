import cv2
import numpy as np

src = cv2.imread('./data/morphology.jpg', cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(shape=cv2.MORPH_RECT, ksize=(3,3))

# 흰색 속에 검은색 잡음 제거
closing = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel, iterations=5) # 침식 -> 팽창

# 흰색 잡음 제거
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel, iterations=5) # 팽창 -> 침식

# 흰색 물체 테두리 검출
gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel) # 팽창 - 침식
# 두꺼운 테두리 검출
# gradient = cv2.morphologyEx(opening, cv2.MORPH_GRADIENT, kernel, iterations=5)

# 검은색 배경속 흰색 점 검출
tophat = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel, iterations=5) # 원본 - opening

# 흰색 물체 속 검은색 점 검출
blackhat = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel, iterations=5) # closing - 원본

cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.imshow('gradient', gradient)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)

cv2.waitKey()
cv2.destroyAllWindows()