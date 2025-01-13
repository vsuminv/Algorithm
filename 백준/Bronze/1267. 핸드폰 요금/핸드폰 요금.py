N = int(input())
T = list(map(int,input().split()))
Y_sum = 0
M_sum = 0
for i in range(len(T)):
    if T[i] // 30 != 0:
        Y_sum += (T[i]//30) *10 + 10
    elif T[i] < 30:
        Y_sum += 10
    else:
        Y_sum += (T[i]//30) * 10

for i in range(len(T)):
    if T[i] // 60 != 0:
        M_sum += (T[i]//60) *15 + 15
    elif T[i] < 60 :
        M_sum += 15
    else:
        M_sum += (T[i]//60) * 15
if Y_sum < M_sum:
    print("Y", Y_sum)
elif M_sum < Y_sum:
    print("M", M_sum)
else:
    print("Y","M", M_sum)