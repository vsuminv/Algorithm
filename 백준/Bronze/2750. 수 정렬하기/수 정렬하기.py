n = int(input())

st = []
for i in range(n):
    num = int(input())
    st.append(num)
    st.sort()
for i in st:
    print(i)