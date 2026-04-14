def solution(my_string, n):
    answer = ''
    arr_string = list(my_string)
    for i in arr_string:
        answer += i * n
    return answer