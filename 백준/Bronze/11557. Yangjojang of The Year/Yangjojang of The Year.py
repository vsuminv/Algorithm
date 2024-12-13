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
