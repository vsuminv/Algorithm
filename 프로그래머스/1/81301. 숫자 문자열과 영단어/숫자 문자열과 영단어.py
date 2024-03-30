'''
딕셔러니를 사용하여 값 넣기
dic.items()를 사용하여 문자열을 찾아 숫자로 변경

'''
def solution(s):
    dic = {'zero' : 0, 'one':1, 'two':2, 'three' : 3, 'four':4, 'five':5, 'six':6, 'seven': 7, 'eight': 8, "nine":9}

    
    for i in dic.items():
        s = s.replace(i[0], str(i[1]))
        
    return int(s)
 