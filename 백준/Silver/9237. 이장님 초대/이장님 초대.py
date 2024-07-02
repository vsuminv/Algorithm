n = int(input())
tree = list(map(int,input().split()))
tree.sort(reverse=True)

max = 0
cnt = 0
for a in range(len(tree)):
    cnt = a+tree[a]+1
    if(cnt > max):
        max = cnt
print(max+1)