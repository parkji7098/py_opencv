import cv2

class Animator():
    def __init__(self, initFunc, updateFrameFunc, interval):
        self.__initFunc = initFunc
        self.__updateFrameFunc = updateFrameFunc
        self.__interval = interval

    def show(self):
        # 처음으로 초기화 함수를 호출
        self.__initFunc()

        # 루프 지정된 간격으로 프레임을 갱신하는 함수를 호출
        while True:
            self.__updateFrameFunc()
            key = cv2.waitKey(self.__interval)
            if key == 27:
                break
        





cap = cv2.VideoCapture('./data/vtest.avi')
def init():
    retval, frame = cap.read()
    cv2.imshow('video', frame)

def updateFrame():
    retval, frame = cap.read()
    if retval:
        cv2.imshow('video', frame)

retval, frame = cap.read()
cv2.imshow('video', frame)

# 콜백함수를 연결
ani = Animator(init, updateFrame, 50)

# show, 재생시작
ani.show()

if cap.isOpened():
    cap.release()

