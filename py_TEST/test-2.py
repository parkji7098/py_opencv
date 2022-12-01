import random

CARD_MAX = 100

cards = []

keepGroups = []
scores = []
opened = []

def solution():

  global cards

  # global keepGroups
  # global scores
  # global opened
  
  # keepGroups = []
  # scores = []
  # opened = []
  
  while True:

    # 임의의 상자를 선택
    n = random.randrange(1, len(cards)+1)
    # n = random.choice(cards)
    # print('n: ', n)

    # [3, 6, 8, 1, 4, 7, 2, 5]
    # 임의 1(0) -> 3 (opened 1)
    # 3(2) -> 8 
    # 8(7) -> 5 (opened 8)
    # 5(4) -> 4 
    # 4(3) -> 1 (opened 4)
    # 1(0) (열어본 숫자 -> break)


    # opened [6,7,2]
    # 1 - 10
    # [3, 6, 8, 1, 4, 7, 2, 5, 9, 10]
    # n = 6(상자), n = 7, n = 2, n = 6
    # num = 7, num = 2, num = 6

    group = []

    while True:
      
      # print('num: ', num)
      if n in opened:
        break

      # for i in range(len(opened)):
      #   onum = opened[i]
      #   if n == onum:
      #     break

      # for n in opened:
      #   if n == num:
      #     break

      # 해당 번호의 상자 안에 들어 있었던 카드의 숫자
      num = cards[n-1]
      # num2 = cards[num - 1]

      opened.append(n)
      group.append(n)
    
      n = num

    # print('group: ', group)
    # print('opened: ', opened)
    # print('cards: ', cards)

    # keepGroups = [group1[], group2[]]
    # scores = [3, x]
    if len(group) > 0:
      keepGroups.append(group)
      scores.append(len(group))

    # print('keepGroups: ', keepGroups)

    # 모든카드가 열려있으면 결과 보기
    # # closedList = [card for card in cards if card not in opened]
    # # [] => False
    # # if not closedList:
    # if not [card for card in cards if card not in opened]:
    #   break

    # isContinue = True
    # for i in range(len(cards)):
    #   cardNum = cards[i]
    #   for j in range(len(opened)):
    #     openNum = opened[j]
    #     result = cardNum == openNum

    #     isContinue = isContinue and result
    #     # True, True, True, True, True == True
    #     # True, True, False, True, True == False

    #     # end = end and cardNum == openNum

    # if not isContinue:
    #   break

    if len(cards) == len(opened):
      break


def openBoxRecursion(n, group:list):
  # print('n: ', n)
  # print('group: ', group)

  if n in opened:
    # print('group: ', group)
    return group

  num = cards[n-1]
    # print('num: ', num)

  group.append(n)
  opened.append(n)

  openBoxRecursion(num, group)
  return group


def solutionRecursion():
  
  # 임의의 상자를 선택
  n = random.randrange(1, len(cards)+1)
  # n = random.choice(cards)
  # print('n: ', n)

  # 카드 열어보기
  
  # 반복문
  # group = []
  # while True:
    
  #   if n in opened:
  #     break

  #   num = cards[n-1]
  #   # print('num: ', num)

  #   group.append(n)
  #   opened.append(n)
  #   n = num

  # 재귀
  group = openBoxRecursion(n, [])
  # print('group: ', group)
  # # print('opened: ', opened)
  # # print('cards: ', cards)

  if len(group) > 0:
    keepGroups.append(group)
    scores.append(len(group))
    # print('keepGroups: ', keepGroups)

  # 카드가 모두 열려있는지 확인
  if not [card for card in cards if card not in opened]:
    return

  # if len(cards) == len(opened):
  #   return

  # 재귀
  solutionRecursion()


def displayResult():

  # 내림차순 정렬
  scores.sort(reverse=True)
  # print('scores: ', scores)
    
  # 결과 출력
  print('\n:::result:::\n')
  for keep in keepGroups:
    print(keep)

  print()

  if (len(scores) <= 1):
    print(f'score: {scores[0]} x 0 = 0')
  else:
    print(f'score: {scores[0]} x {scores[1]} = {scores[0] * scores[1]}')

  print()

if __name__ == '__main__':

  while True:

    # ---- 초기화
    # global keepGroups
    # global scores
    # global opened
    
    keepGroups = []
    scores = []
    opened = []

    # ---- 사용자 입력
    inputText = input('카드의 수를 입력하세요(2이상 100이하): ')

    if not inputText.isdigit():
      continue

    inputDigit = int(inputText)
    if inputDigit < 2 or inputDigit > 100:
      continue

    # ---- 지정된 수 만큼 순차적으로 숫자를 생성해서 리스트에 담고 순서를 랜덤으로 섞음

    # 랜덤 위치에 생성
    # cards = random.sample([i+1 for i in range(inputDigit)], inputDigit)

    # 생성
    cards = [i+1 for i in range(inputDigit)]
    # 섞기
    # random.shuffle(cards)

    # 직접구현
    for i in range(len(cards)):
      ri = random.randrange(0, len(cards))

      temp = cards[i]
      cards[i] = cards[ri]
      cards[ri] = temp

    # cards = [8,6,3,7,2,5,1,4]

    # print('cards: ', cards)

    # ---- 게임 진행
    # 반복문
    solution()

    # 재귀
    # solutionRecursion()

    # 결과확인
    displayResult()



