c = int(input())

for i in range(c):
    # 테스트 케이스 학생수와 학생수만큼의 점수입력
    n= list(map(int, input().split()))
    cnt = 0
    # 학생수를 제외하고 점수만 비교교
    for i in n[1:]:
        # 학생의 점수가 평균값보다 클 때 cnt +1
        if sum(n[1:])/n[0] < i:
            cnt += 1
    # 비율구하기 => 평균값보다 큰 학생/비교한 학생 수 *100
    num = (cnt / n[0]) * 100
    
    
    print(f"{num:.3f}%")