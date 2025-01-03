N = int(input())

for i in range(1,N+1):
    n_sum = sum(map(int,str(i)))
    result = n_sum + i
    
    if result == N:
        print(i)
        break
else:
    print(0)
