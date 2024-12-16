# x좌표에 제일 큰 값 - 제일 작은 값
# y좌표에 제일 큰 값 - 제일 작은 값
# 두 값을 곱함

n = int(input())
x = []
y = []
for i in range(n):
    a ,b = map(int,input().split())
    x.append(a)
    y.append(b)
    
result = (max(x) - min(x)) * (max(y) - min(y))
print(result)