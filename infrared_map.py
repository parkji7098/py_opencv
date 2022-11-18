import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

# ------------------ 진행에 필요한 소스와 변수 준비
src = cv2.imread('./data/infrared_road.jpg')
cv2.imshow('src', src)

# 한블럭안에 픽셀의 갯수는 58x70 = 4060
blockN = (5,7) # row, col

# shape: height, width, channel
height, width = src.shape[0:2]
bh = height // blockN[0]
bw = width // blockN[1]

# 5x7 (row, col) 내에 장애물 위치 표기
# 숫자가 1이상이면 장애물 (장애물은 실제 온도맵에서 -1로 기록됨)
obstacleMap = [
  [0,0,0,0,0,0,0],
  [0,1,1,0,1,1,0],
  [0,0,0,0,0,0,0],
  [0,1,1,0,1,1,0],
  [0,0,0,0,0,0,0],
]

print('src height,width : ', (height, width))
print('block height,width : ', (bh, bw))


tempMap = []
currentPosition = [4,6]
heatCoord = []

# ------------------ 기능처리를 위한 함수 구성

def originToCoordinate(orign, blockSize):
    oRow, oCol = orign
    row = oRow // blockSize[0]
    col = oCol // blockSize[1]

    return row, col



def parsingTempMap() -> cv2.Mat:
  global src

  hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
  hsv_mask = cv2.inRange(hsv, (-50,0,100), (130,255,255))
  # redMat = cv2.copyTo(hsv, mask = hsv_mask)
  # result = cv2.cvtColor(redMat, cv2.COLOR_HSV2BGR)
  result = cv2.copyTo(src, mask = hsv_mask)
  gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

  # tempMat = np.zeros((blockN[0], blockN[1]), np.uint8)
  tempMat = np.zeros((blockN[0], blockN[1]), np.int16)

  for y in range(0, blockN[0]):
    for x in range(0, blockN[1]):
      point = (y*bh,x*bw)
      coord = originToCoordinate(point, (bh, bw))
      # print('coord: ', coord)
      
      blockVal = 0

      if obstacleMap[coord[0]][coord[1]] > 0:
        # 장애물 위치
        blockVal = -1
      else:
        # 해당 블록의 평균구하기
        block = gray[point[0]:point[0]+bh, point[1]:point[1]+bw]
        # cv2.imshow(f'{coord}', block)

        # np.mean()
        blockVal = round(cv2.mean(block)[0])
        # print(f'{coord}, ', blockVal)

        if blockVal > 0:
          heatCoord.append((coord, blockVal))

      tempMat[coord[0], coord[1]] = blockVal

      # hist = cv2.calcHist([gray],[0],None,[5],[0,256])
      # print('hist: ', hist)

  # 로그로 확인
  for row in tempMat:
    for col in row:
      print(f'{col:>3}', end='  ')
    print('\n')

  return tempMat


def displayTempMap():

  global src
  global tempMap

  dst = src.copy()

  for y in range(0, blockN[0]):
    lineY = min(y+1, blockN[0]-1)
    cv2.line(dst, (0,lineY*bh), (width, lineY*bh), color=(255,255,255), thickness=1)

    for x in range(0, blockN[1]):
      lineX = min(x+1, blockN[1]-1)
      cv2.line(dst, (lineX*bw,0), (lineX*bw, height), color=(255,255,255), thickness=1)

      # 장애물 위치면
      if obstacleMap[y][x] > 0:
        # x표시
        cv2.line(dst, (x*bw, y*bh), (x*bw + bw, y*bh + bh), color=(255,255,255), thickness=1)
        cv2.line(dst, (x*bw + bw, y*bh), (x*bw, y*bh + bh), color=(255,255,255), thickness=1)

      cv2.putText(dst, f'{tempMap[y,x]}', (x*bw + 5, y*bh + (bh - 15)), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,255,0), 2)
      cv2.putText(dst, f'{y},{x}', (x*bw + 5, y*bh + 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (255,255,255), 1)
  
  cv2.imshow('Debug Map', dst)


# 거리계산
def distanceFromCoordinate(firstPoint, secondPoint):

  # 맨하튼거리
  x1, y1 = firstPoint
  x2, y2 = secondPoint

  distance = abs(x1 - x2) +  abs(y1 - y2)
  return distance


# 열이 발생되는 지점 중 가까운 위치
def findHeatAndNearCoordinate():

  minDistance = 999
  targetHeat = None

  for heat in heatCoord:
    coord, heatVal = heat
    distance = distanceFromCoordinate(currentPosition, coord)

    if heatVal >= 40 and minDistance >= distance:
    # if (not targetHeat) or (targetHeat[1] >= 40 and minDistance >= distance):
      minDistance = distance
      targetPoint = coord
      targetHeat = heatVal

      targetHeat = heat

    # print(f'{coord} h:{heat} d:{distance}')

  print(f'targetHeat: {targetHeat}')

  return targetHeat


# 길찾기
class Node:
  def __init__(self, pos, parent=None) -> None:
    self.position = pos
    self.parent = parent

def findPathFromCoordinate(firstPoint, secondPoint):

  # DFS
  visitedList = []
  nodeQueue = []

  startNode = Node(firstPoint, None)
  nodeQueue.append(startNode)

  while nodeQueue:

    node = nodeQueue.pop()
    # print('node: ', node)
    visitedList.append(node)

    # 현재노드가 도착지인지 파악
    if node.position[0] == secondPoint[0] and node.position[1] == secondPoint[1]:
      # 도착지라면 노드의 부모를 추적하여 경로 생성 및 리턴
      path = []
      
      # 현재 노드가 도착노드라 현재 노드부터 확인하고 추가하고 시작
      checkNode = node
      while checkNode:
        # path.append(checkNode.position)
        path.insert(0, checkNode.position)

        parent = checkNode.parent
        checkNode = parent
        pass

      return path

    # 상하좌우 경로 검색
    for offset in ((0,1), (1,0), (0,-1), (-1,0)):

      nY, nX = node.position
      
      # 자식노드 생성
      nextY = nY + offset[0]
      nextX = nX + offset[1]
      childNode = Node((nextY, nextX), node)

      # 자식노드가 유효범위 위치인지 확인
      if nextY < 0 or nextY >= blockN[0] or nextX < 0 or nextX >= blockN[1]:
        continue

      # 자식노드가 이동가능 위치인지 확인 (장애물확인)
      if obstacleMap[nextY][nextX] > 0:
        # 장애물 위치
        continue

      # 자식노드가 아직 방문하지 않았고, 노드큐에 없는 노드라면 탐색 가능 노드로 기록
      if (not [vNode for vNode in visitedList if vNode.position[0] == childNode.position[0] and vNode.position[1] == childNode.position[1]]
        and not [qNode for qNode in nodeQueue if qNode.position[0] == childNode.position[0] and node.position[1] == childNode.position[1]]):

        nodeQueue.append(childNode)
        pass


  

# ------------------ 코드 진행

# 지도를 파악해서 일정 구역으로 나눠 온도지도를 만든다
tempMap = parsingTempMap()
# 파악된 온도지도를 표시
displayTempMap()

# tempMap의 좌표를 기준으로 현재 가장 가까운 온도가 높은 위치를 찾고
targetHeat = findHeatAndNearCoordinate()

# 현재 위치에서 해당위치로 길찾기 시도
path = findPathFromCoordinate(currentPosition, targetHeat[0])
print(f'path: {path}')


cv2.waitKey()
cv2.destroyAllWindows()
