N,M = map(int, input().split())

num = list(map(int, input().split()))

num.sort(reverse=True)
print(num[M-1])