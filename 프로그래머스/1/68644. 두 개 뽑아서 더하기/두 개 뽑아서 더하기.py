def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            # if numbers[i] + numbers[j] not in answer and i != j :
            #     answer.append(numbers[i] + numbers[j])
            if i != j:
                answer.append(numbers[i] + numbers[j])
    
    answer= list(set(answer))            
    answer.sort()
    return answer