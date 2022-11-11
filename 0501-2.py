import cv2
import numpy as np
import time

# cap = cv2.VideoCapture('./data/vtest.avi')
cap = cv2.VideoCapture(0)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

print(frame_size)

while True:
    retval, frame = cap.read()
    print(retval)
    if not retval:
        break

    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(dst, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    dst = cv2.bitwise_and(frame, frame, mask=dst)
    # dst = cv2.normalize(dst, None, 100, 200, cv2.NORM_MINMAX)
    
    print(dst)


    cv2.imshow('frame', frame)
    cv2.imshow('dst', dst)

    key = cv2.waitKey(50)

    if key == 27:
        break

cv2.waitKey()
cv2.destroyAllWindows()
