#0507.py
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

roiX = 0
roiY = 0
roiW = 200
roiH = 200

while True:
    retval, frame = cap.read()

    preview = cv2.rectangle(frame.copy(), (roiX, roiY), (roiX+roiW, roiY+roiH), color=(0,0,255))


    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(frame_hsv)

    roi = h[roiY:roiY+roiH, roiX:roiX+roiW]

    hist = cv2.calcHist([roi], [0], None, [64], [0,255])
    backP = cv2.calcBackProject([h.astype(np.float32)], [0], hist, (0,255), scale=1)

    hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)
    T = hist[1][0] - 1

    mask = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)[1].astype(np.uint8)
    # ret, mask = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)
    # mask = mask.astype(np.uint8)

    dst = cv2.copyTo(frame, mask=mask)

    # cv2.imshow('mask', mask)
    cv2.imshow('preview', preview)
    cv2.imshow('dst', dst)
    

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()