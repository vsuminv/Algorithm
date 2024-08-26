def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        c = 0
        for j in range(1,int(i**0.5)+1):
            if (i % j == 0):
                c += 1
                if j != i//j:
                    c += 1
        if c > limit:
            answer += power
            print(power)
        else:
            answer += c

    return answer