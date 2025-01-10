alpha = []
word = list(input())
for a in range(0,26):
    alpha.append( chr(97+a))

for i in range(len(alpha)):
    count = 0
    for j in word:
        if alpha[i] in j:
            count += 1
    print(count, end = ' ')
    