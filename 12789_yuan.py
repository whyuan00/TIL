
def f():
    output = []
    st = []
    i = 1
    j = 0
    while j < N:
        if a[j] == i:
            output.append(a[j])
            i += 1
            j += 1

        else:
            if st: #st 가 있으면
                if st[-1] == i:
                    output.append(st[-1])
                    st.pop()
                    j += 1
                else:
                    st.append(a[j])
                    j +=1

            else:
                st.append(a[j])
                j += 1

    # if j == N:
    #     return 'Nice'
    # else:
    #     return 'Sad'

N = int(input())
a = list(map(int,input().split()))
print(f())

