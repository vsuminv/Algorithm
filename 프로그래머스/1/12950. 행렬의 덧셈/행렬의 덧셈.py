def solution(arr1, arr2):
    answer = []
  
    for i in range(len(arr1)):
        sum_list = []
        for j in range(len(arr1[0])):
            sum_list.append(arr1[i][j] + arr2[i][j])
        answer.append(sum_list)
    return answer