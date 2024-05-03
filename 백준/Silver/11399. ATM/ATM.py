N = int(input())
P = list(map(int,input().split()))
P.sort()
sum_list = []
s = 0
for i in range(N):
    s = s+P[i]
    sum_list.append(s)
print(sum(sum_list))