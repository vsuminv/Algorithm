subject = int(input())
score = list(map(int,input().split()))
max_score = max(score)
avg = 0
score_list = []

for i in range(subject):
    score_list.append(score[i]/max_score*100)
print(sum(score_list)/subject)
