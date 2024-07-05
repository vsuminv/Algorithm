n, L  = map(int, input().split())

cnt = 0
num = 0

while cnt < n:
    num+= 1
    if str(L) in str(num):
        continue
    else:
        cnt+=1

print(num)