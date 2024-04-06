
def solution(strings, n):
    answer = []
    alpha = []
    for i in strings:
        alpha.append(i[n] + i)
    
    alpha.sort()
    
    for i in alpha:
        answer.append(i[1:])

    
    return answer