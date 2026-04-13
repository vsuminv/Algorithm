def solution(array, height):
    answer = 0
    count = 0
    array.sort()
    for i in array:
        if  i <= height:
            count = 0
        else:
            count += 1
    answer = count
    return answer