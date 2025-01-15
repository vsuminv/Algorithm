A = int(input())
B = int(input())
C = int(input())

result = A +B +C 

if A == B == C == 60:
    print("Equilateral")
elif result == 180:
    if A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")
elif result != 180:
    print("Error")
