T = int(input())

money = [25,10,5,1] 

for i in range(T):
    C = int(input())
    for j in money:
        print(C//j,end = ' ')
        C %= j