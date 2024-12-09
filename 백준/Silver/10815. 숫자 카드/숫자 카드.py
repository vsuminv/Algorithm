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