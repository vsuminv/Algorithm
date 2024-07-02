s = arr = [[0 for j in range(100)] for i in range(100)]
n = int(input())
cnt = 0
for i in range(n):
    x , y = map(int,input().split())
    for j in range(x,x+10):
        for k in range(y, y+10):
            s[j][k] = 1
           
            
for i in range(100):
    for j in range(100):
        if s[i][j] == 1:
            cnt +=1
print(cnt)