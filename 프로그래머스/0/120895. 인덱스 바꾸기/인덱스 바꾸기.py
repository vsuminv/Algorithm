def solution(my_string, num1, num2):
    answer = ''
    s_list = list(my_string)
    n1 = s_list[num1]
    n2 = s_list[num2]
    s_list[num1] = n2
    s_list[num2] = n1
    

    return "".join(s_list)