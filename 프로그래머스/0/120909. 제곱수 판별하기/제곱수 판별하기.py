import math
def solution(n):
    answer = 0
    
    root = math.isqrt(n)
    return 1 if root * root == n else 2