import sys

a =[]
N = int(input())
for i in range(N):
    a.append(int(sys.stdin.readline()))
a.sort()

for i in range(len(a)):
    print(a[i])