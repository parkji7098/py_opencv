import cv2
import numpy as np

src = cv2.imread('./data/Heart10.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', src)

ret, dst = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY) # 임계값(120)에 도달하지못한 것들은 다 0으로 처리
print('ret =', ret) # ret = 120
cv2.imshow('dst', dst)

ret2, dst2 = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # THRESH_OTSU 최적임계값 계산
print('ret2 =', ret2) # ret2 = 175 # 원래 설정한 임계값 200과 상관없이 최적임계값 175를구함
cv2.imshow('dst2', dst2)

ret3, dst3 = cv2.threshold(src, 120, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) # THRESH_BINARY_INV 반전
print('ret3 =', ret3) # ret = 120
cv2.imshow('dst3', dst3)

cv2.waitKey()
cv2.destroyAllWindows()
