N,B =input().split()
B = int(B)
print(int(N,int(B)))

#방법 2
N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i,n in enumerate(N):
    result += (int(b)**i)*(ary.index(n))
print(result)
