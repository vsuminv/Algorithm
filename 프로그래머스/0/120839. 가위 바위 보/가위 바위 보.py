def solution(rsp):
    answer = ''
    rsp_dict ={'0' : '5', '2':'0','5' : '2'}
    
    for i in list(rsp):
        if i in rsp_dict:
            answer += rsp_dict[i]
    return answer