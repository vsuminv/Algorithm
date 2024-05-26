N = int(input())

for i in range(0,N+1):
    if i == 0:
        square = 1
    else:
        square *= 2

print((square+1)**2)

# 짧은 정답 코드
#print((2**int(input())+1)**2)