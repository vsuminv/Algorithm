'''

'''


def solution(survey, choices):
    answer = ''
    test = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        if choices[i] <= 3:
            test[survey[i][0]] += 4- choices[i]
        elif choices[i] > 4:
            test[survey[i][1]] += choices[i] -4
        else:
            continue
        

    
    print(test)
    if test['R'] >= test['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if test ['C'] >= test['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if test ['J'] >= test['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if test['A'] >= test ['N']:
        answer += 'A'
    else :
        answer += 'N'
    
    
        
#     for i in range(8,2):
#         if test_list[i][0] > test_list[i][1]:
#             answer += survey[i][0]
#         else:
#             answer += survey[i][1]
    
        

        
    return answer
    

        
    