'''
s 문자열 공백 분리
'''
def solution(s):
    answer = []
    s = s.split(" ")
    
    for i in range(len(s)):
        s[i] = s[i].capitalize()
        answer.append(s[i])
        
    return " ".join(answer) 