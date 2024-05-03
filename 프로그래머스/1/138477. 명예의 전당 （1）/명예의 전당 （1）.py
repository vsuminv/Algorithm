'''
k > len(score) 일 때는 result에 값 추가
k <= len(score) 일 때 
들어오는 값이 원래 최솟값보다 작으면 들어오는 값 제거하기, answer에 최솟값 추가
'''
def solution(k, score):
    answer = []
    result = []
    
    for i in score:
        if len(result) < k:
            result.append(i)

        else:
            result.append(i)
            if i < min(result):
                result.remove(i)
            else:
                result.remove(min(result))
        
        answer.append(min(result))
    return answer