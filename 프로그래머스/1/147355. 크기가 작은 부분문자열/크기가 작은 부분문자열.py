'''
t 문자열을 리스트에 담기
p는 int로 변환
p의 길이를 for문으로 돌려 t[:i] 이런식으로 나눠보기
'''
def solution(t, p):
    answer = 0
   
    for i in range(len(t)):
        a = t[i:i+len(p)]
        
        if len(a) == len(p):
            if t[i:i+len(p)] <= p:
                
                answer += 1
            
    # print(a)
        
    return answer