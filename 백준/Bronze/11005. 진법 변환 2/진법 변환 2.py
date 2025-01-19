A,B = map(int,input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ''

while A > 0:
    result += str(ary[A%B])
    A = A//B
print(result[::-1])
