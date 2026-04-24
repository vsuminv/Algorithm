def solution(n):
    answer = set()
    
    d=2

    while n!=1:            
        while n%d==0:
            n=n//d  
            answer.add(d)
        d=d+1
        
    if n > 1:
        answer.add(n)
    a = sorted(list(answer))
    # list(answer).sort()
    return a