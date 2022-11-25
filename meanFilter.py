import random
from matplotlib import pyplot as plt

# 50.00 ~ 51.99의 랜덤으로 생성되는 1000개의 샘플의
# 샘플이 모이는 동안 실시간 평균필터된 값을 구하고 (샘플이 추가될때마다)
# 최종 평균을 구하세요.


sampleCount = 1000
samples = []

meanPlots = []
samplePlots = []

addVal = 0

for i in range(sampleCount):
    val = random.uniform(50, 51)
    samples.append(val)
    # print('val:', val)
    # 평균필터
    # 평균 = 총합 / 갯수
    mean = sum(samples) / len(samples)

    #^ addVal += val
    # mean = addVal / (i+1)

    print(f'[{i+1}]mean: ', mean)

    samplePlots.append([val])
    meanPlots.append([mean])

print('result mean: ', mean)

plt.plot(samplePlots, color = 'b', label = 'sample')
plt.plot(meanPlots, color = 'r', label = 'mean', alpha = 0.5)
plt.legend(loc = 'best')
plt.show()

