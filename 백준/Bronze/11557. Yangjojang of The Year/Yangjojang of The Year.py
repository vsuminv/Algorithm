n = int(input())

for i in range(n):
    max_uni = ''
    max_al = 0
    num = int(input())
    for j in range(num):
        t = input().split()
        uni = t[0]
        al = int(t[1])
        
        if al > max_al:
            max_al = al
            max_uni = uni
    print(max_uni)

#딕셔너리 방법
T = int(input()) 

for _ in range(T):
    N = int(input())   
    school_dict = {}  

    for _ in range(N):
        data = input().split()  
        school = data[0]  
        liquor = int(data[1]) 
        school_dict[school] = liquor  

    max_school = max(school_dict, key=school_dict.get)
    print(max_school) 
