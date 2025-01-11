sum = 0
N_list = []
for i in range(7):
    N = int(input())
    if N % 2 == 1:
        sum += N
        N_list.append(N)

if len(N_list) < 1:
    print(-1)
else:
    print(sum)
    print(min(N_list))