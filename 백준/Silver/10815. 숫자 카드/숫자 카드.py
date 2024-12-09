# 리스트를 사용해서 조회하면 O(N)
# set을 해서 조회하면 O(1)이므로 빠르게 조회 가능
# in 연산자를 사용하면 O(N) 시간이 걸리므로 시간초과 발생하기 때문에 SET 사용

N = int(input())  
cards = set(map(int, input().split()))
M = int(input()) 
query = list(map(int, input().split()))
result = []
for num in query:
    if num in cards:  
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))