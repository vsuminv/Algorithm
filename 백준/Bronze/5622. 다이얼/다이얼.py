N = list(input())
num = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
n = 0
for i in num:
    for j in i:
        for k in N:
            if j == k:
                n += num.index(i)+3
print(n)