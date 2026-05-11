def solution(my_string):
    s = my_string.split()
    result = int(s[0])
    for i in range(1, len(s), 2):
        if s[i] == '+':
            result += int(s[i+1])
        else:
            result -= int(s[i+1])
    return result