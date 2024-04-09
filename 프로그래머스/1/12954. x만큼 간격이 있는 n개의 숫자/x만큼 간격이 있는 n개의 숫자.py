'''
for문 초기값 = x , 끝값 = n+1
answer.append(i*x)
'''
def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i*x)
    return answer