def solution(age):
    answer = ''
    n = {'a' : 0, 'b' :1, 'c':2, 'd' : 3 , 'e':4,'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j':9}
    age = list(str(age))
    
    for a in age:
        for i , j in n.items():
            if j == int(a):
                answer += i
    
            
        
        
    return answer