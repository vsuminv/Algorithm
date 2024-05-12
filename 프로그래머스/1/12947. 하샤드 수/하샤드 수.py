def solution(x):
    answer = True
    
    n = list(str(x))
    s = 0
    for i in n:
        s += int(i)
    
    if x % s == 0:
        return answer
    else:
        return False
        
    # return answer