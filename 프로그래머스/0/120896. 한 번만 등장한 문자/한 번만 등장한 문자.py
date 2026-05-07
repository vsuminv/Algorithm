def solution(s):
    answer = ''
    
    result = {i: s.count(i) for i in set(s)}
    
    for i , j in result.items():
        if j == 1:
            answer += i
    answer = list(answer)
    answer.sort()
    return "".join(answer)