def solution(x, n):
    answer = [] # 빈 리스트 선언 
    for i in range(1, n+1): 
        answer.append(i*x)
 
    return answer