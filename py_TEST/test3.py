# def solution(cards):
# 	answer = 0
# 	return answer

import numpy as np

cards = []
box = []
box_save = []
box_open = 0
box_save = []
box_save2 = []
group2 =0

for num in range(1,101):
    cards.append(num)
# print(cards)

Input = int(input('숫자를 입력하세요(2~100): '))

if 2 <= Input <= 100:
    box = np.random.choice(range(1,Input+1), Input, replace=False)
    print('box: ', box)
    box_Input = int(input('상자 번호 입력: '))
    # for box_Input in range(Input+1):
    if 0 <= box_Input <= Input:
        box_save.append(box_Input) 

        box_open = box[box_Input-1] 
        while not box_open in box_save:
            box_save.append(box_open)
            box_open = box[box_open-1]

        print('box_save: ', box_save)

        group1 = len(box_save)



        if group1 == 10:
            print('종료 : 점수 0')
        else:
            while True:
                box_Input2 = int(input('2그룹 상자 번호 입력: '))

                if box_Input2 in box_save:
                    print('이미 열린 상자')
                    
                else:
                    box_save2.append(box_Input2)
                    box_open = box[box_Input2-1] 

                    while not box_open in box_save2:
                        box_save2.append(box_open)
                        box_open = box[box_open-1]
                        # print('box_save2: ', box_save2)
                    
                    break

        group2 = len(box_save2)

        print('group1',group1)
        print('group2',group2)
                
        print('result: ', group1 * group2)





        #     for i in range(Input):
        #         if box[i in box_save]:
        #             continue
        #         else:
        #             box_save2.append(i) 
        #             box_open = box[i] 
        #             while not box_open in box_save2:
        #                 box_save2.append(box_open-1)
        #                 box_open = box[box_open-1]
        #                 print(box_save2)
                    
                    



                # if 0 < box_Input <= Input and box[box_Input]:
                #     box_save.append(box_Input) 

                #     box_open = box[box_Input-1] 
                #     while not box_open in box_save:
                #         box_save.append(box_open)
                #         box_open = box[box_open-1]
 
        


        
# else : print('자연수 2 ~ 100 중 입력')