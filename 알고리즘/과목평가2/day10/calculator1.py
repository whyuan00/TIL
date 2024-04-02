T = 10
for tc in range(1,T+1):
    N = int(input())
    x = list(input())
    st_num = []
    st = []
    for a in x:
        if a.isdigit():
            a = int(a)
            st_num.append(a)
        else:
            st.append(a)

    M = len(st)
    while M >0:
        x = st_num.pop()
        y = st_num.pop()
        st_num.append(x+y)
        M -=1

    print(f'#{tc} {st_num}')