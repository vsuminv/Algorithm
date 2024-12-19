#삼각형은 가장 긴 변이 나머지 두 변의 합보다 작아야 함함

t =sorted(list(map(int, input().split())))


if t[0] + t[1] > t[2]:
    print(sum(t))
else:
    tt = t[0]+t[1] -1
    print(t[0]+t[1]+tt)