#0311.py
import cv2
import numpy as np

isDoubleClick = False

def onMouse(event, x, y, flags, param):

    global isDoubleClick

    # print('flags: ', flags)
    # print('param: ', param)
    print('event: ', event)

    # if event == cv2.EVENT_LBUTTONDBLCLK:
    #     param[0] = np.zeros(param[0].shape, np.uint8) + 255
    #     isDoubleClick = True

    # else:

    #     # if event == cv2.EVENT_LBUTTONDOWN:
    #     if event == cv2.EVENT_LBUTTONUP: #마우스 왼쪽 클릭
    #         if isDoubleClick:
    #             isDoubleClick = False
    #         elif flags & cv2.EVENT_FLAG_SHIFTKEY: # 시프트 키와 함께
    #             cv2.rectangle(param[0], (x-5, y-5), (x+5, y+5), (255,0,0))
    #         else:
    #             cv2.circle(param[0], (x,y), 5, (255,0,0), 3)

    #     elif event == cv2.EVENT_RBUTTONDOWN: # 마우스 오른쪽 클릭
    #         cv2.circle(param[0], (x,y), 5, (0,0,255), 3)

        # 1,4,7,(1,4)

    # if event == cv2.EVENT_LBUTTONDOWN: #마우스 왼쪽 클릭
    if event == cv2.EVENT_LBUTTONUP: #마우스 왼쪽 클릭

        if isDoubleClick:
            isDoubleClick = False
        elif flags & cv2.EVENT_FLAG_SHIFTKEY: # 시프트 키와 함께
            cv2.rectangle(param[0], (x-5, y-5), (x+5, y+5), (255,0,0))
        else:
            cv2.circle(param[0], (x,y), 5, (255,0,0), 3)

    elif event == cv2.EVENT_RBUTTONDOWN: # 마우스 오른쪽 클릭
        cv2.circle(param[0], (x,y), 5, (0,0,255), 3)
        
    elif event == cv2.EVENT_LBUTTONDBLCLK: # 마우스 왼쪽 버튼 더블클릭
        param[0] = np.zeros(param[0].shape, np.uint8) + 255
        isDoubleClick = True

        
    cv2.imshow('img', param[0])
    pass



#지우고 그리기
img = np.zeros((512,512,3), dtype=np.uint8) + 255 #지우기
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, [img])

# cv2.waitKey()

while True:
    key = cv2.waitKey()
    if key == 27:
        break

cv2.destroyAllWindows()