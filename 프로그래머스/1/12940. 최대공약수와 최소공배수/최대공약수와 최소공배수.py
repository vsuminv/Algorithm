'''
최대 공약수 : 두 값이 갖는 약수 중 가장 큰 값
최소 공배수 : 두 값이 값는 배수 중 가장 작은 값 / 두 자연수의 곱 * 최대 공약수
'''
def solution(n, m):
    answer = []
    min_value = n*m
    max_value = 0
    while m != 0:
        n = n%m
        n,m = m,n
    max_value = n
    
    answer += (max_value,min_value//max_value)
        
    return answer