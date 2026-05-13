def solution(num, k):
    answer = 0
    n_list = list(str(num))
    
    if str(k) in n_list:
        answer = n_list.index(str(k))+1
    else:
        answer =-1
        
    return answer
        