def solution(n):
    answer = 0
    
    
    num = n
    div = 6
    
    if n % 6 == 0:
        answer = n // 6
    else:
        while div != 0:
            num , div = div , num%div
    
        answer = n // num
           
            
            
    return answer