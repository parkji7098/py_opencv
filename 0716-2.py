import cv2
import numpy as np

#1
# src = cv2.imread('./data/circles.jpg')
src = cv2.imread('./data/car_num2.jpg')
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

data = src.reshape((-1,3)).astype(np.float32)

k = 2

term_crit = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, labels, centers = cv2.kmeans(data, k, None, term_crit, 5, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
res = centers[labels.flatten()]     # 1차원 배열로 변환
dst = res.reshape(src.shape)

# gray = cv2.bitwise_not(gray)
ret, res = cv2.threshold(dst, 100, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('res', res)

#2
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(res)
print('ret =', ret)     # 레이블 개수 (배경 포함)
print('labels =', labels)   # 객체에 번호가 지정된 레이블 맵
print('stats =', stats)     # 통계 정보
print('centroids =', centroids)     # 중심점

#3
# dst = np.zeros(src.shape, dtype=src.dtype)
# dst = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# for i in range(1, int(ret)):
#     r = np.random.randint(256)
#     g = np.random.randint(256)
#     b = np.random.randint(256)
#     dst[labels == i] = [b, g, r]

#4
for i in range(1, int(ret)):
    x, y, width, height, area = stats[i]    # area: 면적, 픽셀의 수
    cv2.rectangle(dst, (x, y), (x + width, y + height), (0, 0, 255), 2)

    cx, cy = centroids[i]
    cv2.circle(dst, (int(cx), int(cy)), 5, (255, 0, 0), -1)

cv2.imshow('dst', dst)
cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()