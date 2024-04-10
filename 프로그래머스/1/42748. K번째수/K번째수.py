def solution(array, commands):
    answer = []
    
    for i in commands:
        num = array[i[0]-1:i[1]]
        num.sort()
        answer.append(num[i[2]-1])
    return answer