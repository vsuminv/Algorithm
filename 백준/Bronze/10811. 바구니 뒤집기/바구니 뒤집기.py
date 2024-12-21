N, M = map(int,input().split())
tmp = 0
num = []
for j in range(1, N+1):
    num.append(j)
    
for i in range(M):
    i,j = map(int,input().split())
    if i == 1:  
        num[i-1:j] = num[j-1::-1]
    else:
        num[i-1:j] = num[j-1:i-2:-1]
for k in num:
    print(k, end = ' ')
