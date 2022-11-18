x = 0
y = 0
z = []
n = 0
List=[]
def Input(x, y):
    while True:
        global n
        # global List
        if x < 0 or y < 0 or n > 2:
            break
        n = n + 1
        x = int(input())
        y = int(input())
        List = []
        List.append(x)
        List.append(y)
        z = 0.25*x + 0.75*y
        List.append(z)
        print(List)


Input(x, y)