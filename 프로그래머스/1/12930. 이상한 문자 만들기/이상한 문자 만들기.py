def solution(s):
    answer = ''
    s = s.split(' ')
    word = []
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        word.append(answer)
        answer = ''
  
    return ' '.join(word)