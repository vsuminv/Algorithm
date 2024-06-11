def solution(hp):
    answer = 0
    cnt = 0
    if hp != 0:
        cnt += hp//5
        hp %= 5
        
        cnt += hp//3
        hp %= 3
        
        cnt += hp//1
        hp %= 1
    return cnt