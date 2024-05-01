y, m ,d = map(int,input().split())
yy, mm ,dd = map(int,input().split())



#만나이 = 생일 기준 +1
# 생일 지났을 때
if mm > m or (m==mm and dd >= d):
    print(yy-y)
# 생일 안 지났을 때때
else:
    print(yy-y-1)
#세나이 = 원래 나이 1살, 해가 바뀌면 +1
print(yy-y+1)
#연나이 = 해가 바뀌면 +1
print(yy-y)