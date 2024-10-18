A,B = map(int,input().split())

result = A *B
while B != 0:
    A = A % B
    A,B = B,A
max = A
print(result//max)