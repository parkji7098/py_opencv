import cv2
import numpy as np

src1 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8) + 255

dst1 = 255 - src1
dst2 = cv2.subtract(src2, src1)

# CMP_GT: > , CMP_GE: >=, CMP_LT: <, CMP_LE: <=, CMP_EQ: ==, CMP_NE: !=
# compare() 두 행렬의 각 위치의 화소를 비교 (옵션에 따라 같은지 다른지 큰지 작은지 )
# compare() 의 결과는 비교한 결과 해당위치에 담긴 행렬 (true = 255, false = 0)
dst3 = cv2.compare(dst1, dst2, cv2.CMP_NE) # 참이면 255, 거짓이면 0 반환
n = cv2.countNonZero(dst3)

print('n =', n)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()