def solution(money):
    answer = []
    count = money // 5500
    cash = money % 5500

    answer.append(count)
    answer.append(cash)
        
    return answer