def solution(food):
    answer = ''
    cal = 0
    food_list = []
    food_list_reverse = []
    
    for i in range(1,len(food)):
        cal = (food[i] //2)
        food_list += str(i)*cal
        
    
    for i in food_list:
        if i == 3:
            food_list_revesre.insert(0,'0')
        food_list_reverse.append(str(int(i)))
        food_list_reverse.sort(reverse=True)
   
        answer += i 

    return answer+'0'+''.join(food_list_reverse)