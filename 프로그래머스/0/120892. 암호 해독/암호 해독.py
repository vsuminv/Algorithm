def solution(cipher, code):
    answer = ''
    cipher_list = list(cipher)
    for i in range(1,len(cipher_list)+1):
        if i % code == 0:
            answer+= cipher[i-1]

    return answer