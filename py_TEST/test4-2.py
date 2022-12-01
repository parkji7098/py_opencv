import sys

# 91 100
# 100 100
# 95 92
# 60 70
# 87 88
# 73 85
# 84 95



teamScores = []
participantCount = 0

def inputScore():
    global participantCount
    participantCount = 0

    print('예선 준결승 점수 입력 (공백으로 구분):\n')
    
    while True:
        teamScore = []
        inputText = input()
        # print('%x' % inputText)

        inputs = inputText.split()

        # if '-1' in inputs or 'q' in inputs:
        #     break

        for inp in inputs:
            if not inp.isdigit():
                break
            
            score = int(inp)
            teamScore.append(score)

        if len(teamScore) < 2:
            continue

        participantCount += 1

        x, y = teamScore
        z = x * 0.25 + y * 0.75 #총합
        if z < 90:
            continue
    
        teamScore.append(z)

        # 결승전 참가로 기록
        teamScores.append(teamScore)


def debugInput():

    global teamScores
    global participantCount

    teamScores = [
        [91,100],
        [100,100],
        [95,92],
        [60,70],
        [87,88],
        [73,85],
        [84,95],
    ]

    participantCount = len(teamScores)

    for score in teamScores:

        x, y = score
        z = x * 0.25 + y * 0.75

        # print(f'{x} {y}')
        # print(f'{x} + {y} = {z}')

        # z = (score[0] * 0.25) + (score[1] * 0.75)
        if len(score) <= 2:
            score.append(z)
        else:
            score[2] = z
    pass

    

    # print('calTotalScore:: teamScores: ', teamScores)

def sorting():

    global teamScores

    # 1, 2, 3, 4, 5

    # 2, 1, 3, 4, 5
    # 2, 3, 1, 4, 5
    # 2, 3, 4, 1, 5
    # 2, 3, 4, 5, 1

    # 3, 2, 4, 5, 1
    # 3, 4, 2, 5, 1
    # 3, 4, 5, 2, 1

    # 4, 3, 5, 2, 1
    # 4, 5, 3, 2, 1

    # 5, 4, 3, 2, 1

    if len(teamScores) <= 0:
        return

    for i in range(len(teamScores)):
        for j in range(i, len(teamScores)-1):

            score1 = teamScores[j][2]
            score2 = teamScores[j+1][2]

            if score1 >= score2:
                break
            
            # 교체
            temp = teamScores[j]
            teamScores[j] = teamScores[j+1]
            teamScores[j+1] = temp
            pass
        
    # print('sorting:: ', teamScores)
    pass
    
def displayResult():

    print('\n출력결과:')
    print(f'참가자수: {participantCount} / 결승전 진출: {len(teamScores)}')

    if len(teamScores) <= 0:
        print('Not Found')
        return

    for score in teamScores:
        print(f'{score[0]} {score[1]} {score[2]}')

    pass



# debugInput()
# inputScore()

sorting()
displayResult()
