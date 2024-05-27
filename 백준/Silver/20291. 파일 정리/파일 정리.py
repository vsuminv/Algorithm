N = int(input())

file = {}

for i in range(N):
    dat = (input().split("."))[1]
    if dat in file:
        file[dat] +=1
    else:
        file[dat] = 1

result = sorted(file.items())

for k,v in result:
    print(k,v)

