num = []

for i in range(1,21):
    num.append(i)
for i in range(10):
    n1, n2 = map(int,input().split())
    if n1 == 1:
        num[n1-1:n2] = num[n2-1::-1]
    else:
        num[n1-1:n2] = num[n2-1:n1-2:-1]
for i in num:
    print(i, end = ' ')