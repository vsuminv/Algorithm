def solution(numer1, denom1, numer2, denom2):
    answer = []
    top = (numer1 * denom2) + (numer2 * denom1)
    bottom = denom1 * denom2
    t = top
    b = bottom
    
    while (b !=0):
        t, b = b ,t%b
    answer += (top/t, bottom/t)
    # answer[1] = bottom/t
    
    return answer