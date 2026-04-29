def solution(order):
    answer = 0
    order_split = list(str(order))
    
    for i in order_split:
        if int(i) in (3, 6, 9):
            answer += 1
            
    return answer