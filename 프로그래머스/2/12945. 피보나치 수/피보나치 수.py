'''
F(n) = F(n-1) + F(n-2)

a[0] = 0, a[1] = 1 초기화 시켜줌

for문을 돌려 n번까지 더해줌
'''
def solution(n):
    answer = 0
    a = [0] * (n+1)
    a[0] = 0
    a[1] = 1
    # print(a)
    for i in range(2,n+1 ) :
        a[i] += a[i-1] + a[i-2]
        answer = a[n] %1234567
       
    
    return answer