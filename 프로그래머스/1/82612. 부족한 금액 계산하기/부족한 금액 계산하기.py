def solution(price, money, count):
    answer = 0
    
    for i in range(count+1):
        answer += price*i
        
    if answer > money:
        answer = answer - money
    else:
        answer = 0

    return answer