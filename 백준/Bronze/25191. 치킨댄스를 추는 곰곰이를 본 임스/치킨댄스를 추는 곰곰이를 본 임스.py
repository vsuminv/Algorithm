N = int(input())
c, b = map(int,input().split())

cola = c//2


cnt = cola + b

if N > cnt :
    print(cnt)
else:
    print(N)