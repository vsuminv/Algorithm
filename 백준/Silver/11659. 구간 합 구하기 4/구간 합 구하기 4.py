import sys
n , m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num_list = [0]
s = 0
for i in num:
    s += i
    num_list.append(s)



  
for j in range(m):
    a, b= map(int, sys.stdin.readline().split())
    print(num_list[b]-num_list[a-1])