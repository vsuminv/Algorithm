import sys
N = int(input())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
r = int(input())
left = 0
right = N-1
cnt = 0

while left < right:
    if a[left] + a[right] == r:
        cnt += 1
        left += 1
    elif a[left] + a[right] > r:
        right -=1
    else:
        left += 1
print(cnt)