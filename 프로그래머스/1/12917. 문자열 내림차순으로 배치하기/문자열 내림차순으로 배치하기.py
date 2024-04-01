'''
s를 리스트로 담기
s를 정렬 후 역정렬 s.reverse() 사용
answer에 추가해줌
'''

def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    s.reverse()
    answer = ''.join(s)
    
    
    return answer