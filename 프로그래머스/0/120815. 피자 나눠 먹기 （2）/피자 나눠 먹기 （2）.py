def solution(n):
    answer = 0
    max_num = n
    pizza_num = 6
    if n % 6 == 0:
        answer = n // 6
    else:
        while pizza_num != 0:
                max_num , pizza_num = pizza_num, max_num % pizza_num
            
        answer = n // max_num
                
                
    return answer