def p(a,l,r):

    p = a[l]  # pivot= left
    i = l
    j = r

    while i<= j:
        while i <= j and a[i] <= p:
            i += 1
        while i<= j and a[j] >= p:
            j -= 1

        # p보다 큰수와 p보다 작은수 스왑
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j

def qs(A, l, r):

    if l < r:
        s = p(A,l,r) # s 가 pivot

        qs(A,l,s-1)
        qs(A,s+1,r )


lst = list(map(int, input().split()))
l = 0
r= len(lst)-1
qs(lst, l, r)

print(f'#{lst[500000]}')
