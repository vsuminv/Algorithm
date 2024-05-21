num_max= 0
row = 0
columns = 0
for i in range(1,10):
    num = list(map(int,input().split()))
    for j in range(1,10):
        if num[j-1] >= num_max:
            num_max = num[j-1]
            row = i
            columns = j

print(num_max)
print(row, columns)