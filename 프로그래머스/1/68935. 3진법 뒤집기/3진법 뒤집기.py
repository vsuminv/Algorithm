'''
진법변환 
// divmod를 사용해서도 가능
 while n >= 0:			
        n, re = divmod(n,3)	
        answer += str(re)
'''
def solution(n):
    answer = ''
    number = 0
    while n:
        answer += str(n % 3)
        n //= 3
    return int(answer,3)