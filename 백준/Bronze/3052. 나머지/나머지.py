num = set()

for i in range(10):
    a = int(input())
    num.add(a%42)
print(len(num))