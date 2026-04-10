def solution(array):
    count_dict = {}
    max_key = []
    for i in array:
        if i in count_dict:
            count_dict[i] +=1
        else:
            count_dict[i] = 1

    max_num = max(count_dict.values())
    for i,j in count_dict.items():
        if j == max_num:
            max_key.append(i)



    if len(max_key) > 1:
        return -1
    else:
        return max_key[0]