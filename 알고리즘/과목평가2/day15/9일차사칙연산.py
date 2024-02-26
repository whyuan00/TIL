T = 10
for tc in range(1, T+1):
    N = int(input())

    h = [0] * (N+1)
    cl = [0]  * (N+1)
    cr = [0] * (N+1)

    for _ in range(N):
        x = input().split()
        if len(x) == 2:#  입력값 두개일때
            n, key = x
            n = int(n)
            h[n] = key

        else:#  입력값 세개일때
            n, a, l, r = x
            n = int(n)
            h[n] = a
            cl[n] = l # n의 자식 인덱스
            cr[n] = r # n의 오른쪽 자식인덱스

    for n in range(N,0,-1):

        if not h[n].isdigit():
            p,q = int(cl[n]), int(cr[n])
            h[p] = int(h[p])
            h[q] = int(h[q])
            if h[n] == '+':
                h[n] = h[p] + h[q]
            elif h[n] == '-':
                h[n] = h[p] - h[q]
            elif h[n] == '*':
                h[n] = h[p] * h[q]
            elif h[n] == '/':
                h[n] = float(h[p] / h[q])


    print(f'#{tc} {int(h[1])}')



