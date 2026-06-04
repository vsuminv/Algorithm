def solution(array):
    answer = 0
    array = list(map(str, array))
    for i in array:
        for j in i:
            if j == "7":
                answer += 1
    return answer