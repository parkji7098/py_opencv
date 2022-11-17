import cv2
import numpy as np

src = cv2.imread('./data/infrared_road.jpg')
# src = cv2.imread('./data/infrared_road.jpg', cv2.COLOR_BGR2HSV)
dst = src.copy()
hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)

dst2 = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
# cv2.imshow('dst2', dst2)


mask = cv2.inRange(hsv, (-30, 0, 100), (130, 255, 255)) # 241 175 108
# mask = cv2.inRange(dst, (-30, 0, 100), (130, 255, 255)) # 241 175 108
dst2 = cv2.copyTo(dst2, mask=mask)

print(src.shape)
height, width = src.shape[0:2]

h = height // 5
w = width // 7

for i in range(6):
    for j in range(8):
        y = i * h
        x = j * w

        roi = dst2[y:y + h, x:x + w]
        # dst[y:y + h, x:x + w] = cv2.mean(roi)[0] # C
        dst2[y:y + h, x:x + w] = cv2.mean(roi)[0] # [B,G,R]
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text = f'{i,j}'
        cv2.putText(dst2[y:y + h, x:x + w],text, (5, 15), font, 0.3,(255,255,255), 1)
        text2 = f'{dst2[y:y+1, x]}'
        cv2.putText(dst2[y:y + h, x:x + w],text2, (5, 40), font, 0.4,(0,255,0), 1)
            
        # print(dst2[y:y+1, x])



# 선 그리기
for i in range(w,width-w,w):
    pt1 = i,0
    pt2 = i, height
    cv2.line(dst2, pt1, pt2, (255, 255, 255), 1)
for i in range(h,height,h):
    pt1 = 0,i
    pt2 = width, i
    cv2.line(dst2, pt1, pt2, (255, 255, 255), 1)


# dst2 = src.copy()


cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
# cv2.imshow('mask', mask)
# cv2.imshow('hsv', hsv)
# cv2.imshow('copy', copy)
cv2.waitKey()
cv2.destroyAllWindows