def solution(dots):
    answer = 0
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    
    w = max(x)- min(x)
    h = max(y) - min(y)
    answer= w * h
    return answer 