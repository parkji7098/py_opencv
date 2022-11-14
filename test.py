# 공원을 아름답게 하기 위해서 봄에 꽃 종자를 구입하여 꽃길을 만들 계획이다.
# 붉은색 꽃, 노란색 꽃, 보라색 꽃을 색상별로 최소 5봉지 이상 구매하고 싶다.
# 그중 품종에 대한 요구 사항을 적어도 다음 조건 중 하나를 충족한다.

# 1. 노란색 은 빨간색꽃의 2배가 필요하다.
# 2. 보라색 꽃은 노란색 꽃의 1/3이다.

# 이 비율에 따라 구매가 진행되며 총 구매 경비 x는 (n < x <2000) 이내이며, n은 사용자가 화면에서 입력한다.
# 그중 붉은색 꽃은 한포대에 80원, 노란색꽃은 한포대에 50원, 보라색꽃은 한포대에 36원이다.
# (출력은 빨강, 노랑, 보라 세 가지 꽃의 작은 것부터 큰 것 순으로 출력하라)

re = 80
ye = 50
pu = 36

Input = int(input('숫자를 입력하세요(~2000): '))

for r in range(5,100):
    for y in range(5,100):
        for p in range(5,100):
            total = r * re + y * ye + p * pu
            if Input <= total < 2000:
                if r*2 == y or divmod(y,p) == (3,0):
                    print(f'{r},{y},{p}')


