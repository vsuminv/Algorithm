def solution(n):
    answer = 0
    s = set()
    for i in range(2, n+1):
        for j  in range(2,i):
            if i % j == 0:
                s.add(i)
        
  
    return len(s)