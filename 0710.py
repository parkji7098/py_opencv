import cv2
import numpy as np

#1
# src = cv2.imread('./data/hand.jpg')
src = cv2.imread('./data/flower.jpg')
mask = np.zeros(shape= src.shape[:2], dtype= np.uint8)
markers = np.zeros(shape= src.shape[:2], dtype= np.int32)
dst = src.copy()
cv2.imshow('dst', dst)

#2
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:    # 마우스가 움직일 때 발생
        if flags & cv2.EVENT_FLAG_LBUTTON:  # &: 비트 연산자(둘이 비교하여 모두 1일때만 1반환)
            # param[0]은 mask, param[1]은 dst가 전달됨  # 26번 줄 참고
            cv2.circle(param[0], (x, y), 10, (255, 255, 255), -1)
            cv2.circle(param[1], (x, y), 10, (255, 255, 255), -1)
    cv2.imshow('dst', param[1])
    # print(param[1])

#3
mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
while True:
    cv2.setMouseCallback('dst', onMouse, [mask, dst]) # [mask, dst] = param[0,1]
    key = cv2.waitKey(30)

    if key == 0x1B: # ESC = 종료
        break

    elif key == ord('r'):   # r = 리셋
        mask[:,:] = 0   # mask의 모든 화소 0으로 초기화
        dst = src.copy()
        cv2.imshow('dst', dst)

    elif key == ord(' '):   # space = 영역 분할
        contours, hierarchy = cv2.findContours(mask, mode, method)  # mask에서 윤곽선 검출
        print('len(contours) = ', len(contours))
        markers[:,:] = 0

        for i, cnt in enumerate(contours):
            # print('i', i)
            # print('cnt', cnt)
            # cv2.drawContours(이미지, [윤곽선], 윤곽선 인덱스, (B, G, R), 두께, 선형 타입)
            cv2.drawContours(markers, [cnt], 0, i + 1, -1)
        cv2.watershed(src, markers)

        dst = src.copy()
        dst[markers == -1] = [0, 0, 255]    # 경계선
        for i in range(len(contours)):      # 분할 영역
            r = np.random.randint(256)
            g = np.random.randint(256)
            b = np.random.randint(256)
            dst[markers == i+1] = [b, g, r]

        dst = cv2.addWeighted(src, 0.4, dst, 0.6, 0)    # 합성
        cv2.imshow('dst', dst)
        # cv2.imshow('mask', mask)
cv2.destroyAllWindows()