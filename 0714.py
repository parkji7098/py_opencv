import cv2
import numpy as np

#1
src = cv2.imread('./data/hand.jpg')
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

data = src.reshape((-1,3)).astype(np.float32)

#2
k = 2

# 참고: http://www.gisdeveloper.co.kr/?p=7123

# 종료 조건 타입
# cv2.TERM_CRITERIA_EPS: 주어진 정확도(epsilon 인자)에 도달하면 반복 중단
# cv2.TERM_CRITERIA_MAX_ITER: max_iter 인자에 지정된 횟수만큼 반복하고 중단
# (TERM_CRITERIA_EPS, TERM_CRITERIA_MAX_ITER, 최대 반복할 횟수(정수형), 정확도)
term_crit = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, centers = cv2.kmeans(data, k, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)
print('centers.shape =', centers.shape)
print('labels.shape =', labels.shape)
print('ret =', ret)

#3
centers = np.uint8(centers)
res = centers[labels.flatten()]     # 1차원 배열로 변환
dst = res.reshape(src.shape)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()