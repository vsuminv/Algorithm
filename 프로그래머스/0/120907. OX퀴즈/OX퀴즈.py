def solution(quiz):
    answer = []
    for i in quiz:
        left, right = i.split(" = ")
        x, op, y = left.split()
        if op == '+':
            if int(x)+int(y) == int(right):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(x)-int(y) == int(right):
                answer.append("O")
            else:
                answer.append("X")
            
    return answer