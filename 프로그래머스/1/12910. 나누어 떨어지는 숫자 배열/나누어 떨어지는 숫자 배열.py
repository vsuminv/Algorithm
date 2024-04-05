'''
arr 배열 정렬
arr 배열을 for문으로 돌려 divisor과 나눠지는 수를 answer에 저장
없다면 -1
'''
def solution(arr, divisor):
    answer = []
    cnt = 0
   
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            cnt+=1
    if cnt == 0:
        answer = [-1]
    answer.sort()     
    
    return answer