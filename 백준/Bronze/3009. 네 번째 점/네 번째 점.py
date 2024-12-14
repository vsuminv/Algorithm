# x , y 리스트로 담음
# x, y 입력 받은 값이 1개인 것을 출력

x= []
y = []

for i in range(3):
    x1,y1 = map(int,input().split())
    x.append(x1)
    y.append(y1)


for i in range(3):
    if x.count(x[i]) == 1:
        r_x = x[i]
    if y.count(y[i]) == 1:
        r_y = y[i]
print(r_x, r_y)