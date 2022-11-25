import cv2
import numpy as np

# src = cv2.imread('./data/alphabet.bmp', cv2.IMREAD_GRAYSCALE)
# src = cv2.bitwise_not(src) # 반전
src = cv2.imread('./data/T.jpg', cv2.IMREAD_GRAYSCALE)

ret, A = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY)
skel_dst = np.zeros(src.shape, np.uint8)
shape1 = cv2.MORPH_RECT
# shape1 = cv2.MORPH_CROSS

B = cv2.getStructuringElement(shape=shape1, ksize=(3,3))
done = True
while done:
    erode = cv2.erode(A,B)
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, B)
    tmp = cv2.subtract(erode, opening) # erode - opening
    skel_dst = cv2.bitwise_or(skel_dst, tmp)
    A = erode.copy()
    
    # A가 비어있으면 false
    done = cv2.countNonZero(A) > 0 # countNonZero: 0이 아닌값 카운트
    # done = cv2.countNonZero(A) != 0 # countNonZero: 0이 아닌값 카운트

cv2.imshow('src', src)
cv2.imshow('skel_dst', skel_dst)
cv2.waitKey()
cv2.destroyAllWindows()
