while True:
    N = input()
    if N =='0':
        break
    else:
        if N == N[::-1]:
            print("yes")
        else:
            print("no")