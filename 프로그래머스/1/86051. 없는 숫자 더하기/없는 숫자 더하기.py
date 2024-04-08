'''
0~9까지 숫자 중 numbers 배열에 없는 숫자 모두 더하기

for을 사용해 10까지 돌린 후 numbers 안에 숫자와 일치 하지 않으면 더하기
'''
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer