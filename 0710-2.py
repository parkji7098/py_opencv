#0710.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

frameSize = (
    int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
)
print('frame_size =', frameSize)


mask = np.zeros(shape=(frameSize[1], frameSize[0]), dtype=np.uint8)
markers = np.zeros(shape=(frameSize[1], frameSize[0]), dtype=np.int32)

cv2.circle(mask, (10,10), 10, (255,255,255), -1)
cv2.circle(mask, (frameSize[0]//2,frameSize[1]//2), 10, (255,255,255), -1)

while True:
    retval, frame = cap.read()
    key = cv2.waitKey(30)

    if key == 0x1B:  #esc, 27
        break

    constours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print('len(contours)=', len(constours))
    markers[:,:] = 0 #초기화

    for i, cnt in enumerate(constours):
        cv2.drawContours(markers, [cnt], 0, i+1, -1)

    cv2.watershed(frame, markers)

    dst = frame.copy()
    dst[markers == -1] = [0,0,255]  #경계선

    for i in range(len(constours)): #분할영역
        # r = np.random.randint(256)
        # g = np.random.randint(256)
        # b = np.random.randint(256)
        r = ((i+1) * 32) % 256
        g = ((i+1) * 64) % 256
        b = ((i+1) * 128) % 256
        dst[markers == i+1] = [b,g,r]
        
    dst = cv2.addWeighted(frame, 0.4, dst, 0.6, 0)  #합성

    cv2.circle(dst, (10,10), 10, (255,255,255), 2)
    cv2.circle(dst, (frameSize[0]//2,frameSize[1]//2), 10, (255,255,255), 2)

    cv2.imshow('dst', dst)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # retval, gray = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    # constours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # dst = frame.copy()
    # cv2.drawContours(dst, constours, -1, (255,255,0), 2)
    # cv2.imshow('dst', dst)

    # for i, cnt in enumerate(constours):
    #    cv2.drawContours(dst, [cnt], 0, i+1, -1)


    # constours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print('len(contours)=', len(constours))
    # markers[:,:] = 0 #초기화

cv2.destroyAllWindows()