def solution(my_string, letter):
    answer = ''
    list_string =list(my_string)
    for i in list_string:
        if letter in list_string:
            list_string.remove(letter)
        answer = ''.join(list_string)
    return answer