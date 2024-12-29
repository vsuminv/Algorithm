n = int(input())
word_list = []
for i in range(n):
    word = input()
    word_list.append(word)
word_set_list =list(set(word_list))

word_set_list.sort()
word_set_list.sort(key = len)
for i in word_set_list:
    print(i)
