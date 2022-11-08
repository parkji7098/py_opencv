#0310.py
import cv2
import numpy as np

width, height = 512, 512
x, y, R = 256, 256, 10
direction = 0  #right
 
KEY_MAP = {
    100: 0, # 오, d
    115: 1, # 아, s
    97: 2, # 왼, a
    119: 3 #위, w
}

# (x, y)
OFFSETS = (
    (10, 0), # 오
    (0, 10), # 아
    (-10, 0), # 왼
    (0, -10) # 위
)


while True:
    key = cv2.waitKeyEx(30)
    print('key: ', key)

    if key == 0x1B: # 27(10)
        break

    # v2
    # 방향키 방향전환
    direction = KEY_MAP.get(key, direction)

    # 방향으로 이동
    offset = OFFSETS[direction]
    x += offset[0]
    y += offset[1]



    # v1
    # 방향키 방향전환
    # elif key == 0x270000:  #right
    #     direction = 0 
    # elif key == 0x280000:  #down
    #     direction = 1 
    # elif key == 0x250000:  #left
    #     direction = 2 
    # elif key == 0x260000:  #up
    #     direction = 3 
    
    # elif key == 0x27:  #right, 39(10)
    #     direction = 0 
    # elif key == 0x28:  #down, 40(10)
    #     direction = 1 
    # elif key == 0x25:  #left, 37(10)
    #     direction = 2 
    # elif key == 0x26:  #up, 38(10)
    #     direction = 3 

    # elif key == 54:  #right
    #     direction = 0 
    # elif key == 50:  #down
    #     direction = 1 
    # elif key == 52:  #left
    #     direction = 2 
    # elif key == 56:  #up
    #     direction = 3 

    # elif key == 100:  #right, d
    #     direction = 0 
    # elif key == 115:  #down, s
    #     direction = 1 
    # elif key == 97:  #left, a
    #     direction = 2 
    # elif key == 119:  #up, w
    #     direction = 3 


    # 방향으로 이동
    # if direction == 0:  # right
    #     x += 10
    # elif direction == 1: # down
    #     y += 10
    # elif direction == 2: # left
    #     x -= 10
    # else: # up
    #     y -= 10


    #경계확인 (특정 경계에 닿으면 반대 방향으로 반전)
    if x < R:
        x = R
        direction = 0 #right 로 반전
    
    if x > width - R:
        x = width - R
        direction = 2 #left 로 반전
    
    if y < R:
        y = R
        direction = 1 #down 으로 반전
    
    if y > height - R:
        y = height - R
        direction = 3 #up 으로 반전

    #지우고 그리기
    img = np.zeros((width,height,3), dtype=np.uint8) + 255 #지우기
    cv2.circle(img, (x,y), R, (0,0,255), -1)
    cv2.imshow('img', img)


cv2.destroyAllWindows()