r = []
test = 0
test1 = 0
result = 0
N = int(input())
for i in range(N):
    num = int(input())
    r.append(num)


x = r[1] - r[0] #등차수열
x1 = r[1] // r[0] #등비수열열

for i in range(len(r)):
    if r[i] - r[i-1] == x:
        result = r[-1]+x
    else:
        if r[i] // r[i-1] == x1:
            result = r[-1]*x1
print(result)