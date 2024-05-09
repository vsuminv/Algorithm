def solution(s):
    answer = True
 
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return answer
    else:
        return False
    