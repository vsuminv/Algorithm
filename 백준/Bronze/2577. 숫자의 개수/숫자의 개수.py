A = int(input())
B = int(input())
C = int(input())
result = list(str(A*B*C))

cnt =[0]*10
for num in result:
    cnt[int(num)] += 1  

for count in cnt:
    print(count)