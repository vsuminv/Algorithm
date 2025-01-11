sum = 0
nl = []
for i in range(5):
    n = int(input())
    sum += n
    nl.append(n)
nl.sort()
print(sum //5)
print(nl[2])
    