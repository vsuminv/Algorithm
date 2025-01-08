N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N 

for i in A:
    r = i - B  
    if r > 0:  
        cnt += (r + C - 1) // C  

print(cnt)
