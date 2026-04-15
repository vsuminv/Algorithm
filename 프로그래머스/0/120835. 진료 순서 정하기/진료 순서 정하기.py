def solution(emergency):
    answer = []
    
    so_emergency = sorted(emergency,reverse=True)
    

    for i in range (len(emergency)):
        # for j in range(len(so_emergency)):
        if emergency[i] in so_emergency:
            answer.append(so_emergency.index(emergency[i])+1)
            
        
        
    
    return answer