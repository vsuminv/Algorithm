for i in range(3):
    num = list(map(int,input().split()))
    cnt = 0
    for j in range(len(num)):
        if num[j] == 0:
            cnt += 1
    if cnt == 1:
        print("A")
    elif cnt == 2 :
        print("B")
    elif cnt == 3:
        print("C")
    elif cnt == 4 :
        print("D")
    else:
        print("E")