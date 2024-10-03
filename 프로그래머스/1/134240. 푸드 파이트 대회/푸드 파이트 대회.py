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


# 다른 방법
def solution(food):
    answer = ''
    food_list = []
    food_list_re=[]
    cal = 0
    for i in range(1,len(food)):
        cal = food[i] // 2
        food_list.append(str(i)*cal)
        food_list_re.append(str(i)*cal)
    
    food_list_re.reverse()
    
        
    return ''.join(food_list)+"0"+''.join(food_list_re)
