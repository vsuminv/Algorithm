n = int(input())
user_list = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    user_list.append((age, name))

user_list.sort(key = lambda x : x[0])

for i in user_list:
    print(i[0], i[1])