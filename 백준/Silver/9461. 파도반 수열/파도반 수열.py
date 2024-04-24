
n = int(input())
p = [0,1,1,1]

for i in range(4,101):
    p.append(p[i-2] + p[i-3])
    
for i in range(n):
    t_num = int(input())
    print(p[t_num])
    