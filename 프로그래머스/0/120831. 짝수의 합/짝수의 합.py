def solution(n):
   
    numbers = []
    for i in range(n+1):
        numbers.append(i)
    
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    sum = 0
    for num in even_numbers:
        sum += num
     
    return sum