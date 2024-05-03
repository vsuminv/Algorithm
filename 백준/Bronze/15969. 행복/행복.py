N = int(input())
score_list =list(map(int,(input().split())))
print(max(score_list)-min(score_list))