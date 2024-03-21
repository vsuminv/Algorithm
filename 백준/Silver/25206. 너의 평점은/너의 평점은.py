'''
전공 평점을 계산해주는 프로그램

전공 평점 = 전공과목(학점 * 과목평점)의 합 / 학점 총합

P/F 과목의 경우 등급이 P 또는 F, P는 계산에서 제외


input() = 수강한 전공과목명, 학점, 등급 // 공백으로 구분

'''
s = 0
gs = 0

for i in range(20):
    sub, score, grade = input().split()
    if grade == "P":
         continue
    elif grade == "A+":
        s += float(score)*4.5
        gs += float(score)
    elif grade == "A0":
        s += float(score)*4.0
        gs += float(score)
    elif grade == "B+":
        s += float(score)*3.5
        gs += float(score)
    elif grade == "B0":
        s += float(score)*3.0
        gs += float(score)
    elif grade == "C+":
        s += float(score)*2.5
        gs += float(score)
    elif grade == "C0":
        s += float(score)*2.0
        gs += float(score)
    elif grade == "D+":
        s += float(score)*1.5
        gs += float(score)
    elif grade == "D0":
        s += float(score)*1.0
        gs += float(score)
    else:
        s+= float(score)*0
        gs += float(score)

print(round((s/gs),6))


