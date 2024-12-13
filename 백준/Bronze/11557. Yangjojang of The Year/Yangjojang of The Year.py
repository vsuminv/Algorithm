n = int(input())

for i in range(n):
    max_uni = ''
    max_al = 0
    num = int(input())
    for j in range(num):
        t = input().split()
        uni = t[0]
        al = int(t[1])
        
        if al > max_al:
            max_al = al
            max_uni = uni
    print(max_uni)