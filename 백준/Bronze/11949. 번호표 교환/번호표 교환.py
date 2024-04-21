# 입력 받기
N, M = map(int, input().split())
students = []

# 학생들의 번호표를 입력 받기
for _ in range(N):
    students.append(int(input()))

# 각 카드에 대해 작업 수행
for i in range(1, M + 1):  # 카드 i
    for j in range(N - 1):  # 학생 j
        if students[j] % i > students[j + 1] % i:
            # 조건에 따라 두 학생의 번호표 교환
            students[j], students[j + 1] = students[j + 1], students[j]

# 최종 번호표 결과 출력
for num in students:
    print(num, end=" ")