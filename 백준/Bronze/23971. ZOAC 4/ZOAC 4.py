import math
H, W, N, M = map(int, input().split())

odd_row = math.ceil(H / (N+1))
odd_cols = math.ceil(W / (M+1))
result = odd_row * odd_cols
print(result)