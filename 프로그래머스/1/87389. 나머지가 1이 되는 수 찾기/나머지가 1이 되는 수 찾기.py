def solution(n):
    answer = 0
    x = []
    for i in range(1,n+1):    
        if n % i == 1:
            x.append(i)
    answer = min(x)      
    return answer