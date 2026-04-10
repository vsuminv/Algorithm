def solution(n):
    answer = 0
    pizza = 7
    if pizza >= n :
        answer = 1
    else:
        if n % pizza == 0:
            answer = n// pizza
        else:
            
            answer = n // pizza + 1
    return answer