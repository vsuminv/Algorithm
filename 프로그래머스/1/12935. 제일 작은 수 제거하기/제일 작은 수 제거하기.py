def solution(arr):
    answer = []
    
    min_arr = min(arr)
    
    if len(arr) <= 1:
            answer.append(-1)
    
    for i in arr :
        if min_arr == i:
            continue
        else:
            answer.append(i)
        
    return answer