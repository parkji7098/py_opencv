# 수탉은 5달러, 암닭은 3달러, 병아리는 3마리 1달러이다.
# 100달러를 사용하여 닭 100마리를 사려면 몇마리의 수탉, 암탉, 병아리를 얻을수있을까?

m = 5
f = 3
baby = 1

for mm in range(100):
    for ff in range(100):
        for bb in range(100):
            money = m*mm + f*ff + baby*bb
            num = mm + ff + bb*3

            if money == 100 and num == 100:
                print(mm,ff,bb*3)
