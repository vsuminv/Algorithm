N = int(input())
nl = list(map(int,input().split()))

result = int(input())
cnt = 0
for i in nl:
    if result == i:
        cnt +=1
print(cnt)